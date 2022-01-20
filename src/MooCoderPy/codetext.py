from ScrollText import *
from tkinter import *

class CodeText(ScrollText):
    bottom:Frame
    test:Entry
    caption:str
    testvar:StringVar

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bottom = Frame(self, bg="LightGray")
        self.bottom.pack(side=BOTTOM, fill=X)
        lbl=Label(self.bottom,text="Test ",font="Arial 12")
        lbl.pack(side=LEFT)
        self.testvar=StringVar()
        self.test=Entry(self.bottom,width=60,font="Arial 12",textvariable=self.testvar)
        self.test.pack(side=LEFT,fill=X,expand=True)

    
    def testName(self)->str:
        return self.caption.lower().replace("*","").replace("=","_").replace("#","").replace(":","_")
        





