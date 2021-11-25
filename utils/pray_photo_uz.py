import urllib.request
import requests
from aiogram.types import InputFile
from PIL import Image, ImageDraw,ImageFont
import io

sanserif= 'https://github.com/ProgrammingFonts/ProgrammingFonts/raw/master/Droid-Sans-Mono/droid-sans-mono-1.00/Droid%20Sans%20Mono.ttf'
def pray_photo(city):
    r = requests.get(sanserif, allow_redirects=True)
    font30 = ImageFont.truetype(io.BytesIO(r.content), size=30)
    font50 = ImageFont.truetype(io.BytesIO(r.content), size=50)
    font40 = ImageFont.truetype(io.BytesIO(r.content), size=40)
    font20 = ImageFont.truetype(io.BytesIO(r.content), size=20)


    img = Image.new('RGB', (600, 400), color = 'red')
    urllib.request.urlretrieve('https://i.ibb.co/4VsHjqJ/Namozvaqt.jpg',"namoz-uz.png")
    img = Image.open('namoz-uz.png')
    draw = ImageDraw.Draw(img)
    url=f'http://api.pray.zone/v2/times/today.json?city={city}&juristic=1&school=12'
    response=requests.get(url)
    data=response.json()
    hijri=str(data['results']['datetime'][0]['date']['hijri'])
    georgian=str(data['results']['datetime'][0]['date']['gregorian'])
    Tong=str(data['results']['datetime'][0]['times']['Imsak'])
    Quyosh=str(data['results']['datetime'][0]['times']['Sunrise'])
    Bomdod= str(data['results']['datetime'][0]['times']['Fajr'])
    Peshin= str(data['results']['datetime'][0]['times']['Dhuhr'])
    Asr=    str(data['results']['datetime'][0]['times']['Asr'])
    Shom=   str(data['results']['datetime'][0]['times']['Maghrib'])
    Xufton= str(data['results']['datetime'][0]['times']['Isha'])

    hijriy_oylar={ '01':'Muharram',
'02': 'Safar','03': 'Rabiul avval', '04':'Rabiul soniy', '05':'Jumodul avval',
'06': 'Jumo-dul oxir','07': 'Rajab','08':'Shaʼbon','09': 'Ramazon',
'10': 'Shavval','11': 'Zulqaʼda','12':' Zulhijja'}

    oylar={ '01':'Yanvar',
'02': 'Fevral','03': 'Mart', '04':'Aprel', '05':'May',
'06': 'Iyun','07': 'Iyul','08':'Avgust','09': 'Sentyabr',
'10': 'Oktyabr','11': 'Noyabr','12':' Dekabr'}

    bu_oy=hijriy_oylar[(str(hijri[5:7]))]
    oy=oylar[(str(georgian[5:7]))]
    draw.text((250, 60),f"{int(hijri[-2:])}",(255,255,255),font=font50)
    draw.text((810, 60),f"{int(georgian[-2:])}",(255,255,255),font=font50)
    draw.text((500,120),f"{city}",(255,255,255),font=font40)
    draw.text((190, 140),f"{bu_oy} / {hijri[0:4]}",(255,255,255),font=font20)
    draw.text((780, 140),f"{oy} / {georgian[0:4]}",(255,255,255),font=font20)
    draw.text((285, 310),Bomdod,(4,58,70),font=font30)
    draw.text((595, 310),Peshin,(4,58,70),font=font30)
    draw.text((885, 310),Asr,(4,58,70),font=font30)
    draw.text((450, 480),Shom,(4,58,70),font=font30)
    draw.text((730, 480),Xufton,(4,58,70),font=font30)
    img.save('j.jpg')
    photo_file=InputFile(path_or_bytesio="j.jpg")
    return photo_file
