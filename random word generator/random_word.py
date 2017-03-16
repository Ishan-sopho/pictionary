"""def word_generator():
    from random import randint
    easy=open(r'easynouns.txt','r')
    medium=open(r'mediumnouns.txt','r')
    hard=open(r'hardnouns.txt','r')
    rhard=open(r'reallyhardnouns.txt','r')
    noun=[]
    noun.append(easy.readlines())
    noun.append(medium.readlines())
    noun.append(hard.readlines())
    noun.append(rhard.readlines())
    word=0
    while True:
        n=randint(1,12)
        if n<=5:
            word=randint(0,len(noun[0]))
            yield noun[0][word]
            continue
        elif n<=9:
            word=randint(0,len(noun[1]))
            yield noun[1][word]
            continue
        elif n<=11:
            word=randint(0,len(noun[2]))
            yield noun[2][word]
            continue
        else:
            word=randint(0,len(noun[3]))
            yield noun[3][word]
            continue"""

import pickle
from random import randint
movies = open(r'movies.dat', 'r')
music = open(r'musio.dat', 'r')
tvseries = open(r'tvseries.dat', 'r')
phrases = open(r'phrases.dat', 'r')

def moviesrandom():
    list = pickle.load(movies)
    easy = pickle.load(movies)
    medium = pickle.load(movies)
    hard = pickle.load(movies)
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield list[randint(0,easy)],1
            continue
        elif flag < 13:
            yield list[randint(easy+1,medium)],1
            continue
        else:
            yield list[randint(medium+1,hard)],1
            continue

def musicrandom():
    list = pickle.load(music)
    easy = pickle.load(music)
    medium = pickle.load(music)
    hard = pickle.load(music)
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield list[randint(0,easy)],2
            continue
        elif flag < 13:
            yield list[randint(easy+1,medium)],2
            continue
        else:
            yield list[randint(medium+1,hard)],2
            continue

def tvseriesrandom():
    list = pickle.load(tvseries)
    easy = pickle.load(tvseries)
    medium = pickle.load(tvseries)
    hard = pickle.load(tvseries)
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield list[randint(0,easy)],3
            continue
        elif flag < 13:
            yield list[randint(easy+1,medium)],3
            continue
        else:
            yield list[randint(medium+1,hard)],3
            continue

def phrasesrandom():
    list = pickle.load(phrases)
    easy = pickle.load(phrases)
    medium = pickle.load(phrases)
    hard = pickle.load(phrases)
    while True:
        flag = randint(1,15)
        if flag < 8:
            yield list[randint(0,easy)],4
            continue
        elif flag < 13:
            yield list[randint(easy+1,medium)],4
            continue
        else:
            yield list[randint(medium+1,hard)],4
            continue

def allrandom():
    flag = randint(1,4)
    if flag==1:
        return moviesrandom()
    elif flag==2:
        return musicrandom()
    elif flag==3:
        return tvseriesrandom()
    else:
        return phrasesrandom()

while True:
    def word_generator(mode = 0):
        if mode == 0:
            return allrandom()
        elif mode == 1:
            return moviesrandom()
        elif mode == 2:
            return musicrandom()
        elif mode == 3:
            return tvseriesrandom()
        elif mode == 4:
            return phrasesrandom()