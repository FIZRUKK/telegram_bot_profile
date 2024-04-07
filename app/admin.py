import asyncio
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import  Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


import app.keyboards as kb
from app.database.requests import get_users, get_count_users

from config import ADMINS


admin = Router()

admins = ADMINS


class Newsletter(StatesGroup):
    message = State()

    
class AdminProtect(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id in admins

@admin.message(AdminProtect(), F.text == 'Админка')
async def main_admin(message: Message):
    await message.answer('Добро пожаловать в админку!', reply_markup=kb.admin)
    
@admin.message(AdminProtect(), F.text == 'Рассылка')
async def newsletter(message: Message, state: FSMContext):
    await state.set_state(Newsletter.message)
    await message.answer('Введите сообщение')

@admin.message(AdminProtect(), Newsletter.message)
async def newsletter_message(message: Message, state: FSMContext):
    await message.answer('Идет рассылка')
    sent_messages = []
    
    for user in await get_users():
        try:
            sent_message = await message.send_copy(chat_id=user.user_id)
            info_sent_msg = (sent_message.message_id, user.user_id)    
            sent_messages.append(info_sent_msg)
        except:
            pass
        
    await message.answer('Рассылка выполнена')
    await state.clear()
    await asyncio.sleep(600)  # Ждем 10 минут
    for user in sent_messages:
        message_id = user[0]
        chat_id = user[1]
        try:
            await message.bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

@admin.message(F.text == 'Кол-во пользователей')
async def count_users(message: Message):
    count = await get_count_users()
    sent = await message.answer(f"Кол-во пользователей {count}")
    await asyncio.sleep(3)
    for admin in admins:
        try:
            await message.bot.delete_messages(chat_id=admin, message_ids=[sent.message_id,message.message_id])
        except:
            pass

