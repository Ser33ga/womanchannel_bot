import asyncio
from environs import Env
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Router

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup

from aiogram.fsm.storage.memory import MemoryStorage

from settings.settingspy import bot_token, admin_id

from handlers.basehandler import router

BOT_TOKEN='7410131654:AAEY3S3bmbWQs3SzrwWMRxvs8Z1-vBDC_lY'

async def main():
    storage = MemoryStorage()

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher(storage=storage)

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())