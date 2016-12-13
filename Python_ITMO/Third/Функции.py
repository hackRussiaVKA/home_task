
# название функции
def func():
    print('Hello World from func!')
#запуск функции
#func() пустые скобки -  всегда запуск!!!

import datetime

f = open('log.txt','w')

def log_time():
    now = datetime.datetime.now()
    print(now)
    f.write(str(now)+'\n')

log_time()
