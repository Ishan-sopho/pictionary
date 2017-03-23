import pickle
data = open(r'bitsian.txt',  'r').readlines()
words=[]
for i in data:
    words.append(i)
    print i
pickle.dump([words, 0, 0, 0, [None]*len(words)], open(r'bitsian.dat', 'w'))
'''from Tkinter import *
import ttk

root = Tk()
v=IntVar()
L=[]
L.append(Radiobutton(root, text='A'))
L.append(Radiobutton(root, text='B'))
root.geometry("300x300")
radio = ttk.Style()
#radio.configure('radiobutton', background='#53ff1a', font=('Times New Roman', 18), indicatoron=0)

for i in range(len(L)):
    R = ttk.Radiobutton(root, text='afwef', variable=v, value=i, font=('Times New Roman', 18))
    R.grid(row=1, column=i+1)
mainloop()'''
