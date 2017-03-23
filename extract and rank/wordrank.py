import os,pickle
from Tkinter import *
file = "songs.dat"  #change this name to the file you want to rank
data = pickle.load(open(file, 'r'))
print "click 'yes' button if you want the word in pictionary"

global i
i=0
def word_gen():
    while i<len(data[0]):
        i+=1
        yield data[0][i]
    pickle.dump(data, open(r'temp.dat', 'w'))
    os.remove(file)
    os.rename(r'temp.dat', file)
    quit()
global word
word = word_gen()

def rank(choice):
    display.config(text=word.next())
    if choice:
        data[4][i]=1
    else:
        data[4][i]=0

root = Tk()

global display
display = Label(root, text="")
display.pack()

Button(root, text="YES", command= lambda : rank(1)).pack()
Button(root, text="NO", command= lambda : rank(0)).pack()
mainloop()