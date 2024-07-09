from aiogram.types import Message
from aiogram.filters import CommandStart
from loader import router
from aiogram import F
from keyboards.Inline_Keyboards.keyboards import  menu, ortga
from aiogram.types import CallbackQuery
from request_api import weather


@router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer_sticker('CAACAgIAAxkBAAID5mXZuHK0vG10IaptGi101X_oTKo4AAIiAQACpkRICxH1ucyPFfRmNAQ')
    await msg.answer(f"Assalomu aleykum {msg.from_user.full_name}!😊")
    await msg.answer(f"Shahringiz ob-havosini tanlang:👇🏻", reply_markup=menu)


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