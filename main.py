import telebot
from telebot import types
from inf import Info
from mange import SQL
bot = telebot.TeleBot('5573494140:AAHWaUd_Oe8GI1SqSoqaRzf-qRUWy5yVlOM')
dt_user = [0]
chat_id = 0
user_id = 0
i = 0


def st(message):
    st_inmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    da_but = types.KeyboardButton('📝 Опрос')
    net_but = types.KeyboardButton('Парсинг Rаспи')
    st_inmarkup.row(da_but)
    st_inmarkup.row(net_but)
    bot.send_message(message.chat.id, 'Приветствую,вот мой функционал ⤵', reply_markup=st_inmarkup)


@bot.message_handler(commands=["start"])
def start(message):
    start_inmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vh_but = types.KeyboardButton('Войти')
    reg_but = types.KeyboardButton('Зарегистрироваться')
    start_inmarkup.row(vh_but)
    start_inmarkup.row(reg_but)
    bot.send_message(message.chat.id, 'Приветствую, вас в онлайн опроснике', reply_markup=start_inmarkup)


def user(message):
    global i, dt_user
    if i == 0:
        dt_user.append(int(message.text))
        i += 1
        ms1 = bot.send_message(message.chat.id, 'Введите почту')
        bot.register_next_step_handler(ms1, user)
    elif i == 1:
        dt_user.append(message.text)
        i = 0
        bot.send_message(message.chat.id, 'Регистрация прошла успешно')
        SQL.add_user(user_id, dt_user[1], dt_user[2])
        dt_user = []
        st(message)


def check(message):
    global dt_user
    if len(SQL.sel_user(user_id, message.text)) > 0:
        dt_user.append(SQL.sel_user(user_id, message.text))
        st(message)
    else:
        bot.send_message(message.chat.id, 'Ошибка такого пользователя не найдено, зарегестрируйтесь или'
                                          ' проверьте введенные данные на ошибки')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global user_id
    global chat_id
    if message.text == '📝 Опрос':
        Info.vi(bot, chat_id, user_id)
    elif message.text == 'Войти':
        chat_id = message.chat.id
        user_id = message.from_user.id
        ms = bot.send_message(message.chat.id, 'Введите номер телефона')
        bot.register_next_step_handler(ms, check)
    elif message.text == 'Зарегистрироваться':
        chat_id = message.chat.id
        user_id = message.from_user.id
        ms = bot.send_message(message.chat.id, 'Введите немер телефона')
        bot.register_next_step_handler(ms, user)
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
