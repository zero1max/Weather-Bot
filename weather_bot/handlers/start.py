from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from loader import router, db, bot
from aiogram import F
from keyboards.Inline_Keyboards.keyboards import  menu, ortga
from aiogram.types import CallbackQuery
from request_api import weather


@router.message(CommandStart())
async def start_handler(msg: Message):
    full_name = msg.from_user.full_name
    surname = msg.from_user.last_name or ''
    user_id = msg.from_user.id

    db.create_table()
    db.add_user(user_id, full_name, surname)

    await msg.answer_sticker('CAACAgIAAxkBAAID5mXZuHK0vG10IaptGi101X_oTKo4AAIiAQACpkRICxH1ucyPFfRmNAQ')
    await msg.answer(f"Assalomu aleykum {msg.from_user.full_name}!😊")
    await check_subscription(msg)

async def check_subscription(message: Message):
    channel_ids = ["@first_channel", "@second_channel"]  # Kanal username'lari yoki ID'lari
    channel_urls = {
        "@zero1max_channel": "https://t.me/first_channel",
        "@zeromaxs_movies": "https://t.me/second_channel"
    }
    user_id = message.from_user.id
    subscribed_channels = set()  # Obuna bo'lgan kanallar ro'yxati

    # Har bir kanalni tekshirib chiqamiz
    for channel_id in channel_ids:
        try:
            member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            if member.status != 'left':
                subscribed_channels.add(channel_id)  # Obuna bo'lgan kanallar ro'yxatiga qo'shamiz
        except Exception as e:
            print(f"Kanal tekshirishda xatolik: {channel_id} - {e}")

    # Obuna bo'lmagan kanallarni aniqlaymiz
    not_subscribed_channels = set(channel_ids) - subscribed_channels

    # `inline_keyboard` ro'yxatini yaratamiz
    inline_keyboard = []

    for channel_id in not_subscribed_channels:
        inline_keyboard.append([InlineKeyboardButton(text=f"{channel_id[1:]}", url=channel_urls[channel_id])])

    markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    if not_subscribed_channels:
        await message.answer(
            "Kanallarga obuna bo'lishingizni so'raymiz.\nObuna bo'lgandan so'ng /start buyrug'ini yuboring!\nIltimos, quyidagi kanallarga obuna bo'ling:👇🏻",
            reply_markup=markup
        )
    else:
        await message.answer(f"Shahringiz ob-havosini tanlang:👇🏻", reply_markup=menu)


@router.callback_query(F.data=='tosh')
async def weath(call: CallbackQuery):
    response_message = weather("Toshkent")  
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga) 

@router.callback_query(F.data=='tosh_vil')
async def weath(call: CallbackQuery):
    response_message = weather('Toshkent viloyati')
    await call.message.delete()   
    await call.message.answer(response_message, reply_markup=ortga)


@router.callback_query(F.data=='far')
async def weath(call: CallbackQuery):
    response_message = weather("Farg'ona")
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data=='nam')
async def weath(call: CallbackQuery):
    response_message = weather('Namangan')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data=='and')
async def weath(call: CallbackQuery):
    response_message = weather('Andijon')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data=='xor')
async def weath(call: CallbackQuery):
    response_message = weather('Khiva')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)
    
@router.callback_query(F.data=='jiz')
async def weath(call: CallbackQuery):
    response_message = weather('Jizzax')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data=='nav')
async def weath(call: CallbackQuery):
    response_message = weather('Navoiy')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data=='samar')
async def weath(call: CallbackQuery):
    response_message = weather('Samarqand')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data=='sir')
async def weath(call: CallbackQuery):
    response_message = weather('Sirdaryo')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)


@router.callback_query(F.data=='sur')
async def weath(call: CallbackQuery):
    response_message = weather('Termiz')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data=='qash')
async def weath(call: CallbackQuery):
    response_message = weather('Qashqadaryo')
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

#
@router.callback_query(F.data=='qoraqalpoq')
async def weath(call: CallbackQuery):
    response_message = weather("Nukus")
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data == 'back')
async def back1(call: CallbackQuery):
    await call.message.delete()    
    await call.message.answer(f"Shahringiz ob-havosini tanlang:👇🏻", reply_markup=menu)

@router.message()
async def nothing(msg: Message):
    await msg.answer("Chunmadim??")