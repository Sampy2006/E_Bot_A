import speech_recognition as sr
import pyttsx3
import telebot
import requests
import subprocess
from gtts import gTTS
from telebot import types
import os
import pyglet
from telebot import types

# создание переменных для работы
token = '5731619416:AAFvoGx7ESHFCArTUFafoIGIZ4eld5ed8Jg'
# создание служебных переменных
bot = telebot.TeleBot(token)
r = sr.Recognizer()
engine = pyttsx3.init()


# самый начальный экран с кнопками
@bot.message_handler(commands=['start'])
def sending_welcome_message(message):
    if message.from_user.id == 706901738 or 1350128290:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        murkup = types.InlineKeyboardMarkup(row_width=1, )
        btn1 = types.KeyboardButton("/help")
        btn2 = types.KeyboardButton("/start")
        btn3 = types.KeyboardButton('/Террористы')
        btn4 = types.KeyboardButton('/Пожар')
        markup.add(btn2, btn1, btn3, btn4)
    bot.send_message(message.chat.id,
                     text='Здравствуйте!\nЭто система управления голосвоыми оповещениями\nПодробнее : /help',
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def sending_welcome_message(message):
    bot.send_message(message.chat.id,
                     text='Для отправки голосового оповещение, запишите и отправьте голосовое сообщение или введите текст вручную.')


@bot.message_handler(commands=['Террористы'])
def sending_welcome_message(message):
    music = pyglet.resource.media('terror.mp3')
    music.play()


@bot.message_handler(commands=['Пожар'])
def sending_welcome_message(message):
    music = pyglet.resource.media('fire.mp3')
    music.play()


# создание кнопок выбора языка
@bot.message_handler(content_types=['text'])
def func(message):
    if message.from_user.id == 706901738 or 1350128290:
        text = message.text
        audio = gTTS(text=text, lang='ru', slow=False)
        audio.save('anvoice.mp3')
        music = pyglet.resource.media('anvoice.mp3')
        music.play()
        os.remove('anvoice.mp3')
        # os.system(r'D:\\Acoudiment\anvoice.mp3')
    else:
        bot.send_message(message.chat.id, "you are not a admin")


# # создание самой конструкции бота-переводчика
@bot.message_handler(content_types=['voice'])
def repeat_all_message(message):
    if message.from_user.id == 706901738 or 1350128290:
        # получение голосового сообщение и информации из него
        file_info = bot.get_file(message.voice.file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
        # создание файла с информацией из голосового сообщения
        with open(r"voice.oga", 'wb') as f:
            f.write(file.content)
        # os.system(r"D:\task6\voice.oga")
        music = pyglet.resource.media('voice.oga')
        music.play()
        os.remove('voice.oga')


    else:
        bot.send_message(message.chat.id, "you are not a admin")


if __name__ == '__main__':
    bot.polling(none_stop=True)
    pyglet.app.run()
