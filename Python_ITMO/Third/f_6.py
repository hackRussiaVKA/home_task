

def fuct(a):
    count = 1

    for i in range(1, a+1):         # range - от одного до (в данном случае) 7 НЕ ВКЛЮЧАЯ!!!
        count *= i

    return count

print(fuct(6))

#Рекурсия

def fact(a):
    if a == -3:                     #чтобы ограничить рекурсию
        return 1
    return fact(a-1)

print(fact(6))

#Есть пределы рекурсии ~ 1000 вхождений

def func1(*args, **kwargs):  #kwargs неограниченное количество именованных аргументов
    #совет для использования
    if key in kwargs:
        fdfdfdf

#при чтении из файла, f.strip() обрезает все слева и справа (символ переноса, например)