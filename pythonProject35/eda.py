#5224730330:AAHZ5vuej2t6zhxE-87n6hgbtaMHajiG3-0
import telebot
from telebot import types

token='5224730330:AAHZ5vuej2t6zhxE-87n6hgbtaMHajiG3-0'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    walk_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='4')
    joke_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(walk_btn)
    keyboard.add(sleep_btn)
    keyboard.add(joke_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('17.jpeg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка воды",
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('18.jpeg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еда",
                reply_markup=keyboard)
            img.close()
        if call.data == "3":
            img = open('19.jpeg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка гулять",
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            bot.send_message(chat_id=call.message.chat.id, text="Спать пора! Уснул бычок, Лёг в коробку на бочок. Сонный мишка лег в кровать,Только слон не хочет спать.Головой качает слон,Он слонихе шлет поклон",reply_markup=keyboard)

        if call.data == "5":
            bot.send_message(
                chat_id=call.message.chat.id,
                text='https://веселун.рф/anekdoty/shutki',
                reply_markup=keyboard)

if __name__=="__main__":
    bot.polling(none_stop=True)
