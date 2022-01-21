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
        FindReplaceDialog.go=False
        return self.search # initial focus

    def apply(self):
        findReplaceSettings.search=self.searchvar.get()
        findReplaceSettings.replace=self.replacevar.get()
        findReplaceSettings.caseSensitive=bool(self.casevar.get())
        findReplaceSettings.backward=bool(self.backvar.get())
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

