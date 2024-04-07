from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto, ContentType
from aiogram.filters import CommandStart


import app.keyboards as kb
from app.database.requests import input_user, get_user_info_by_id
from config import ADMINS

rt = Router()
admins = ADMINS

id_messages = [] # Чтобы удалить ненужные сообщения


# start
@rt.message(CommandStart())
async def cmd_start(message: Message):
    main_photo = 'AgACAgIAAxkBAAMUZhKEpH9qedQTS-dlgvhaWgAB0mdoAALn2DEbRRaRSHypFGK9B-o4AQADAgADeQADNAQ'
    text = '<b>Поделитесь контактом нажав на кнопку <u>Поделиться контактом</u>, что бы я мог оперативно с вами связаться</b>'
    sent_message_bot = await message.answer_photo(photo=main_photo, caption=text, reply_markup = kb.contact)
    sent_message_user = message.message_id
    id_messages.append(sent_message_bot.message_id)
    id_messages.append(sent_message_user)

# Share contact
@rt.message(F.content_type == ContentType.CONTACT)
async def get(message: Message):
    main_photo = 'AgACAgIAAxkBAAMYZhKE95Vex57QUk5SHVMZwfFalPoAAu3YMRtFFpFIzEHk3ScTXHUBAAMCAAN5AAM0BA'
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    phone_number = f'+{message.contact.phone_number}'
    
    await input_user(user_id, user_name, first_name, last_name, phone_number)
    text = f'<b>Доброго времени суток <i>{first_name}</i>\n\nРад вас видеть в своем телеграм-боте\nВы можете ознакомиться с частичкой моих работ и заказать\n\n<u>ЛУЧШЕЕ РЕШЕНИЕ</u> - для вашего бизнеса\n\nОставьте заявку, и я свяжусь с вами в самые короткие сроки!</b>'
    await message.answer_photo(photo=main_photo, caption=text, reply_markup=kb.main)
    
    message_id_bot = id_messages[0]
    message_id_user = id_messages[1]
    message_id_user2 = message.message_id
    
    try:
        await message.bot.delete_messages(chat_id=user_id, message_ids=[message_id_bot, message_id_user, message_id_user2])
    except:
        pass
    
    id_messages.clear()

    
# Not share
@rt.message(F.text == 'Нет, спасибо')  
async def not_share_contact(message: Message):
    main_photo = 'AgACAgIAAxkBAAMYZhKE95Vex57QUk5SHVMZwfFalPoAAu3YMRtFFpFIzEHk3ScTXHUBAAMCAAN5AAM0BA'
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    phone_number = 'Без номера'
    await input_user(user_id, user_name, first_name, last_name, phone_number)
    text = f'<b>Доброго времени суток <i>{first_name}</i>\n\nРад вас видеть в своем телеграм-боте\nВы можете ознакомиться с частичкой моих работ и заказать\n\n<u>ЛУЧШЕЕ РЕШЕНИЕ</u> - для вашего бизнеса\n\nВажно, вы не оставили свой номер телефона, если у вас не указан User Name в телеграм, я не смогу с вами никак связаться, поэтому рекомендую, если после того как оставили заявку, я не связался с вами в течении 3-х часов, написать мне самому в личные сообщения <a href = "https://t.me/danya_grebnev">Написать</a></b>'
    await message.answer_photo(photo=main_photo, caption=text, reply_markup=kb.main)
    
    message_id_bot = id_messages[0]
    message_id_user = id_messages[1]
    message_id_user2 = message.message_id
    try:
        await message.bot.delete_messages(chat_id=user_id, message_ids=[message_id_bot, message_id_user, message_id_user2])
    except:
        pass
    id_messages.clear()
        
# about_me
@rt.callback_query(F.data == 'about_me')
async def about_me(callback: CallbackQuery):
    # Путь к новой фотографии
    photo_about_me = 'AgACAgIAAxkBAAMaZhKFNjaaZdTNmRBhF643p0vmXfoAAu7YMRtFFpFIryX6b5CyL4cBAAMCAAN5AAM0BA'
    
    text = 'Меня зовут Даниил\nЯ являюсь опытным Python разработчиком и смогу сделать качественное решение для вашего бизнеса, с помощью автоматизации.'
    media = InputMediaPhoto(media=photo_about_me, caption=text)
    
    await callback.message.edit_media(media=media, reply_markup=kb.about_me)
    
# portfolio 
@rt.callback_query(F.data == 'portfolio')
async def portfolio(callback: CallbackQuery):
    photo_portfolio = 'AgACAgIAAxkBAAMcZhKFRwl9Hjkmg4zZ892BPUCzliwAAvDYMRtFFpFIh1TSmvEX1G8BAAMCAAN5AAM0BA'
    
    text = 'Несколько моих работ'
    media = InputMediaPhoto(media=photo_portfolio, caption=text)
    
    await callback.message.edit_media(media=media, reply_markup=kb.portfolio)

# call_me
@rt.callback_query(F.data == 'call_me')
async def call_me(callback: CallbackQuery):
    user_id = callback.from_user.id
    user_info = await get_user_info_by_id(user_id)
    
    text_admin = f'Новая заявка от пользователя @{user_info["user_name"]}\nИмя {user_info["first_name"]}\nФамилия {user_info["last_name"]}\nНомер телефона {user_info["phone_number"]}'
    for admin in admins:
        await callback.bot.send_message(admin, text_admin)
    
    text = 'Спасибо за заявку, я скоро свяжусь с вами!'
    await callback.answer(text, show_alert=True)
    
# FAQ
@rt.callback_query(F.data == 'FAQ')
async def FAQ(callback: CallbackQuery):
    photo_FAQ = 'AgACAgIAAxkBAAMeZhKFXCISaleGWMwZprim0GjdQ2EAAvLYMRtFFpFIPKXgbRy-QmEBAAMCAAN5AAM0BA'
    
    text = 'Часто задаваемые вопросы'
    media = InputMediaPhoto(media=photo_FAQ, caption=text)
    
    await callback.message.edit_media(media=media, reply_markup=kb.faq)

# guarantee
@rt.callback_query(F.data == 'guarantee')
async def guarantee(callback: CallbackQuery):
    text = 'Я предоставляю гарантию на работу бота в течение 90 дней с даты покупки. Если бот не работает корректно, я гарантирую, что исправлю все проблемы бесплатно.'
    await callback.message.edit_caption(caption = text, reply_markup = kb.back_faq)

# support
@rt.callback_query(F.data == 'support')
async def support(callback: CallbackQuery):
    text = 'Я предоставляю бесплатную поддержку клиентам в течение 30 дней с даты покупки. Если клиенты столкнутся с проблемами, они могут обратиться ко мне для получения помощи.'
    await callback.message.edit_caption(caption = text, reply_markup = kb.back_faq)

# updates
@rt.callback_query(F.data == 'updates')
async def updates(callback: CallbackQuery):
    text = 'Я обновляю ботов регулярно, но клиенты могут заказать отдельное обновление за дополнительную плату'
    await callback.message.edit_caption(caption = text, reply_markup = kb.back_faq)

# safe 
@rt.callback_query(F.data == 'safe')
async def safe(callback: CallbackQuery):
    await callback.message.edit_caption(caption = 'Я гарантирую, что бот безопасен и защищен от вторжений. Я использую современные методы защиты данных, чтобы обеспечить безопасность клиентов.', reply_markup = kb.back_faq)

# data  
@rt.callback_query(F.data == 'data')
async def data(callback: CallbackQuery):
    text = 'Я гарантирую, что данные клиентов защищены и не будут переданы третьим сторонам. Я использую современные методы защиты данных, чтобы обеспечить безопасность клиентов.'
    await callback.message.edit_caption(caption = text, reply_markup = kb.back_faq)
    

# Back Button
@rt.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    main_photo = 'AgACAgIAAxkBAAMYZhKE95Vex57QUk5SHVMZwfFalPoAAu3YMRtFFpFIzEHk3ScTXHUBAAMCAAN5AAM0BA'
    
    first_name = callback.from_user.first_name
    text = f'<b>Доброго времени суток <i>{first_name}</i>\n\nРад вас видеть в своем телеграм-боте\nВы можете ознакомиться с частичкой моих работ и заказать\n\n<u>ЛУЧШЕЕ РЕШЕНИЕ</u> - для вашего бизнеса\n\nОставьте заявку, и я свяжусь с вами в самые короткие сроки!</b>'
    media = InputMediaPhoto(media=main_photo, caption=text)
    await callback.message.edit_media(media=media, reply_markup=kb.main)
    
# Back FAQ
@rt.callback_query(F.data == 'back_faq')
async def back_faq(callback: CallbackQuery):
    
    text = 'Часто задаваемые вопросы'
    await callback.message.edit_caption(caption=text, reply_markup=kb.faq)
