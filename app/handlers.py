from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ContentType
from app import keyboard as kb
from fsm import user_fsm
from main import get_photo
from app.func import download_file
from aiogram.fsm.context import FSMContext
from data.db_func import get_user_rec_info

import base64
from api.api import ai_photo_work
from data.db_func import add_user_search


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(f'Здравствуйте, {message.from_user.first_name.capitalize()}'
                         'Для распознавания детали, пришлите ее фото.'
                         'Посторайтесь сделать четкую фотографию',
                         reply_markup=kb.main)
    await state.set_state(user_fsm.HoldJson.resp_json)


@router.message(F.text == 'Мои запросы')
async def new_record(message: Message):
    await message.answer('Ваши последние 10 запросов:', reply_markup = await kb.user_last_rec(message.from_user.id))


@router.message(F.text == 'Информация')
async def my_info(message: Message):
    await message.answer("Информация, когда мне датут тг админа я прифигачу сюда его контакты, а пока хз")


@router.message(content_types=ContentType.PHOTO)
async def handle_photo(message: Message, state: FSMContext):
    file_path = 'data/photo.jpg'
    await download_file(await get_photo(message.photo[-1].file_id), file_path)
    with open("data/photo.jpg", "rb") as image_file:
        await state.update_data(resp_json=ai_photo_work(base64.b64encode(image_file.read()).decode("utf-8")))
    data = await state.get_data()
    info = 'тут информация'
    await message.answer(info)
    add_user_search(message.from_user.id, data['resp_json']['name'], info)


@router.callback_query(F.data.startswith('inforec_'))
async def set_place(callback: CallbackQuery, state: FSMContext):
    info = get_user_rec_info(callback.from_user.id, callback.data.replace('inforec_', ''))
    await callback.message.edit_text(info)








