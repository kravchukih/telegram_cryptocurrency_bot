import requests
from bs4 import BeautifulSoup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot_token='1720933334:AAFUwxDiEJsqSERzKZsd84-t3xJgDPQ63dY'
chatID='537296452'


BITCOIN_UAH= 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D1%96%D1%82%D0%BA%D0%BE%D0%B9%D0%BD%D0%B0+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&sxsrf=ALeKk03hEE3QaaEm6RRXjJkpWqI1WKf9Rw%3A1626955311420&ei=L175YMaDGbHjkgWByragCQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D1%96%D1%82%D0%BA%D0%BE%D0%B9%D0%BD%D0%B0+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEAoQywEyAggAOgcIABBHELADOgQIABAKOgcIABDJAxAKOgUIABDJA0oECEEYAFCyC1i2GGDnGWgAcAN4AIABugKIAZQTkgEFMi05LjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwiG15vr0PbxAhWxsaQKHQGlDZQQ4dUDCA4&uact=5'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

full_page= requests.get(BITCOIN_UAH,headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert=soup.findAll("span", {"class":'DFlfde', "class":'SwHCTb',"data-precision":2})


bot=Bot(token=bot_token)
dp=Dispatcher(bot)

@dp.message_handler(commands=['Start'])

async def start_command(message: types.Message):
    await message.reply("Курс 1 Bitcoin складає "+ convert[0].text+" гривень")

if __name__=="__main__":
    executor.start_polling(dp)

