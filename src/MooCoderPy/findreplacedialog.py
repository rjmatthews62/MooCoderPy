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
    all:bool=False
    go:bool=False

findReplaceSettings=FindReplaceSettings() # Global holder for settings.

class FindReplaceDialog(tkinter.simpledialog.Dialog):
    searchvar:StringVar
    replacevar:StringVar
    casevar:IntVar
    backvar:IntVar
    wordmatch:IntVar
    selection:IntVar
    all:IntVar
    backbtn:Checkbutton
    selbtn:Checkbutton

    def body(self, master):
        f=("Arial",12)
        Label(master, text="Search",font=f).grid(row=0,column=0)
        self.searchvar=StringVar(value=findReplaceSettings.search)
        self.search=Entry(master,width=60,font=f,textvariable=self.searchvar)
        self.search.grid(row=0, column=1,columnspan=3)
        if  findReplaceSettings.isreplace:
            Label(master, text="Replace",font=f).grid(row=1,column=0)
            self.replacevar=StringVar(value=findReplaceSettings.replace)
            self.replace=Entry(master,width=60,font=f,textvariable=self.replacevar)
            self.replace.grid(row=1, column=1, columnspan=3)
        self.casevar=IntVar(value=int(findReplaceSettings.caseSensitive))
        Checkbutton(master,text="Case Senstive",variable=self.casevar,font=f).grid(row=2,column=0,sticky=W)
        self.backvar=IntVar(value=int(findReplaceSettings.backward))
        bck=Checkbutton(master,text="Backwards",variable=self.backvar,font=f)
        bck.grid(row=2,column=1,sticky=W)
        self.backbtn=bck
        self.wordmatch=IntVar(value=int(findReplaceSettings.wordmatch))
        Checkbutton(master,text="Word Match",variable=self.wordmatch,font=f).grid(row=2,column=2,sticky=W)
        if findReplaceSettings.isreplace:
            self.all=IntVar(value=int(findReplaceSettings.all))
            all=Checkbutton(master,text="All",variable=self.all,font=f,command=self.updateScreen)
            all.grid(row=3,column=0,sticky=W)
            self.selection=IntVar(value=int(findReplaceSettings.selection))
            self.selbtn=Checkbutton(master,text="Selection",variable=self.selection,font=f)
            self.selbtn.grid(row=3,column=1,sticky=W)
            self.updateScreen()
        findReplaceSettings.go=False
        self.search.select_range(0, END)
        return self.search # initial focus

    def updateScreen(self,event=None):
        self.backbtn.configure(state=DISABLED if self.all.get() else NORMAL)
        self.selbtn.configure(state=DISABLED if not self.all.get() else NORMAL)


    def apply(self):
        findReplaceSettings.search=self.searchvar.get()
        if findReplaceSettings.isreplace:
            findReplaceSettings.replace=self.replacevar.get()
            findReplaceSettings.selection=self.selection.get()
            findReplaceSettings.all=self.all.get()
        findReplaceSettings.caseSensitive=bool(self.casevar.get())
        findReplaceSettings.backward=bool(self.backvar.get())
        findReplaceSettings.wordmatch=bool(self.wordmatch.get())
        findReplaceSettings.go=True

if __name__=="__main__":
    root=Tk()
    findReplaceSettings.isreplace=True
    FindReplaceDialog(None,"Find and Replace")
    print("Replace done.")
    print(findReplaceSettings.replace)
    print(findReplaceSettings.search)
    print(findReplaceSettings.caseSensitive)
    print(findReplaceSettings.backward)
    print(findReplaceSettings.go)
    print(findReplaceSettings.isreplace)

