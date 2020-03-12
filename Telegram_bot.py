#Напишем телеграм бота
import telebot

#Импортируем погоду
import pyowm
owm = pyowm.OWM('27d057065c7fb12eb132fe31b42c2195', language = "ru")
observation = owm.weather_at_place("MINSK")
w = observation.get_weather()

#Вытягиваем температуру и скорость ветра
temp = w.get_temperature('celsius') ["temp"]
speed = w.get_wind() ["speed"]

#заходим в телегу и получаем токен нашего телебота
# определяем переменную с токеном телебота
bot = telebot.TeleBot('932525918:AAGDj4LRNCBi0hFo59vclpgYdavF4_vuxEU')

#определяем тип сообщения при котором наш телебот будет реагировать

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.send_message(message.chat.id,"Доброго времени суток Сергей Николаевич!" + " \nТекущая температура в Минске составляет: " + str(temp)+ " C0." + " \nСкорость ветра составляет: " + str(speed) + " м/с")
bot.polling(none_stop = True)













