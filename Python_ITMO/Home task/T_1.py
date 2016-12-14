#coding: utf-8
# Написать программу:
# Условие:
#1. Задаем список студентов (Имя, Фамилия, Возраст)1
#2. Выводим на экран (Для начала) 1
#3. Считаем и выводим количество студентов у которых в сумме (Имя+Фамилия) > 15 символов 1
#4. Выводим всех девушек(имя) в обратном порядке(по алфавиту)
#5. Записать в файл в этом порядке
#6*. В конце файла добавить сумму (количество) всех глассных букв данного списка

Students = [
    ['Александр Канаев', 21],
    ['Александр Хвостионок', 20],
    ['Александр Усков', 22],
    ['Владислав Березин', 21],
    ['Иван Быжко', 22],
    ['Артем Борисенко', 20],
    ['Никита Панфилов', 23],
    ['Михаил Усачев', 19],
    ['Илья Парастаев', 24],
    ['Анастасия Ромашенкова', 24],
    ['Наталья Гамбеева', 22],
    ['Анна Голубятник', 20],
    ['Мария Денчик', 22],
    ['Анастасия Турубанова', 24],
    ['Нина Шестирублева', 23]
]

print('используется следующий список :')
for i, (name, age) in enumerate(Students):
    print(name, age)
sch_1 = 0
summa_1 = 0
for s, (name, age) in enumerate(Students):
    #print(name)
    for m in name:
        if m != ' ':
            sch_1 += 1
        else:
            pass
    if sch_1 > 15:
        summa_1 += 1
        sch_1 = 0
    else:
        sch_1 = 0
print('Студентов у которых в сумме ФИО больше 15 символов :', summa_1)
Gl_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
Devushki = []
for b, (name, age) in enumerate(Students):
    for v, n in enumerate(name):
        if name[v] == ' ':
            if name[0 : v] == 'Никита':
                pass
            elif name[0 : v] == 'Илья':
                pass
            elif name[v - 1] in Gl_letters:
                Devushki.append(name)
            else:
                pass
        else:
            pass
Devushki = sorted((Devushki))
kol_gl = 0
for D in Devushki:
    for n in D:
        if n in Gl_letters:
            kol_gl += 1
f = open('1.txt','w')
f.write(str(Devushki)+'\n'+str(kol_gl))
f.close()
