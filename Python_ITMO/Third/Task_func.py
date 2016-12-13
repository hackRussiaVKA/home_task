# 30 столов, 30 стульев и 1 доска
# функция приниамет на вход название, кол-во и выводит на экран
kol_vo = 0
def furniture (element, count):
    global kol_vo
    kol_vo += count
    print(element, count, 'Всего элементов :', kol_vo)

furniture('стульев', 30)
furniture('столов', 30)
furniture(element='доска', count=1) #именнованные аргументы (слева от позиционных не может быть никаких других)