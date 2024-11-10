import asyncio
from aiogram.methods import DeleteWebhook
from app.bot import bot, dp
from app.handlers import router

async def main():
    dp.include_router(router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)  # Убедитесь, что bot уже передан в Dispatcher

if __name__ == '__main__':
    try:
        print("Start")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
