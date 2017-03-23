import openpyxl
import pickle
wb = openpyxl.load_workbook('acm work.xlsx')
movies = open(r'movies.txt','w')
sheet = wb.get_sheet_by_name('Sheet1')
easy,medium,hard=0,0,0
list = [None]*1419
for i in range (2,1421):
    word = str(sheet.cell(row=i,column=1).value.encode('utf-8'))
    print word
    movies.write(word)
    movies.write('\n')
    list[i-3] = word
movies.close()
score = [0]*len(list)
data = [list,easy,medium,hard,score]
pickle.dump(data, open(r'movies.dat','w'))
