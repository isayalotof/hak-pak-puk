import asyncio
from aiogram.methods import DeleteWebhook
from aiogram import Bot, Dispatcher

from app.handlers import router
from config_file.cfg import token


bot = Bot(token=token)
dp = Dispatcher()


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