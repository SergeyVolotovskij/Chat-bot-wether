# Напишем телеграм бота
import telebot

# Импортируем модули для парсера
import requests
from bs4 import BeautifulSoup

# Импортируем погоду
import pyowm

owm=pyowm.OWM('27d057065c7fb12eb132fe31b42c2195', language="ru")
observation=owm.weather_at_place("MINSK")
w=observation.get_weather()

# Вытягиваем температуру и скорость ветра
temp=w.get_temperature('celsius')["temp"]
speed=w.get_wind()["speed"]

# Парсим курс BTC
def parcer_kurs():
    url="https://exchange.currency.com/ru/tokenizirovannaya-para-bitcoin-to-us-dollar"  # ресурс с которого будем черпать инфо
    source=requests.get(url)  # открываем данный ресурс
    main_txt=source.text  # забираем весь текст и записываем его в переменную
    # передаем страницу txt в модуль BeautifulSoup
    soup=BeautifulSoup(main_txt, 'lxml')
    table1=soup.find('body')  # вытянули всю таблицу
    st=table1.find('div', class_='instrument__banner--btns')  # вытянули нужное значение
    BTC=(st.text)  # получаем только текст значения
    a=[]
    a.append(BTC)
    BTC=float((a[0][8]) + (a[0][9]) + (a[0][10]) + (a[0][11]) + (a[0][12]) + (a[0][13]) + (a[0][14]) + (a[0][15]))
    return(BTC)

def parcer_covi():
    url="https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html"  # ресурс с которого будем черпать инфо
    source=requests.get(url)  # открываем данный ресурс
    main_txt=source.text  # забираем весь текст и записываем его в переменную
    # передаем страницу txt в модуль BeautifulSoup
    soup=BeautifulSoup(main_txt, 'lxml')
    table1=soup.find('body')  # вытянули всю таблицу
    st=table1.find('div', class_='flex-fix allow-shrink indicator-center-text responsive-text flex-vertical ember-view')  # вытянули нужное значение
    zaraj = st.text
    print(zaraj)

# заходим в телегу и получаем токен нашего телебота
# определяем переменную с токеном телебота
bot=telebot.TeleBot('932525918:AAGDj4LRNCBi0hFo59vclpgYdavF4_vuxEU')

# определяем тип сообщения при котором наш телебот будет реагировать
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    parcer_covi()
    bot.send_message(message.chat.id,
                     "Доброго времени суток Сергей Николаевич!" + "\nВ городе Минске сейчас: " + w.get_detailed_status() + "\nТекущая температура в Минске составляет: " + str(
                         temp) + " C0." + " \nСкорость ветра составляет: " + str(speed) + " м/с" + "\nBTC($) = " + str(parcer_kurs()))

bot.polling(none_stop=True)
