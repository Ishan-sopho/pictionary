import random_word
from Tkinter import *
noun = random_word.word_generator()
print next(noun)
root = Tk()
root.title("Pictionary")
mode = IntVar()
display=StringVar()
def change(display,noun):
    display = next(noun)
    return
Entry(root, textvariable=display).grid(row=2, column=3)
generate = Button(root, text='GENERATE', command=lambda: change(display,noun)).grid(row=3, column=3)
#Radiobutton(root, text="easy words", variable=mode, value=1).grid(row=1, column=1)
#Radiobutton(root, text="medium words", variable=mode, value=2).grid(row=1, column=2)
#Radiobutton(root, text="hard words", variable=mode, value=3).grid(row=1, column=3)
#Radiobutton(root, text="really hard words", variable=mode, value=4).grid(row=1, column=4)
#Radiobutton(root, text="all words", variable=mode, value=5).grid(row=1, column=5)
mainloop()