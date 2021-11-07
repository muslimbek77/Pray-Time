from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Andijon'),
            KeyboardButton(text='Toshkent'),
            
        ],[KeyboardButton(text='Fargona'),
            KeyboardButton(text='Namangan')],
    ],
    resize_keyboard=True
)