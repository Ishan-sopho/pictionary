import pickle
data = pickle.load(open('songs.dat', 'r'))
for i in range(len(data[0])):
    print data[0][i]