from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Мои запросы'), KeyboardButton(text='Информация')]
    ],
    resize_keyboard=True
)


user_choise = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Подтвердить', callback_data='req_yes')],
        [InlineKeyboardButton(text='Попробовать еще раз', callback_data='req_dec')],
    ]
)