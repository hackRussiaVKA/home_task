#coding: utf-8

print('hello world!!!')

# int    - целое число              => 5    => -5
# float  - дробное число            => 1.5  => -1.5
# bool   - логический тип данных    => True, False
# str    - строки                   => 'S'  => 's'
# tuple  - кортеж                   => (1, True, 'SS' )  -> неизменяемый тип хранения данных
# list   - список                   => [1, True, 'SS' ]  -> изменяемый тип
# dict   - словарь                  => {}
# set    - множество                => set {}            -> значения не дублируются, можно только проверять есть ли элемент в множестве или нет
# None   - пусто                    => None

lst = [1,2,3]

product = {
    'name' : 'PC',
    'price': 15000,
    'is_work' : False
}
print(lst[1], product['name'])