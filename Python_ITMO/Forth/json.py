# json (java script object notation)
"""
import json

lst = [1, 2, 3, 'olesya', {17 : 12}]

# запись в джейсон
with open ('lst_json', 'w') as f:
    json.dump(lst,f)

# чтение из джейсона
with open('lst_json', 'r') as f:
    lst = json.load(f)

"""

import json

FILE_name = 'File'

def write_Train(*kwargs):
    lok = []
    name = str(input('Vvedite nazvanie poezda'))
    pwr = str(input('Vvedite moshnost poezda'))
    size = str(input('Vvedite gabarity poezda'))
    lok.append((name, pwr, size))
    with open (FILE_name, 'wb') as f:
        json.dump(lok, f)

write_Train()
write_Train()
write_Train()

def read_Train():
    with open(FILE_name, 'rb') as f:
        loc_2 = json.load(f)
    print(loc_2)

read_Train()