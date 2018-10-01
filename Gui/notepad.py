from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.simpledialog import askstring
class Notepad(Frame):
    def __init__(self, parent=None, text=None, file=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makewidgets()
        self.settext()

    def makewidgets(self):
        frm=Frame(self)
        frm.pack(side=TOP)
        sbar=Scrollbar(self)
        text=Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)


        Button(frm, text='paste', command=self.onPaste).pack(side=LEFT)
        Button(frm, text='Save', command=self.Onsave).pack(side=LEFT)
        Button(frm, text='Copy', command=self.onCopy).pack(side=LEFT)

        self.text=text

    def onPaste(self):
        try:
            text=self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass

    def Onsave(self):
        filename=asksaveasfilename()
        if filename:
            alltext=self.gettext()
            open(filename ,'w').write(alltext)

    def onCopy(self):
        text=self.text.get(SEL_FIRST,SEL_LAST)
        self.text.delete(SEL_LAST,SEL_LAST)
        self.clipboard_clear()
        self.clipboard_append(text)



    def settext(self,  text=None,file=None):
        if file:
            text=open(file, 'r').read()
            self.text.delete('1.0', END)
            self.text.insert('1.0', text)
            self.text.mark_set(INSERT, '1.0')
            self.text.focus()

    def gettext(self):
        return self.text.get('1.0', END)

if __name__=='__main__':
    root=Tk()
    if len(sys.argv)>1:
        nt=Notepad(file=sys.argv[1])

    else:
        nt=Notepad(text='words go\n in here')

    def show(event):
        print(repr(nt.gettext()))

    root.bind('<Key-Escape>', show)
    root.mainloop()

