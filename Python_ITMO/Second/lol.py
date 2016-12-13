#coding: utf-8

lst = [
    ['Юля', 20],
    ['Степа',21],
    ['Артем',19]
]
i = 0
for i, (name, age) in enumerate(lst):               # распаковка!!! вместо нее можно item!! / (enumerate добавляет
    if i % 2 == 0:                                  #                                      порядковый номер к элементам)
        print('Имя :', name, 'Возраст :', age)      # тогда здесь был бы item[0] и item[1] вместо name и age

lst_1 = ['cccc', 'vv', 'a']                             # сортировка. Числа, буквы
lst_1 = sorted (lst_1,
               key=lambda b:len(b))                     # сортировка по длине строки (!)
print(lst_1)

lst_2 = [1, -17, 233, 10, 12]
lst_2 = lst_2[0 : 3 : 2]                                    # срез. Первые три элемента (c шагом 2)

print(lst_2)

# Генератор списка
names = ['Vasyan','Misha','Vera']

lst_3 = [ a for a in names ]                        # преобразование с циклом for

print(lst_3)

