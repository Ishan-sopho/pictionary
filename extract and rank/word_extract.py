import openpyxl
import pickle
wb = openpyxl.load_workbook('songs list.xlsx')
movies = open(r'songs.txt','w')
sheet = wb.get_sheet_by_name('Sheet1')
easy,medium,hard=0,0,0
list = [None]*149
for i in range (3,151):
    word = str(sheet.cell(row=i,column=2).value.encode('utf-8'))
    print word
    movies.write(word)
    movies.write('\n')
    list.append(word)
movies.close()
score = [0]*len(list)
data = [list,easy,medium,hard,score]
pickle.dump(data, open(r'songs.dat','w'))
