from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from app import keyboard as kb
from aiogram.fsm.context import FSMContext


db_path = "data.db"
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name.capitalize()} ',
                         reply_markup=kb.main)

