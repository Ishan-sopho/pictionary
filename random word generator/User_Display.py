from Tkinter import *
from random_word import *

root = Tk()

mode = IntVar()
word = "word"
word_type = "word-type"
L = [None]*5

global disp_type
global disp_word

disp_type = Label(root, text=word_type)
disp_word = Label(root, text=word)
disp_word.config(width=40)

disp_type.grid(row=2, column=3)
disp_word.grid(row=3 ,column=3)

button = Button(root, text="Generate", command= lambda : change(mode))
button.grid(row=4, column=3)

def change(mode):
    word,word_type = word_generator(mode.get())
    disp_word.config(text=word)
    disp_type.config(text=word_type)
    root.update()

L.append(Radiobutton(root, text="MIXED", variable=mode, value=0).grid(row=1, column=1))
L.append(Radiobutton(root, text="MOVIES", variable=mode, value=1).grid(row=1, column=2))
L.append(Radiobutton(root, text="SONGS", variable=mode, value=2).grid(row=1, column=3))
L.append(Radiobutton(root, text="T.V. Series", variable=mode, value=3).grid(row=1, column=4))
L.append(Radiobutton(root, text="Bitsian lingo", variable=mode, value=4).grid(row=1, column=5))

mainloop()