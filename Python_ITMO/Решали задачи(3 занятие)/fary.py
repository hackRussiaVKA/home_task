print("Cколько имеется тарелок?")
trl = input("Кол-во :")

print("Cколько имеется средства?")
srv = input("Кол-во :")

int_trl = int(trl)
fl_srv = float(srv)

while int_trl and fl_srv >= 0.5:
    int_trl -= 1
    fl_srv -= 0.5
    print('Тарелок осталось', int_trl)
    print('Средства осталось', fl_srv)

