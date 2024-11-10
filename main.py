import asyncio
from aiogram.methods import DeleteWebhook
from aiogram import Bot, Dispatcher

from app.handlers import router
from config_file.cfg import token


bot = Bot(token=token)
dp = Dispatcher()


async def get_photo(photo):
    file_id = photo.file_id  # Получаем ID самого высокого качества фото
    file = await bot.get_file(file_id)  # Получаем информацию о файле
    file_path = file.file_path  # Путь к файлу на серверах Telegram
    url = f'https://api.telegram.org/file/bot{token}/{file_path}'
    return url

async def main():
    dp.include_router(router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print("Start")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")