#coding: utf-8

s = input('2 + 1 = ')                                   #операторы сравнения : <
                                                        #                      >
                                                        #                      >=
                                                        #                      <=
                                                        #                      ==
                                                        #                      !=

i = int(s)

print(type(s),type(i))

a = 1
b = 2
#Условия:
if a > b:
    print('a > b')
elif a == b:
    print('a = b')
else:
    print('a < b')