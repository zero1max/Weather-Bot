from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Correctly initializing InlineKeyboardMarkup with inline_keyboard parameter
menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Toshkent', callback_data='tosh'),InlineKeyboardButton(text='Toshkent Viloyati', callback_data='tosh_vil')],
    [InlineKeyboardButton(text="Farg'ona", callback_data='far'),InlineKeyboardButton(text='Namangan', callback_data='nam')],
    [InlineKeyboardButton(text="Andijon", callback_data='and'),InlineKeyboardButton(text='Xorazm', callback_data='xor')],
    [InlineKeyboardButton(text='Jizzax', callback_data='jiz'),InlineKeyboardButton(text='Navoiy', callback_data='nav')],
    [InlineKeyboardButton(text='Samarqand', callback_data='samar'),InlineKeyboardButton(text='Sirdaryo', callback_data='sir')],
    [InlineKeyboardButton(text='Surxondaryo', callback_data='sur'),InlineKeyboardButton(text='Qashqadaryo', callback_data='qash')],
    [InlineKeyboardButton(text="Qoraqalpog'iston", callback_data='qoraqalpoq')],
])

ortga = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ortga🔙', callback_data='back')]
])

