import telebot
from telebot import types
from inf import Info
from mail import send_mail

bot = telebot.TeleBot('5573494140:AAHWaUd_Oe8GI1SqSoqaRzf-qRUWy5yVlOM')
chat_id = 0


@bot.message_handler(commands=["start"])
def start(message):
    start_inmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    da_but = types.KeyboardButton('📝 Опрос')
    net_but = types.KeyboardButton('Парсинг Rаспи')
    start_inmarkup.row(da_but)
    start_inmarkup.row(net_but)
    bot.send_message(message.chat.id, 'Приветствую,вот мой функционал ⤵', reply_markup=start_inmarkup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global chat_id
    if 'mail' in message.text:
        bot.send_message(message.chat.id, 'Результаты отправлены на указанную почту')
        send_mail(message.text)
    elif message.text == '📝 Опрос':
        chat_id = message.chat.id
        Info.vi(bot, chat_id)
    else:
        bot.send_message(message.chat.id, 'Я пока не знаю таких команд')


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == '1':
        Info.proverka(1, call.message.id, bot, chat_id)
    elif call.data == '2':
        Info.proverka(2, call.message.id, bot, chat_id)
    elif call.data == '3':
        Info.proverka(3, call.message.id, bot, chat_id)
    elif call.data == '4':
        Info.proverka(4, call.message.id, bot, chat_id)


bot.polling(none_stop=True, interval=0)
