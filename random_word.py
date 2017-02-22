def word_generator():
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
            continue