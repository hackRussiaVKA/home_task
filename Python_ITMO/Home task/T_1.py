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
#x = input('Хотите ввести своих студентов ?(да / нет)')
#if x == 'да':
#    kol_vo = int(input('Сколько студентов вы хотите ввести? (кол-во)'))
#    i=0
#    students_1 = []
#    while i < kol_vo:
#        Name = input('Введите Имя и Фамилию')
#        Age = int(input ('Введите возраст'))
#        students_cycle = [Name, Age]
#        i += 1
#        students_1.append(students_cycle)
#    print('Получился такой список :',students_1)
#    sch = 0
#    summa = 0
#    for s, (name,age) in enumerate(students_1):
#        for m in name:
#            if m != ' ':
#                sch += 1
#            else:
#                pass
#        if sch > 15:
#            summa += 1
#            sch = 0
#        else:
#            sch = 0
#    print('Студентов у которых в сумме ФИО больше 15 символов :',summa)
#    Gl_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
#    Devushki = []
#    for s, (name, age) in enumerate(students_1):
#        for v,n in enumerate(name):
#            if name[v] == ' ':
#                Name_gender = name[0:v]
#                print(Name_gender)
#                if name[v-1] in Gl_letters:
#                    Devushki.append(name)
#                else: pass
#            else: pass
#    Devushki = sorted((Devushki))
#    print(Devushki)
#    f = open('1.txt', 'w')
#    f.write(str(Devushki) + '\n')
#    f.close()
#
#else:
print('используется следующий список :')
for i, (name, age) in enumerate(Students):
    print(name, age)
sch_1 = 0
summa_1 = 0
for s, (name, age) in enumerate(Students):
    print(name)
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
for s, (name, age) in enumerate(Students):
    for v, n in enumerate(name):
        if name[v] == ' ':
            if name[v - 1] in Gl_letters:
                Devushki.append(name)
            else:
                pass
        else:
            pass
Devushki = sorted((Devushki))
print(Devushki)
f = open('1.txt','w')
f.write(str(Devushki)+'\n')
f.close()
