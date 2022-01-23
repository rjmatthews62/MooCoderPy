from gettext import find
from tkinter import *
import tkinter.simpledialog

class FindReplaceSettings:
    search:str=""
    replace:str=""
    caseSensitive:bool=False
    backward:bool=False
    isreplace:bool=False
    selection:bool=False
    wordmatch:bool=False
    go:bool=False

findReplaceSettings=FindReplaceSettings() # Global holder for settings.

class FindReplaceDialog(tkinter.simpledialog.Dialog):
    searchvar:StringVar
    replacevar:StringVar
    casevar:IntVar
    backvar:IntVar
    wordmatch:IntVar

    def body(self, master):
        f=("Arial",12)
        Label(master, text="Search",font=f).grid(row=0,column=0)
        self.searchvar=StringVar(value=findReplaceSettings.search)
        self.search=Entry(master,width=60,font=f,textvariable=self.searchvar)
        self.search.grid(row=0, column=1)
        if  findReplaceSettings.isreplace:
            Label(master, text="Replace",font=f).grid(row=1,column=0)
            self.replacevar=StringVar(value=findReplaceSettings.replace)
            self.replace=Entry(master,width=60,font=f,textvariable=self.replacevar)
            self.replace.grid(row=1, column=1)
        self.casevar=IntVar(value=int(findReplaceSettings.caseSensitive))
        chk=Checkbutton(master,text="Case Senstive",variable=self.casevar)
        chk.grid(row=2,column=1,sticky=W)
        self.backvar=IntVar(value=int(findReplaceSettings.backward))
        Checkbutton(master,text="Backwards",variable=self.backvar).grid(row=3,column=1,sticky=W)
        self.wordmatch=IntVar(value=int(findReplaceSettings.wordmatch))
        Checkbutton(master,text="Word Match",variable=self.wordmatch).grid(row=4,column=1,sticky=W)
        findReplaceSettings.go=False
        self.search.select_range(0, END)
        return self.search # initial focus

    def apply(self):
        findReplaceSettings.search=self.searchvar.get()
        if hasattr(self,"replacevar"):
            findReplaceSettings.replace=self.replacevar.get()
        findReplaceSettings.caseSensitive=bool(self.casevar.get())
        findReplaceSettings.backward=bool(self.backvar.get())
        findReplaceSettings.wordmatch=bool(self.wordmatch.get())
        findReplaceSettings.go=True

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

