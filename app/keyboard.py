from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.db_func import get_user_query_info

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Мои запросы'), KeyboardButton(text='Информация')]
    ],
    resize_keyboard=True
)

def rotation_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Поворот налево', callback_data='rotate_left'),
            InlineKeyboardButton(text='Поворот направо', callback_data='rotate_right')
        ],
        [
            InlineKeyboardButton(text='Перевернуть', callback_data='rotate_upside_down'),
            InlineKeyboardButton(text='Отправить', callback_data='send_photo')
        ]
    ])
    return keyboard

async def user_last_rec(user_id):
    keyboard = InlineKeyboardBuilder()
    records = get_user_query_info(user_id)
    if not records:
        keyboard.add(InlineKeyboardButton(text="Вы еще не делали запросов", callback_data='inforec_dec'))
        return keyboard.adjust(1).as_markup()
    for rec in records[:10]:
        keyboard.add(InlineKeyboardButton(text=rec, callback_data=f'inforec_{rec}'))
    return keyboard.adjust(1).as_markup()
