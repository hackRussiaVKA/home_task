
# pickle
import pickle

lst = [1, 2, 3, 'olesya', {17 : 12}]

FILENAME = 'lst_pickle'

with open('lst_pickle', 'wb') as f: # wb - write bytes чтобы записать байты, а не строки!!(особенности пикла)
    pickle.dump(lst, f)

f = open(FILENAME, 'rb')
lst_2 = pickle.load(f)

print(lst==lst_2)
