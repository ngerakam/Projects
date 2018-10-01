from tkinter import *
import openpyxl

root=Tk()
lab=Label(root, text='names')
lab1=Label(root, text='admission number')
ent=Entry(root, width=50, relief=RIDGE)
ent1=Entry(root, width=50,relief=RIDGE)
lab.grid(row=1, column=0, sticky=NSEW)
lab1.grid(row=2, column=0, sticky=NSEW)
ent.grid(row=1, column=1, sticky=NSEW)
ent1.grid(row=2, column=1, sticky=NSEW)

def displayWidget():
    print(str(ent.get()), str(ent1.get()))

def addToSpreadsheet():
    val=['A1']
    wb=openpyxl.load_workbook('Book1.xlsx')
    sheet=wb.active
    sheet['A1']=str(ent.get())
    sheet['B1']=str(ent1.get())
    #for rows  in sheet['A1':'A40']:
        #for row in rows:
            #sheet[str(val)]=str(ent.get())
            #val+=1

    wb.save("Book1.xlsx")
Button(root, text='display', command=displayWidget).grid()
Button(root, text='OK', command=addToSpreadsheet).grid(row=2, column=2)

mainloop()