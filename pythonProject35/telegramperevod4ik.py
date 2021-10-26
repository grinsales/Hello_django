#5224730330:AAHZ5vuej2t6zhxE-87n6hgbtaMHajiG3-0
import telebot
from telebot import types
from translate import Translator

token='5137056622:AAGoGL0_DJSGRWF9M-M_M-GbfM3wHk-Bijo'
bot = telebot.TeleBot(token)
txt=" "
rus = ''
en = ''
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Хочу перевод' or message.text =='хочу перевод':
        bot.send_message(message.from_user.id, "Нужен перевод: русский(с русского на английский), английский (с английского на русский");
        bot.register_next_step_handler(message, get_type); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши "Хочу перевод"')

def get_type(message):
    global txt
    txt = message.text
    if txt == "русский" or txt == "Русский":
        bot.send_message(message.from_user.id, 'Напиши слово на русском языке')
        bot.register_next_step_handler(message, get_rus)
    if txt == "английский" or txt == "Английский":
        bot.send_message(message.from_user.id, 'Напиши слово на английском языке')
        bot.register_next_step_handler(message, get_en)

def get_rus(message):
    global rus
    rus = message.text
    translator = Translator(from_lang='Russian', to_lang='English')
    w = translator.translate(rus)
    bot.send_message(message.from_user.id, w)

def get_en(message):
    global en
    en = message.text
    translator = Translator(from_lang='English', to_lang='Russian')
    d = translator.translate(en)
    bot.send_message(message.from_user.id, d)

if __name__=="__main__":
    bot.polling(none_stop=True)
