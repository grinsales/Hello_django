# 5242487633:AAHOQopDjLifAB-oVddTHC7iF70t9T1NTHI
#@babydibybot
import telebot
from telebot import types

bot=telebot.TeleBot('5242487633:AAHOQopDjLifAB-oVddTHC7iF70t9T1NTHI')
#Теперь объявим метод для получения текстовых сообщений:

name = ''

surname = ''

age = 0
@bot.message_handler(content_types=['text'])

def start(message):

    if message.text == '/reg':

        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name

    else:

        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message):
    global name
    name=message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age=int(message.txt)
        except Exception:

            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');

    keyboard=types.InlineKeyboardMarkup()
    key_yes=types.InlineKeyboardButton(text='LA',callback_data='yes')
    keyboard.add(key_yes)
    keyboard=types.InlineKeyboardButton(text='Nea', callback_data='no')
    keyboard.add(key_no)
    question ='Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data=="yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        print("povtorite")


if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
       bot.polling(none_stop=True)
    except Exception as e:
        print(e)  # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)

#Теперь наш бот будет постоянно спрашивать у сервера Телеграмма «Мне кто-нибудь написал?», и если мы напишем нашему боту, то Телеграмм передаст ему наше сообщение. Сохраняем весь файл, и пишем в консоли:


#№def get_text_messages(message):
 #   if message.text == "Привет" or "привет":
  #      bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
   ##    bot.send_message(message.from_user.id, "Напиши привет")
    #else:
     #   bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")