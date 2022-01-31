#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
from tkinter import font
from tkinter import scrolledtext
from tkinter import simpledialog
import os,sys

# Stupid packaging messes with paths...
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print("SCRIPT_DIR=",SCRIPT_DIR)
sys.path.append(SCRIPT_DIR)

from ScrollText import *
from TerminalWindow import *
import SettingsDialog
import configparser

tw:TerminalWindow
lastpage:Widget
fontsize:int=12

def doOpen():
    tf = filedialog.askopenfilename(
        initialdir="C:/td/srtmoo/", 
        title="Open Text file", 
        filetypes=(("MOO source Files", "*.moo"),("Text","*.txt"),("Any","*.*"))
        )
    if tf:
        with open(tf,"r") as f:
            data=f.read()
            tw.openEdit("Local Edit","",data)

def doClose():
    tw.disconnect()
    tw.saveSettings()
    root.quit()    

def doConnect():
    inifile=SettingsDialog.getConfig()
    server=inifile["settings"]["Server"]
    connectstr=inifile["settings"]["Connect"]
    (server,port)=server.split(":")
    tw.connectString=connectstr
    tw.doConnect(server,int(port))

def doDisconnect():
    tw.disconnect()

def doSettings():
    global fontsize,nb
    oldsize=fontsize
    SettingsDialog.SettingsDialog(root,title="Server Configuration")
    getInitalSettings()
    if (fontsize!=oldsize):
        for tab in nb.tabs():
            w=nb.nametowidget(tab)
            if hasattr(w,"setFontSize"):
                w.setFontSize(fontsize)


def doupdate(event=None):
    re=tw.currentPage()
    if re and re.tabtype in (CodeText.MODE_EDIT,CodeText.MODE_CODE,CodeText.MODE_PROPERTY):
        tw.docompile(re)

def doTabChanged(event):
    global lastpage
    tabname=nb.tab("current","text")
    if (tabname=="Terminal"):
        tw.sendEntry.focus()
    #track previous page for toggle.
    w=nb.nametowidget(nb.select())
    if w!=tw:
        lastpage=w

def donewtab(event=None):
    """Load a verb into a new tab"""
    verb=simpledialog.askstring("Verb","Enter Object:Verb")
    if (verb):
        tw.loadVerb(verb)

def viewStack(event=None):
    """Make stack visible."""
    global stackloaded
    mainpack(not stackloaded)

def togglePage(event:Event=None):
    """Flip between Terminal window and previous view"""
    global nb,tw,lastpage
    w=nb.nametowidget(nb.select())
    if w==tw:
        nb.select(lastpage)
    else:
        nb.select(tw)

def buildMenu():
    menubar=Menu(root)
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="Open", command=doOpen,underline=0)
    filemenu.add_command(label="Connect", command=doConnect,underline=0)
    filemenu.add_command(label="Disconnect", command=doDisconnect, underline=0)
    filemenu.add_command(label="Exit", command=doClose,underline=1)
    settingmenu=Menu(menubar,tearoff=0)
    settingmenu.add_command(label="Server Config",command=doSettings, underline=0)
    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Send Update F5", command=doupdate, underline=0)
    root.bind("<F5>",doupdate)
    projectmenu=Menu(menubar,tearoff=0)
    projectmenu.add_command(label="New Tab Ctrl+N",command=donewtab,underline=0)
    projectmenu.add_command(label="Get Verbs Ctrl+Shift+V",command=tw.getVerbs,underline=0)
    projectmenu.add_command(label="Get Properties",command=tw.getProperties,underline=4)
    projectmenu.add_command(label="Clear Project",command=tw.clearProject,underline=0)
    
    root.bind("<Control-Shift-Key-V>",tw.getVerbs)
    root.bind("<Control-Shift-Key-v>",tw.getVerbs)
    # Apparently the key binding is case sensitive...
    root.bind("<Control-Key-N>",donewtab)
    root.bind("<Control-Key-n>",donewtab)
    menubar.add_cascade(label="File",menu=filemenu, underline=0)
    menubar.add_cascade(label="Settings", menu=settingmenu, underline=0)
    menubar.add_cascade(label="Edit", menu=editmenu, underline=0)
    menubar.add_cascade(label="Project",menu=projectmenu, underline=0)
    viewmenu=Menu(menubar,tearoff=0)
    viewmenu.add_command(label="Stack", command=viewStack,underline=0)
    viewmenu.add_command(label="Toggle View Ctrl+Shift+T", command=togglePage, underline=0)
    root.bind("<Control-Shift-Key-T>",togglePage)
    root.bind("<Control-Shift-Key-t>",togglePage)
    menubar.add_cascade(label="View",menu=viewmenu,underline=0)
    root.config(menu=menubar)

def mainpack(usestack:bool):
    """Pack the main window so it's possible to hide and reload stack"""
    global stackloaded
    try:
        pane.forget(stack)
    except:
        pass
    if usestack:
        pane.add(stack,weight=1)
    stackloaded=usestack

def loadSettings():
    global fontsize
    ifile=SettingsDialog.getConfig()
    tw.dumpobject=ifile['settings'].get('LastDump',"")

def getInitalSettings():
    global fontsize
    ifile=SettingsDialog.getConfig()
    fontsize=ifile['settings'].getint("fontsize",12)

def doVerbDblClick(event=None):
    nd=verblist.item(verblist.selection())
    tw.loadVerb(nd["text"]+":"+nd["values"][1])

def doPropDblClick(event=None):
    nd=proplist.item(proplist.selection())
    tw.editProp(nd["text"]+"."+nd["values"][1])

def doStackClick(event:Event):
    tw.gotoError(stack)

if not("__VERSION__" in globals()):
    import importlib.metadata
    try:
        __VERSION__ = importlib.metadata.version('MooCoderPy-rjmatthews62')
    except:
        __VERSION__ = "code only"

print("MooCoderPy",__VERSION__)
root = Tk()
try:
    root.iconbitmap(SCRIPT_DIR+"/moocoder.ico")
except:
    print("Couldn't find icon file. Trying png")
    try:
        ico=PhotoImage(file=SCRIPT_DIR+"/moocoder.png")
        root.iconphoto(False,ico)
    except:
        print("Didn't need that dumb icon anyway.")

myfont=font.Font(name="Arial",size=10)
getInitalSettings()
root.option_add( "*font", myfont)
root.title("MooCoderPy "+__VERSION__)
root.protocol("WM_DELETE_WINDOW",doClose)
pane=ttk.PanedWindow(root,orient=HORIZONTAL)
pane.pack(fill=BOTH, expand=True)

stack=Text(pane,width=50)
stack.bind("<Double-Button-1>",doStackClick)
nb=ttk.Notebook(pane)
pane.add(nb,weight=5)
mainpack(False)

tw=TerminalWindow(nb,background="black",foreground="white",font=("Courier",fontsize,"bold"),insertbackground="white")

tw.normalfont=myfont
tw.setFontSize(fontsize)
tw.setstackvisible=mainpack
tw.stack=stack
nb.add(tw,text="Terminal")

verbframe=Frame(nb)
nb.add(verbframe,text="Verbs")
lastpage=verbframe
verblist=ttk.Treeview(verbframe,columns=("c1","c2","c3","c4"))
verblist.heading("#0",text="Obj")
verblist.heading("c1",text="Name")
verblist.heading("c2",text="Verb")
verblist.heading("c3",text="Args")
verblist.heading("c4",text="Detail")
verblist.column("#0",stretch=False,width=50)
for i in range(3):
    verblist.column(i,stretch=False,width=80)
verblist.pack(fill=BOTH, expand=True)
verblist.bind("<Double-Button-1>",doVerbDblClick)
verblist.style=ttk.Style(verblist)
verblist.style.configure("Treeview",font=myfont)
verblist.style.configure("Treeview.Heading",font=myfont)

propframe=Frame(nb)
nb.add(propframe,text="Properties")

proplist=ttk.Treeview(propframe,columns=("name","prop","detail"))
proplist.heading("#0",text="Obj")
proplist.heading("name",text="Name")
proplist.heading("prop",text="Property")
proplist.heading("detail",text="Detail")
proplist.style=verblist.style
proplist.pack(fill=BOTH, expand=True)
proplist.column("#0",stretch=False,width=50)
proplist.column(0,stretch=False,width=50)
proplist.column(1,stretch=False,width=50)
tw.fitListContents(proplist)
proplist.bind("<Double-Button-1>",doPropDblClick)

nb.enable_traversal()
tw.lvVerbs=verblist
tw.lvProperties=proplist
nb.bind("<<NotebookTabChanged>>",func=doTabChanged)
nb.select(tw)
tw.pages=nb
buildMenu()
loadSettings()
try:
    root.state("zoomed") # Works in windows (and MacOs?)
except:
    root.attributes("-zoomed",True) # Works for linux

root.mainloop()
print("Done")

