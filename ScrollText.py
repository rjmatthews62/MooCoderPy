import tkinter as tk
from tkinter import ttk
from queue import Queue
from threading import Thread
import time

class ScrollText(tk.Text):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self,parent)
        self.textbox=tk.Text(self,**kwargs)
        self.scrollbar=ttk.Scrollbar(self, orient='vertical', command=self.textbox.yview)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.textbox.pack(fill=tk.BOTH,expand=True)
        self.textbox["yscrollcommand"]=self.scrollbar.set
        self.queue=Queue(20)
        self.bind("<<sendtext>>",self.handletext)
    
    def sendtext(self,msg):
        self.queue.put(msg)
        self.event_generate("<<sendtext>>",when='tail')
    
    def handletext(self,event):
        while not self.queue.empty():
            msg=self.queue.get()
            self.addtext(msg)
            self.queue.task_done()
    
    def addtext(self,msg):
            self.textbox.insert("end",msg)
            self.textbox.see("end")
            
    def testSend(self):
        time.sleep(2)
        self.sendtext("This should appear after 5 seconds\nAnd this is a second line.")
        print("Thread done.")


if __name__ == "__main__":
    root=tk.Tk()
    wtest=ScrollText(root,background="blue",foreground="white")        
    wtest.pack()
    wtest.textbox.insert("1.0","Hello")
    t=Thread(target=wtest.testSend)
    t.start()
    wtest.mainloop()