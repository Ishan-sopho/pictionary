import pickle
from random import randint

def moviesrandom():
    list = pickle.load(open(r'movies.dat', 'r'))
    easy = len(list[0]) - 1 # pickle.load(list[1])
    #medium = pickle.load(list[2])
    #hard = pickle.load(list[3])
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield [list[0][randint(0,easy)],"movies"]
            continue
        elif flag < 13:
            yield [list[0][randint(0,easy)],"movies"]
            continue
        else:
            yield [list[0][randint(0,easy)],"movies"]
            continue

def musicrandom():
    list = pickle.load(open(r'songs.dat', 'r'))
    easy = len(list[0]) - 1 # pickle.load(list[1])
    #medium = pickle.load(list[2])
    #hard = pickle.load(list[3])
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield [list[0][randint(0,easy)],"music"]
            continue
        elif flag < 13:
            yield [list[0][randint(0,easy)],"music"]
            continue
        else:
            yield [list[0][randint(0,easy)],"music"]
            continue

def tvseriesrandom():
    list = pickle.load(open(r'tvseries.dat', 'r'))
    easy = len(list[0]) - 1
    #medium = pickle.load(list[2])
    #hard = pickle.load(list[3])
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield list[0][randint(0,easy)],"t.v. series"
            continue
        elif flag < 13:
            yield list[0][randint(0,easy)],"t.v. series"
            continue
        else:
            yield list[0][randint(0,easy)],"t.v. series"
            continue

def bitsianrandom():
    list = pickle.load(open(r'bitsian.dat', 'r'))
    easy = len(list[0]) - 1
    #medium = pickle.load(list[2])
    #hard = pickle.load(list[3])
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield list[0][randint(0,easy)],"bitsian lingo"
            continue
        elif flag < 13:
            yield list[0][randint(0,easy)],"bitsian lingo"
            continue
        else:
            yield list[0][randint(0,easy)],"bitsian lingo"
            continue

def allrandom():
    flag = randint(1,4)
    if flag==1:
        return moviesrand.next()
    elif flag==2:
        return musicrand.next()
    elif flag==3:
        return tvseriesrand.next()
    else:
        return bitsianrand.next()
moviesrand=moviesrandom()
musicrand=musicrandom()
tvseriesrand=tvseriesrandom()
bitsianrand=bitsianrandom()
def word_generator(mode=0):
     if mode == 0:
          return allrandom()
     elif mode == 1:
          return moviesrand.next()
     elif mode == 2:
          return musicrand.next()
     elif mode == 3:
          return tvseriesrand.next()
     elif mode == 4:
          return bitsianrand.next()