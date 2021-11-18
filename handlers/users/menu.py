from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.MenuKeyboard import menu
# from keyboards.default.pythonKeyboard import menuPython
import requests
from datetime import date
import json
from hijri_converter import convert
from loader import dp
from datetime import date, datetime
from utils.pray_photo_uz import pray_photo

my_date = str(date.today())

war = datetime.strptime(my_date, '%Y-%m-%d')
hijri_date = convert.Gregorian.fromdate(war).to_hijri()

def namoz_vakti(city):
    city=city
    url=f'http://api.pray.zone/v2/times/today.json?city={city}&school=2'
    response=requests.get(url)
    data=response.json()
    Tong=str(data['results']['datetime'][0]['times']['Imsak'])
    Quyosh=str(data['results']['datetime'][0]['times']['Sunrise'])
    Bomdod= str(data['results']['datetime'][0]['times']['Fajr'])
    Peshin= str(data['results']['datetime'][0]['times']['Dhuhr'])
    Asr=    str(data['results']['datetime'][0]['times']['Asr'])
    Shom=   str(data['results']['datetime'][0]['times']['Maghrib'])
    Xufton= str(data['results']['datetime'][0]['times']['Isha'])

    result=('☪️ Andijon namoz vaqtlari:\n'+
    '📆 gregorian:  '+str(my_date)+
    '\n📆 hijri:  '+str(hijri_date)+
    '\n➖➖➖➖➖➖➖➖\n'+
    '⏰  '+Tong+' | Tong\n'+
    '⏰  '+Quyosh+' | Quyosh\n'+
    '⏰  '+Bomdod+' | Bomdod\n'+
    '⏰  '+Peshin+' | Peshin\n'+
    '⏰  '+Asr+' | Asr\n'+
    '⏰  '+Shom+' | Shom\n'+
    '⏰  '+Xufton+' | Xufton\n'+'\n<a href="https://t.me/nvaqti_bot">Namoz vaqtlari ⏰</a>' )
    return result
    

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    
    await message.answer("Namoz vaqtlarini tanlang", reply_markup=menu)

@dp.message_handler(text='Andijon')
async def send_link(message: Message):



    await message.reply_photo(pray_photo('Andijan'),caption=namoz_vakti('Andijan'))


@dp.message_handler(text='Tashkent')
async def send_link(message: Message):



    await message.reply_photo(pray_photo('Tashkent'),caption=namoz_vakti('Tashkent'))


@dp.message_handler(text='Namangan')
async def send_link(message: Message):



    await message.reply_photo(pray_photo('Namangan'),caption=namoz_vakti('Namangan'))


@dp.message_handler(text='Fergana')
async def send_link(message: Message):



    await message.reply_photo(pray_photo('Fergana'),caption=namoz_vakti('Fergana'))


@dp.message_handler(text='Margilan')
async def send_link(message: Message):



    await message.reply_photo(pray_photo('Margilan'),caption=namoz_vakti('Margilan'))


@dp.message_handler(text='Samarkand')
async def send_link(message: Message):



    await message.reply_photo(pray_photo('Samarkand'),caption=namoz_vakti('Samarkand'))