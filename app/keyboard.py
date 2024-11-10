from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


from data.db_func import get_user_rec_info


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Мои запросы'), KeyboardButton(text='Информация')]
    ],
    resize_keyboard=True
)


async def user_last_rec(user_id):
    keyboard = InlineKeyboardBuilder()
    records = get_user_rec_info(user_id)
    if len(records) == 0:
        keyboard.add(InlineKeyboardButton(text="Вы еще не делали запросов", callback_data=f'inforec_dec'))
        return keyboard.adjust(1).as_markup()
    for rec in range(min(len(records), 10)):
        keyboard.add(InlineKeyboardButton(text=records[rec], callback_data=f'inforec_{records[rec]}'))
    return keyboard.adjust(1).as_markup()