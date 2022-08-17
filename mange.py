import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="telepars")
mycursor = mydb.cursor()


def insert():
    nom_questions = int(input('Введите номер вопроса: '))
    questions = input('Введите вопрос: ')
    var1 = input('Введите вариант A: ')
    var2 = input('Введите вариант B: ')
    var3 = input('Введите вариант C: ')
    var4 = input('Введите вариант D: ')
    arr = [(nom_questions, var1,), (nom_questions, var2,), (nom_questions, var3,), (nom_questions, var4,)]
    answer = input('Введите ответ(ответ должен повторять вариант: ')
    if answer == 'a':
        answer = var1
    elif answer == 'b':
        answer = var2
    elif answer == 'c':
        answer = var3
    elif answer == 'd':
        answer = var4
    else:
        return print('Вы выбрали неправильный вариант')
    sql = 'INSERT INTO `вопросы`(`nom_questions`, `question`) VALUES (%s, %s)'
    values = (nom_questions, questions)
    mycursor.execute(sql, values)
    mydb.commit()
    mycursor.executemany('INSERT INTO `варианты`(`nom_questions`, `variant`) VALUES (%s, %s)', arr)
    mydb.commit()
    sql3 = 'INSERT INTO `ответы`(`nom_questions`, `answer`) VALUES (%s, %s)'
    values = (nom_questions, answer)
    mycursor.execute(sql3, values)
    mydb.commit()
    return print('Все добавленно в БД без ошибок')


def select(con):
    if con == 1:
        sql = 'SELECT `question` FROM `вопросы`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    elif con == 2:
        sql = 'SELECT `variant` FROM `варианты`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    elif con == 3:
        sql = 'SELECT `answer` FROM `ответы`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
