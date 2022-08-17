from telebot import types
from mange import select


class Info:
    questions = []
    for i in select(1):
        questions.append(i[0])

    variants = ['null', ]
    for i in select(2):
        variants.append(i[0])
    answers = []
    for i in select(3):
        answers.append(i[0])
    check = []
    counter = 1
    points = 0
    cin = 0

    @classmethod
    def count(cls):
        cls.counter += 1
        cls.cin += 4

    @classmethod
    def ap_chek(cls, chek):
        cls.check.append(chek)

    @classmethod
    def vopros(cls):
        vopros1_inmarkup = types.InlineKeyboardMarkup()
        variant1 = types.InlineKeyboardButton('А.' + cls.variants[cls.cin + 1], callback_data='1')
        variant2 = types.InlineKeyboardButton('B.' + cls.variants[cls.cin + 2], callback_data='2')
        variant3 = types.InlineKeyboardButton('C.' + cls.variants[cls.cin + 3], callback_data='3')
        variant4 = types.InlineKeyboardButton('D.' + cls.variants[cls.cin + 4], callback_data='4')
        vopros1_inmarkup.row(variant1, variant2)
        vopros1_inmarkup.row(variant3, variant4)
        return vopros1_inmarkup

    @classmethod
    def proverka(cls, nomer, message, bot, chat_id):
        if cls.answers[cls.counter-1] == cls.variants[cls.cin + nomer]:
            cls.ap_chek('da')
            cls.count()
            cls.vi(bot, chat_id)
            return bot.edit_message_text(chat_id=chat_id, message_id=message, text='Ваш ответ принят')
        else:
            cls.ap_chek('net')
            cls.count()
            cls.vi(bot, chat_id)
            return bot.edit_message_text(chat_id=chat_id, message_id=message, text='Ваш ответ принят')

    @classmethod
    def vi(cls, bot, chat_id):
        if cls.counter < len(cls.questions)+1:
            return bot.send_message(chat_id, f'Вопрос №{cls.counter}. {cls.questions[cls.counter-1]}',
                                    reply_markup=cls.vopros())
        else:
            cls.schet()
            return bot.send_message(chat_id, 'Вы прошли тест, пожалуйста введите свой mail чтоб мы могли '
                                             'отправить вам ваш результат')

    @classmethod
    def schet(cls):
        for i in cls.check:
            if i == 'da':
                cls.points += 1
