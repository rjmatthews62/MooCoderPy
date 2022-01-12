#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
from ScrollText import *
from TerminalWindow import *
 
def testButton():
    print("Test BUtton")
    print("Text=",memo1.get("1.0",END))
    print(memo1.index(CURRENT))
    mytext.set(memo1.index(CURRENT))

def doColour():
    memo1.tag_add("red","1.0","1.end")
    memo1.tag_config("red",{"foreground":"red"})
    memo1.tag_add("yellow","2.0","2.end")
    memo1.tag_config("yellow",{"background":"#80ff80"})

def doOpen():
    tf = filedialog.askopenfilename(
        initialdir="C:/td/srtmoo/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.moo"),)
        )
    if tf:
        with open(tf,"r") as f:
            data=f.read();
            memo1.delete("1.0",END)
            memo1.insert("1.0",data)

def selectionCallback(event):
    print("Event=",event)
    mytext.set(memo1.index(INSERT))

def doClose():
    f2.disconnect()
    root.quit()    

def doConnect():
    f2.doConnect("srtmoo.net",8492)

def doDisconnect():
    f2.disconnect()

print("Hello")
root = Tk()
root.title("MooCoderPy Test")
root.protocol("WM_DELETE_WINDOW",doClose)
nb=ttk.Notebook(root)
nb.pack(fill=BOTH,expand=True)
ff=Frame(nb)
nb.add(ff,text="Edit")
f2=TerminalWindow(nb,background="black",foreground="white",font=("Courier New",12,"bold"),insertbackground="white")
nb.add(f2,text="Terminal")
memo1 = Text(ff,insertbackground="white");
memo1.bind("<<Selection>>",selectionCallback)
memo1.config({"background":"black","foreground":"white","font":("Courier New",12,"bold")})
scrollbar = ttk.Scrollbar(ff, orient='vertical', command=memo1.yview)
scrollbar.pack(side=RIGHT,fill=Y)
memo1.pack(fill=BOTH,expand=True)
memo1["yscrollcommand"]=scrollbar.set
bottom = Frame(root,bg="LightGray")
bottom.pack(side=BOTTOM);
mytext=StringVar();
mytext.set("Bottom")
label1=Label(bottom,text="Bottom", textvariable=mytext);
label1.pack(side=LEFT)
button=Button(bottom,text="Button1", command=testButton)
button.pack(side=LEFT)
btn2=Button(bottom,text="Colour", command=doColour)
btn2.pack(side=LEFT)
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=doOpen,underline=0)
filemenu.add_command(label="Connect", command=doConnect,underline=0)
filemenu.add_command(label="Disconnect", command=doDisconnect, underline=0)
filemenu.add_command(label="Exit", command=doClose,underline=1)
menubar.add_cascade(label="File",menu=filemenu, underline=0)
root.config(menu=menubar)
nb.enable_traversal()
nb.select(f2)
# Code to add widgets will go here...
root.mainloop()
print("Done")

