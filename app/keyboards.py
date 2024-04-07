from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

main = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Обо мне', callback_data = 'about_me')],
    [InlineKeyboardButton(text = 'Портфолио', callback_data = 'portfolio'), InlineKeyboardButton(text = 'FAQ', callback_data = 'FAQ')],
    [InlineKeyboardButton(text = 'Оставить заявку', callback_data = 'call_me')]
    # [InlineKeyboardButton(text = 'Связаться', url='https://t.me/FizRukkkkkk')]
])

back = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
])

back_faq = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back_faq')]
])

portfolio = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Анонимные вопросы', url = 'https://t.me/AnonymousAsksBot'), InlineKeyboardButton(text = 'GiveShareBot', url = 'https://t.me/GiveShareBot')],
    [InlineKeyboardButton(text = 'Скачать Рилс? Изи!', url = 'https://t.me/reels_get_video_bot'), InlineKeyboardButton(text = 'Віt🔷Маrt Тrаdе', url = 'https://t.me/Bitmart_Trade_Bot')],
    [InlineKeyboardButton(text = 'CHATGPT4BOT', url = 'https://t.me/chat9pt_bot'), InlineKeyboardButton(text = 'КАЛЬКУЛЯТОР ПРОДАЖ', url = 'https://t.me/calculator_reaktive_bot')],
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
])

faq = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text = 'Какая гарантия на работу бота?', callback_data = 'guarantee')],
    [InlineKeyboardButton(text = 'Какая поддержка предоставляется?', callback_data = 'support ')],
    [InlineKeyboardButton(text = 'Как часто обновляется бот?', callback_data = 'updates')],
    [InlineKeyboardButton(text = 'Безопасен ли бот?', callback_data = 'safe')],
    [InlineKeyboardButton(text = 'Как защищены данные клиента?', callback_data = 'data')],
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
]) 

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Начать', callback_data='start')]
])

contact = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Поделиться контактом', request_contact=True)],
    [KeyboardButton(text = 'Нет, спасибо')],     
],resize_keyboard=True, input_field_placeholder='Поделитесь контактом...', one_time_keyboard=True)


admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Рассылка')],
    [KeyboardButton(text = 'Кол-во пользователей')]
],resize_keyboard=True, input_field_placeholder='Админ-панель...', one_time_keyboard=True)

about_me = InlineKeyboardMarkup(inline_keyboard=[
    
    [InlineKeyboardButton(text='VK', url='https://vk.com/daniil.grebnev'),InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/danya.gebnev')],
    [InlineKeyboardButton(text = 'Назад', callback_data='back')]
    
])