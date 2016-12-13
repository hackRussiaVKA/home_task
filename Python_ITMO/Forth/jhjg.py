# фунция которая добавляет компании новый локомотив (мощность, габариты) и сохранить в pickle
# создать функцию, которая читает все тепловозы этой компании в список
import pickle

FILE_name = 'File'

def write_Train(*kwargs):
    lok = []
    name = str(input('Vvedite nazvanie poezda'))
    pwr = str(input('Vvedite moshnost poezda'))
    size = str(input('Vvedite gabarity poezda'))
    lok.append((name, pwr, size))
    with open (FILE_name, 'wb') as f:
        pickle.dump(lok, f)

write_Train()
write_Train()
write_Train()

def read_Train():
    with open(FILE_name, 'rb') as f:
        loc_2 = pickle.load(f)
    print(loc_2)

read_Train()