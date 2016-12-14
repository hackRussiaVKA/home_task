#1. Написать функцию, которая (без аргументов) принимает на вход "имя", "фамилию", "возраст" через input
#2. Запускаем прогу, в цикле работает эта функция
#3. при закрытии программы, сохраняем список пользователей по порядку (мб контекстный менеджер?)
#4.при очередном запуске программы читаем список из файла, далее снова п.2

#Добавлять, не перезаписывать !!!
#5*.Логировать каждый запуск программы отдельной функцией log (в лог.txt) (время запуска)

import datetime
import os.path

def log():
    time =  datetime.datetime.now()
    return(time)

def add_user(*kwargs):
    Name = input ('Введите Имя :')
    Surname = input ('Введите Фамилию :')
    Age = input ('Введите возраст :')
    User = [Name, Surname, Age]
    t = log()
    with open ('log.txt', 'a') as l:
        l.write('Программа запущена :' + str(t) + '\n')
    return (User)

def delete_user():
    f = open('users.txt','r')
    f = f.replace()
    #Users_new = []
    Users_new = f.replace(isr_del)
    usr_del = input('Введите имя и фамилию пользователя, которого хотите удалить :')
    return(Users_new)

x = ''

if os.path.exists('users.txt') is True:
    n_f = open('users.txt','r')
    users = n_f.read()
    print(users)
    while x != 'нет' :
        with open('users.txt', 'a') as f:
            User = add_user()
            f.write(str(User) + '\n')
        x = input('хотите добавить еще одного пользователя ?(да / нет)')
    y = input('Хотите удалить пользователей ?(да / нет)')
    if y == 'да':
        with open('users.txt', 'a') as f:
            User = delete_user()
            f.writelines(str(User))
    else:
        pass
else:
    while x != 'нет' :
        with open('users.txt', 'a') as f:
            User = add_user()
            f.write(str(User) + '\n')
        x = input('хотите добавить еще одного пользователя ?(да / нет)')