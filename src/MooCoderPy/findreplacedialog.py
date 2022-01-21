from cgitb import text
from msilib.schema import CheckBox
from tkinter import *
import tkinter.simpledialog

class FindReplaceSettings:
    search:str=""
    replace:str=""
    caseSensitive:bool=False
    backward:bool=False
    go:bool=False
    isreplace:bool=False

findReplaceSettings=FindReplaceSettings() # Global holder for settings.

class FindReplaceDialog(tkinter.simpledialog.Dialog):
    searchvar:StringVar
    replacevar:StringVar
    casevar:IntVar
    backvar:IntVar

    def body(self, master):
        f=("Arial",12)
        Label(master, text="Search",font=f).grid(row=0,column=0)
        self.searchvar=StringVar(value=findReplaceSettings.search)
        self.search=Entry(master,width=60,font=f,textvariable=self.searchvar)
        self.search.grid(row=0, column=1)
        Label(master, text="Replace",font=f).grid(row=1,column=0)
        self.replacevar=StringVar(value=findReplaceSettings.replace)
        self.replace=Entry(master,width=60,font=f,textvariable=self.replacevar)
        self.replace.grid(row=1, column=1)
        self.casevar=IntVar(value=int(findReplaceSettings.caseSensitive))
        chk=Checkbutton(master,text="Case Senstive",variable=self.casevar)
        chk.grid(row=2,column=1,sticky=W)
        self.backvar=IntVar(value=int(findReplaceSettings.backward))
        Checkbutton(master,text="Backwards",variable=self.backvar).grid(row=3,column=1,sticky=W)
        findReplaceSettings.go=False
        findReplaceSettings.isreplace=False
        return self.search # initial focus

    def apply(self):
        findReplaceSettings.search=self.searchvar.get()
        findReplaceSettings.replace=self.replacevar.get()
        findReplaceSettings.caseSensitive=bool(self.casevar.get())
        findReplaceSettings.backward=bool(self.backvar.get())
        findReplaceSettings.go=True
        
    def doReplace(self):
        findReplaceSettings.isreplace=True
        self.ok()

    def buttonbox(self):
        '''add standard button box.

        override if you do not want the standard buttons
        '''
    # Copied base buttons from ancestor. Coulnd find a logical way to inherit.
        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box,text="Replace", width=10,command=self.doReplace)
        w.pack(side=LEFT, padx=5,pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()


if __name__=="__main__":
    root=Tk()
    FindReplaceDialog(None,"Find and Replace")
    print("Replace done.")
    print(findReplaceSettings.replace)
    print(findReplaceSettings.search)
    print(findReplaceSettings.caseSensitive)
    print(findReplaceSettings.backward)
    print(findReplaceSettings.go)
    print(findReplaceSettings.isreplace)

