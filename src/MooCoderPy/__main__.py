#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
from tkinter import scrolledtext
import os,sys
# Stupid packaging messes with paths...
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print("SCRIPT_DIR=",SCRIPT_DIR)
sys.path.append(SCRIPT_DIR)

from ScrollText import *
from TerminalWindow import *
import SettingsDialog
import configparser
 
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

def doClose():
    f2.disconnect()
    root.quit()    

def doConnect():
    inifile=SettingsDialog.getConfig()
    server=inifile["settings"]["Server"]
    connectstr=inifile["settings"]["Connect"]
    (server,port)=server.split(":")
    f2.connectString=connectstr
    f2.doConnect(server,int(port))

def doDisconnect():
    f2.disconnect()

def doSettings():
    SettingsDialog.SettingsDialog(root,title="Server Configuration")

print("Hello")
root = Tk()
root.title("MooCoderPy Test")
root.protocol("WM_DELETE_WINDOW",doClose)
nb=ttk.Notebook(root)
nb.pack(fill=BOTH,expand=True)
ff=Frame(nb)
nb.add(ff,text="Edit")
f2=TerminalWindow(nb,background="black",foreground="white",font=("Courier",12,"bold"),insertbackground="white")
nb.add(f2,text="Terminal")
memo1 = scrolledtext.ScrolledText(ff,insertbackground="white");
memo1.config({"background":"black","foreground":"white","font":("Courier",12,"bold")})
memo1.pack(fill=BOTH,expand=True)
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=doOpen,underline=0)
filemenu.add_command(label="Connect", command=doConnect,underline=0)
filemenu.add_command(label="Disconnect", command=doDisconnect, underline=0)
filemenu.add_command(label="Exit", command=doClose,underline=1)
settingmenu=Menu(menubar,tearoff=0)
settingmenu.add_command(label="Server Config",command=doSettings, underline=0)
menubar.add_cascade(label="File",menu=filemenu, underline=0)
menubar.add_cascade(label="Settings", menu=settingmenu, underline=0)
root.config(menu=menubar)
nb.enable_traversal()
nb.select(f2)
# Code to add widgets will go here...
root.mainloop()
print("Done")

