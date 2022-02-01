import tkinter as tk
from tkinter import ttk
from tkinter import font
from queue import Queue
from threading import Thread
import time

# Turns out there's a perfectly good scrolledtext component already, but this works as a useful wrapper anyway.

class ScrollText(tk.Text):
    tabtype=0
    fontsize:int=12
    fontctl:font.Font=None
    nowrap:bool=False
    hscroll:tk.Scrollbar = None

    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self,parent)
        if "nowrap" in kwargs:
            self.nowrap=kwargs["nowrap"]
            del kwargs["nowrap"]
        self.textbox=tk.Text(self,**kwargs)
        self.scrollbar=ttk.Scrollbar(self, orient='vertical', command=self.textbox.yview)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.textbox.pack(fill=tk.BOTH,expand=True)
        self.textbox["yscrollcommand"]=self.scrollbar.set
        if self.nowrap:
            self.textbox.configure(wrap=tk.NONE)
            self.hscroll=ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.textbox.xview)
            self.hscroll.pack(side=tk.BOTTOM, fill=tk.X)
            self.textbox["xscrollcommand"]=self.hscroll.set

        self.queue=Queue(20)
        self.bind("<<sendtext>>",self.handletext)
        self.setFontSize(self.fontsize)
    
    def setFontSize(self,newsize:int):
        self.fontctl=font.Font(family="Courier", size=newsize, weight="bold")
        self.textbox.configure(font=self.fontctl)
        self.fontsize=newsize

    def sendtext(self,msg):
        self.queue.put(msg)
        self.event_generate("<<sendtext>>",when='tail')
    
    def addln(self,line:str):
        self.textbox.insert("end","\n"+line)
        self.textbox.see("end")
    
    def clear(self):
        self.textbox.delete("1.0","end")

    def handletext(self,event):
        while not self.queue.empty():
            msg=self.queue.get()
            self.addtext(msg)
            self.queue.task_done()
        self.flush()
    
    def flush(self):
        pass

    def addtext(self,msg):
            self.textbox.insert("end",msg)
            self.textbox.see("end")
    
    def getText(self)->str:
        return self.textbox.get("1.0",tk.END)

    def testSend(self):
        time.sleep(2)
        self.sendtext("This should appear after 5 seconds\nAnd this is a second line.")
        print("Thread done.")
    
    def lines(self):
        """Return text as a list of strings"""
        return self.textbox.get("1.0","end").split("\n")

if __name__ == "__main__":
    root=tk.Tk()
    wtest=ScrollText(root,background="blue",foreground="white")        
    wtest.pack()
    wtest.textbox.insert("1.0","Hello")
    t=Thread(target=wtest.testSend)
    t.start()
    wtest.mainloop()