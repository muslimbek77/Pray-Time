from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Andijon'),
            KeyboardButton(text='Margilan'),
            
        ],[KeyboardButton(text='Fergana'),
            KeyboardButton(text='Tashkent')],
            [KeyboardButton(text='Namangan'),
            KeyboardButton(text='Samarkand')],
    ],
    resize_keyboard=True
)