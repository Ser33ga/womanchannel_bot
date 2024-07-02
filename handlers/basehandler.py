from aiogram import Router
from aiogram import Bot, F
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram import Dispatcher

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import Command, StateFilter

from aiogram.filters.logic import or_f

from filters.basefilters import IsAdmin, IsParser

from settings.settingspy import admin_id, parser_id

from keyboards.inline.inline_keyboard import inline_keyboard_agree, inline_keyboard_choose_category

router = Router()

@router.message()
async def my_message(message: Message, bot: Bot, ):
    await bot.copy_message(chat_id=admin_id, from_chat_id=message.chat.id, message_id=message.message_id, reply_markup=inline_keyboard_agree)

@router.callback_query(F.data == 'like')
async def my_message(callback: CallbackQuery, bot: Bot):
    original_message = callback.message
    message_id = original_message.message_id
    chat_id = original_message.chat.id
    await bot.copy_message(chat_id=admin_id, from_chat_id=chat_id, message_id=message_id, reply_markup=inline_keyboard_choose_category)

@router.callback_query(F.data == 'dislike')
async def my_message(callback: CallbackQuery):
    await callback.answer('отказано')

@router.callback_query(or_f(F.data == '-1002232311428', F.data == '-1002072920591'))
async def my_message(callback: CallbackQuery, bot: Bot):
    original_message = callback.message
    message_id = original_message.message_id
    chat_id = original_message.chat.id
    await bot.copy_message(chat_id=callback.data, from_chat_id=chat_id, message_id=message_id)
    await callback.answer("отправлено")
