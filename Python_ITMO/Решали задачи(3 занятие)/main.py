# coding: utf-8

year = input ('Введите год :')

year_int = int(year)

if (year_int % 4 == 0):
    if (year_int % 100 == 0):
        if (year_int % 400 == 0):
            print('Год високосный')
        else:
            print('Год не високосный')
    else:
        print('Год високосный')
else:
    print('год не високосный')


if True:
    a = 1
else:                       # => этажерка
    a = 2

# Тернарный оператор !!!
# <Истинная_часть> if <Условие> else <ложная_часть>

a = 1 if True else 2       # тру тема