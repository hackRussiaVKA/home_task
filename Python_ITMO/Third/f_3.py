
# Области видимости

COUNT = 0 #в глобальной области

def func():
    global COUNT #взять из глобальной области для изменения
    #в локальной области
    loc_prm = 12 + COUNT
    COUNT = 100 #Всегда создание локальной переменной

def sum(*args):
    i = 0
    for a in args:
        i += a
    return (i)

print (sum(1,2,3))