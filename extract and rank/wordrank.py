import os
import pickle
data = pickle.load(open(r'movies.dat', 'r'))
print "enter 'y' if you want the word in pictionary and 'n' if you don't"
for i in range(len(data[0])):
    os.system('cls')
    print data[0][i]
    choice = raw_input(':')
    while choice != 'y' or choice != 'n':
        choice = raw_input(':')
    if choice == 'y':
        data[4][i] = 1
    else:
        data[4][i] = 0
pickle.dump(data, open(r'temp.dat', 'r'))
os.remove(r'movies.dat')
os.rename(r'temp.dat', r'movies.dat')
