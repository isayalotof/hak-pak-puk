from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ContentType, FSInputFile, InputMediaPhoto
from app import keyboard as kb
from fsm import user_fsm
from app.func import download_file, encode_image, decode_image
from aiogram.fsm.context import FSMContext
from data.db_func import get_user_rec_info, add_user_search
from api.api import ai_photo_work
from app import func as fn
from app.bot import bot

from data.poisk import find_detail_info

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        f'Здравствуйте, {message.from_user.first_name.capitalize()}!\n'
        'Для распознавания детали, пришлите её фото.\n'
        'Постарайтесь сделать чёткую фотографию.',
        reply_markup=kb.main
    )
    await state.set_state(user_fsm.Hold.resp_json)


@router.message(F.text == 'Мои запросы')
async def new_record(message: Message):
    await message.answer('Ваши последние 10 запросов:', reply_markup=await kb.user_last_rec(message.from_user.id))


@router.message(F.text == 'Информация')
async def my_info(message: Message):
    await message.answer("Информация: когда мне дадут контакт администратора, я добавлю его сюда.")


@router.message(F.content_type == ContentType.PHOTO)
async def handle_photo(message: Message, state: FSMContext):
    file_path = f'img/photo_{message.from_user.id}.jpg'
    await download_file(await fn.get_photo(message.photo[-1].file_id), file_path)
    img = fn.encode_image(fn.load_image(file_path))
    await state.set_state(user_fsm.Hold.img_base64)
    await state.update_data(img_base64=img)

    # Используем FSInputFile
    photo = FSInputFile(file_path)
    await message.answer_photo(photo=photo, reply_markup=kb.rotation_keyboard())


@router.callback_query(F.data.in_({'rotate_left', 'rotate_right', 'rotate_upside_down', 'send_photo'}))
async def handle_rotation(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    img_base64 = data.get('img_base64')

    if callback.data == 'rotate_left':
        img_base64 = fn.rotate_photo_on_the_left(img_base64)
    elif callback.data == 'rotate_right':
        img_base64 = fn.rotate_photo_on_the_right(img_base64)
    elif callback.data == 'rotate_upside_down':
        img_base64 = fn.rotate_photo_upside_down(img_base64)
    elif callback.data == 'send_photo':
        # Обработка изображения через API
        response = ai_photo_work(img_base64)
        if response.status_code == 200:
            result = response.json()
            article = result.get('text', 'Информация не найдена.')

            # Поиск информации по артикулу
            info = find_detail_info(article)

            add_user_search(callback.from_user.id, 'Запрос пользователя', info)
            await callback.message.answer(info)
        else:
            await callback.message.answer('Произошла ошибка при обработке изображения.')
        await state.clear()
        return

    # Сохраняем обновленное изображение в состоянии
    await state.update_data(img_base64=img_base64)

    # Отправляем обновленное изображение
    img = fn.decode_image(img_base64)
    img_path = f'img/photo_{callback.from_user.id}.jpg'
    img.save(img_path)

    # Используем FSInputFile и InputMediaPhoto
    photo = FSInputFile(img_path)
    media = InputMediaPhoto(media=photo)
    await callback.message.edit_media(media=media, reply_markup=kb.rotation_keyboard())
    await callback.answer()



