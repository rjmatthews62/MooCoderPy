from tkinter import *
from tkinter import simpledialog


class MyQueryString(simpledialog._QueryDialog):
    width=50
    def __init__(self,*args, **kw):
        if "width" in kw:
            self.width=kw["width"]
            del kw["width"]
        super().__init__(*args,**kw)

    def body(self, master):

        w = Label(master, text=self.prompt, justify=LEFT)
        w.grid(row=0, padx=5, sticky=W)

        self.entry = Entry(master, name="entry", width=self.width)
        self.entry.grid(row=1, padx=5, sticky=W+E)

        if self.initialvalue is not None:
            self.entry.insert(0, self.initialvalue)
            self.entry.select_range(0, END)

        return self.entry
    
    def getresult(self):
        return self.entry.get()

def askstring(title, prompt, **kw):
    d = MyQueryString(title, prompt, **kw)
    return d.result

if __name__=="__main__":
    root=Tk()
    s=askstring("Testing","Prompt",initialvalue="The quick brown fox jumped over the lazy dog.",width=50)
    print(s)