from tkinter import simpledialog
from tkinter.ttk import Notebook
from warnings import showwarning
from ScrollText import *
from tkinter import *
from tkinter import messagebox,font
import socket, threading,select
import SettingsDialog
from codetext import *
from wgplib import *
import re
import mydialogs
import splitlist


class TerminalWindow(ScrollText):
    pages:Notebook=None
    getstack:bool=False
    setstackvisible=None
    stack:Text=None
    errorverb:str=""
    arglist={}
    verblist=[]
    proplist={}
    namelist={}
    lastobj:str=""
    lvVerbs:ttk.Treeview=None
    lvProperties:ttk.Treeview=None
    dumpobject:str=""
    normalfont:font.Font=None
    testtab:str=""
    lastlno:int=0
    lastproperty:str=""

    ColorTable = (
        "#000000",
        "#c00000",
        "#00c000",
        "#c0c000",
        "#0000c0",
        "#c000c0",
        "#00c0c0",
        "#c0c0c0",
    )
    ColorTableBold = (
        "#000000",
        "#ff0000",
        "#00ff00",
        "#ffff00",
        "#0000ff",
        "#ff00ff",
        "#00ffff",
        "#ffffff",
    )
    ColorX256 = (
        "#000000",
        "#800000",
        "#008000",
        "#808000",
        "#000080",
        "#800080",
        "#008080",
        "#c0c0c0",
        "#808080",
        "#ff0000",
        "#00ff00",
        "#ffff00",
        "#0000ff",
        "#ff00ff",
        "#00ffff",
        "#ffffff",
        "#000000",
        "#00005f",
        "#000087",
        "#0000af",
        "#0000d7",
        "#0000ff",
        "#005f00",
        "#005f5f",
        "#005f87",
        "#005faf",
        "#005fd7",
        "#005fff",
        "#008700",
        "#00875f",
        "#008787",
        "#0087af",
        "#0087d7",
        "#0087ff",
        "#00af00",
        "#00af5f",
        "#00af87",
        "#00afaf",
        "#00afd7",
        "#00afff",
        "#00d700",
        "#00d75f",
        "#00d787",
        "#00d7af",
        "#00d7d7",
        "#00d7ff",
        "#00ff00",
        "#00ff5f",
        "#00ff87",
        "#00ffaf",
        "#00ffd7",
        "#00ffff",
        "#5f0000",
        "#5f005f",
        "#5f0087",
        "#5f00af",
        "#5f00d7",
        "#5f00ff",
        "#5f5f00",
        "#5f5f5f",
        "#5f5f87",
        "#5f5faf",
        "#5f5fd7",
        "#5f5fff",
        "#5f8700",
        "#5f875f",
        "#5f8787",
        "#5f87af",
        "#5f87d7",
        "#5f87ff",
        "#5faf00",
        "#5faf5f",
        "#5faf87",
        "#5fafaf",
        "#5fafd7",
        "#5fafff",
        "#5fd700",
        "#5fd75f",
        "#5fd787",
        "#5fd7af",
        "#5fd7d7",
        "#5fd7ff",
        "#5fff00",
        "#5fff5f",
        "#5fff87",
        "#5fffaf",
        "#5fffd7",
        "#5fffff",
        "#870000",
        "#87005f",
        "#870087",
        "#8700af",
        "#8700d7",
        "#8700ff",
        "#875f00",
        "#875f5f",
        "#875f87",
        "#875faf",
        "#875fd7",
        "#875fff",
        "#878700",
        "#87875f",
        "#878787",
        "#8787af",
        "#8787d7",
        "#8787ff",
        "#87af00",
        "#87af5f",
        "#87af87",
        "#87afaf",
        "#87afd7",
        "#87afff",
        "#87d700",
        "#87d75f",
        "#87d787",
        "#87d7af",
        "#87d7d7",
        "#87d7ff",
        "#87ff00",
        "#87ff5f",
        "#87ff87",
        "#87ffaf",
        "#87ffd7",
        "#87ffff",
        "#af0000",
        "#af005f",
        "#af0087",
        "#af00af",
        "#af00d7",
        "#af00ff",
        "#af5f00",
        "#af5f5f",
        "#af5f87",
        "#af5faf",
        "#af5fd7",
        "#af5fff",
        "#af8700",
        "#af875f",
        "#af8787",
        "#af87af",
        "#af87d7",
        "#af87ff",
        "#afaf00",
        "#afaf5f",
        "#afaf87",
        "#afafaf",
        "#afafd7",
        "#afafff",
        "#afd700",
        "#afd75f",
        "#afd787",
        "#afd7af",
        "#afd7d7",
        "#afd7ff",
        "#afff00",
        "#afff5f",
        "#afff87",
        "#afffaf",
        "#afffd7",
        "#afffff",
        "#d70000",
        "#d7005f",
        "#d70087",
        "#d700af",
        "#d700d7",
        "#d700ff",
        "#d75f00",
        "#d75f5f",
        "#d75f87",
        "#d75faf",
        "#d75fd7",
        "#d75fff",
        "#d78700",
        "#d7875f",
        "#d78787",
        "#d787af",
        "#d787d7",
        "#d787ff",
        "#d7af00",
        "#d7af5f",
        "#d7af87",
        "#d7afaf",
        "#d7afd7",
        "#d7afff",
        "#d7d700",
        "#d7d75f",
        "#d7d787",
        "#d7d7af",
        "#d7d7d7",
        "#d7d7ff",
        "#d7ff00",
        "#d7ff5f",
        "#d7ff87",
        "#d7ffaf",
        "#d7ffd7",
        "#d7ffff",
        "#ff0000",
        "#ff005f",
        "#ff0087",
        "#ff00af",
        "#ff00d7",
        "#ff00ff",
        "#ff5f00",
        "#ff5f5f",
        "#ff5f87",
        "#ff5faf",
        "#ff5fd7",
        "#ff5fff",
        "#ff8700",
        "#ff875f",
        "#ff8787",
        "#ff87af",
        "#ff87d7",
        "#ff87ff",
        "#ffaf00",
        "#ffaf5f",
        "#ffaf87",
        "#ffafaf",
        "#ffafd7",
        "#ffafff",
        "#ffd700",
        "#ffd75f",
        "#ffd787",
        "#ffd7af",
        "#ffd7d7",
        "#ffd7ff",
        "#ffff00",
        "#ffff5f",
        "#ffff87",
        "#ffffaf",
        "#ffffd7",
        "#ffffff",
        "#080808",
        "#121212",
        "#1c1c1c",
        "#262626",
        "#303030",
        "#3a3a3a",
        "#444444",
        "#4e4e4e",
        "#585858",
        "#626262",
        "#6c6c6c",
        "#767676",
        "#808080",
        "#8a8a8a",
        "#949494",
        "#9e9e9e",
        "#a8a8a8",
        "#b2b2b2",
        "#bcbcbc",
        "#c6c6c6",
        "#d0d0d0",
        "#dadada",
        "#e4e4e4",
        "#eeeeee",
    )

    def history(self,event):
        print("Event: ",event)
        if event.keysym=="Up":
            self.historyidx+=1
            if self.historyidx>=len(self.historylst):
                self.historyidx=0
        elif event.keysym=="Down":
            self.historyidx-=1
            if self.historyidx<0:
                self.historyidx=len(self.historylst)-1
        if (self.historyidx>=0 and self.historyidx<len(self.historylst)):
            self.mytext.set(self.historylst[self.historyidx])

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bottom = Frame(self, bg="LightGray")
        self.bottom.pack(side=BOTTOM, fill=X)
        self.sendbtn = Button(self.bottom, text="Snd", command=self.doSend)
        self.mytext = StringVar()
        self.sendEntry = Entry(self.bottom, textvariable=self.mytext)
        self.sendbtn.pack(side=RIGHT)
        self.sendEntry.pack(fill=X, expand=True)
        self.sendEntry.bind("<Return>",self.doSendEvent)
        self.sendEntry.bind("<Up>", self.history)
        self.sendEntry.bind("<Down>", self.history)
        self.textbox.bind("<Double-Button-1>",self.dblClick)
        self.textbox.configure(exportselection=False,inactiveselectbackground=self.textbox["selectbackground"])

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.iscsi = False
        self.isesc = False
        self.parameters = []
        self.currentparam = ""
        self.ResetStyle()
        self.output=""
        self.currenttag=""
        self.taglist = []
        self.settag()
        self.listenthread=None
        self.connectString=""
        self.stopping=False
        self.lastline=""
        self.capturestr=""
        self.capturemode=0
        self.external_edit=""
        self.verbcollect=''
        self.onExamineLine=None
        self.upload=""
        self.historylst=[]
        self.historyidx=0
        ifile=SettingsDialog.getConfig()
        if ifile.has_section("history"):
            for (key,value) in ifile.items("history"):
                if key.isnumeric():
                    self.historylst.append(value)

    def dblClick(self,event:Event):
        """Respond to double click"""
        self.gotoError(self.textbox)

    def settag(self):
        tagname = self.myfontcolor + ";" + self.mycolor
        if (tagname!=self.currenttag):
            self.flush()
        if not (tagname in self.taglist):
            cfg = {"background": self.mycolor, "foreground": self.myfontcolor}
#            if (self.mycolor=="#000000" or self.mycolor=="black"):
#                del cfg["background"]
            self.textbox.tag_config(tagname, cfg)
            self.taglist.append(tagname)
            self.textbox.tag_raise(SEL) # Make sure selection overrides.
        self.currenttag = tagname
    
    def parseVerb(self,value):
        """Return (obj,verb), or False if not valid."""
        if value.startswith('@'):
             value=parse(value)[1]
        (obj,value)=parsesep(value,':')
        (verb,value)=parse(value)
        if verb.startswith('"'):
             verb=getsepfield(verb,1,'"')
        i=verb.find("*")
        if (i>=0):
            verb=verb[0:i]
        if (verb!='') and (obj!=''):
            return (obj,verb)
        return False

    def addtext(self, msg):
        for c in msg:
            self.addchar(c)
        self.textbox.see("end")

    def rgb(self, r, g, b):
        return "#%02x%02x%02x" % (r, g, b)
    
    def flush(self):
        if self.output!="":
            self.textbox.insert("end",self.output,self.currenttag)
            self.output=""
            self.textbox.see("end")

    def saveSettings(self):
        ifile=SettingsDialog.getConfig()
        if (ifile.has_section("history")):
            ifile.remove_section("history")
        ifile.add_section("history")
        h=ifile["history"]
        for i in range(10):
            if i>=len(self.historylst):
                break
            h[str(i)]=self.historylst[i]
        ifile["settings"]['LastDump']=self.dumpobject
        SettingsDialog.saveConfig(ifile)

    def ResetStyle(self):
        self.isbold = False
        self.isunderline = False
        self.isitalic = False
        self.isstrikeout = False
        self.myfontcolor = "#c0c0c0"
        self.mycolor = "#000000"

    def setbold(self, bold):
        if bold != self.isbold:
            if bold:
                ix = self.ColorTable.index(self.myfontcolor)
                if ix >= 0:
                    self.myfontcolor = self.ColorTableBold[ix]
                else:
                    self.myfontcolor = "#ffffff"
            else:
                ix = self.ColorTableBold.index(self.myfontcolor)
                if ix >= 0:
                    self.myfontcolor = self.ColorTable[ix]
                else:
                    self.myfontcolor = "#c0c0c0"
        self.isbold = bold

    def setattributes(self):
        extended = 0
        secondary = 0
        back = False
        xrgb = [0, 0, 0]
        for n in self.parameters:
            if extended > 0:
                if extended == 1:
                    secondary = n
                elif secondary == 5:  # X256
                    if back:
                        self.mycolor = self.ColorX256[n & 0xFF]
                    else:
                        self.myfontcolor = self.ColorX256[n & 0xFF]
                    extended = 0
                    continue
                elif secondary == 2:
                    xrgb[extended - 2] = n & 0xFF
                    if extended == 4:
                        if back:
                            self.mycolor = self.rgb(xrgb[0], xrgb[1], xrgb[2])
                        else:
                            self.myfontcolor = self.rgb(xrgb[0], xrgb[1], xrgb[2])
                        extended = 0
                        continue
                extended += 1
                continue
            if n == 0:
                self.ResetStyle()
            elif n == 1:
                self.setbold(True)
            elif n == 2 or n == 22:
                self.setbold(False)
            elif n == 3:
                self.isitalic = True
            elif n == 4:
                self.isunderline = True
            elif n == 9:
                self.isstrikeout = True
            elif n >= 30 and n <= 37:
                if self.isbold:
                    self.myfontcolor = self.ColorTableBold[n % 10]
                else:
                    self.myfontcolor = self.ColorTable[n % 10]
            elif n == 38:
                back = False
                extended = 1
            elif n >= 40 and n <= 47:
                if self.isbold:
                    self.mycolor = self.ColorTableBold[n % 10]
                else:
                    self.mycolor = self.ColorTable[n % 10]
            elif n == 48:
                back = True
                extended = 1
        # print("fg=",self.myfontcolor," bg=",self.mycolor)
        self.settag()

    def addchar(self, c: str):
        if self.isesc:
            if self.iscsi:
                if c.isalpha():
                    self.iscsi = False
                    self.isesc = False
                    self.parameters.append(int(self.currentparam))
                    self.currentparam = ""
                    if c == "m":
                        self.setattributes()
                elif c.isnumeric():
                    self.currentparam += c
                elif c == ";":
                    self.parameters.append(int(self.currentparam))
                    self.currentparam = ""
            elif c == "[":
                self.iscsi = True
                self.parameters = []
                self.currentparam = ""
        elif c == "\x1b":
            self.isesc = True
        else:
            self.isesc = False
            self.iscsi = False
            self.currentparam = ""
            if self.capturemode!=1:
                self.output+=c
        if (c=="\n"):
            self.processLine()
            self.lastline=""
        elif c!="\r":
            self.lastline+=c

    def processLine(self):
        if self.capturemode==0:
            if self.lastline.startswith("#$# edit"):
                self.external_edit=self.lastline
                self.capturemode=1
                self.capturestr=""
            elif self.onExamineLine:
                self.onExamineLine(self.lastline)
        elif self.capturemode==1:
            if self.capturestr!="":
                self.capturestr+="\n"
            self.capturestr+=self.lastline
            if (self.lastline=="."):
                self.capturemode=0
                (name,upload)=self.parseExternal()
                self.openEdit(name,upload,self.capturestr)

    def selectError(self,obj:str,verb:str,lno:int)->bool:
        tabs=self.pages.tabs()
        for i in range(2,len(tabs)):
            w=self.pages.nametowidget(tabs[i])
            if (isinstance(w,ScrollText)):
                re:Text=w.textbox
                lines=re.get("1.0","end").splitlines()
                if (len(lines)>0 and (lines[0]+" ").lower().find(obj+':'+verb+' ')>=0):
                    self.pages.select(i)
                    start=str(lno+1)+'.0'
                    end=str(lno+1)+".end"
                    re.see(start)
                    re.focus_set()
                    re.tag_add(SEL,start,end)
                    #pagesChange(self);
                    return True
        return False
    
    def findVerbHelp(self,obj:str,verb:str)->str:
        """Extract help line from verb"""
        re=self.findVerbEditor(obj,verb)
        result='No Help'
        if not(re):
            return result
        lines=re.lines()
        if len(lines)>=2:
            s=lines[1]
            if (s.startswith('"')):
                s=s[1:]
                s=s[0:len(s)-2]
                result=s
        return result

    def findVerbEditor(self,obj:str, verb:str):
        searchverb=getsepfield(verb,0,'*') # Handle wildcards.
        for i in self.pages.tabs():
            w=self.pages.nametowidget(i)
            if isinstance(w,ScrollText):
                re:ScrollText=w
                if (re.tabtype!=1):
                    continue
                s=re.textbox.get("1.0","1.end")
                ret=self.parseVerb(s)
                if (ret):
                    (aobj,averb)=ret
                    if ansiSameText(aobj,obj) and ansiSameText(averb,searchverb):
                        return re
        return None
    
    def findPage(self,title:str):
        """Return widget matching title, or None if not found."""
        for i in self.pages.tabs():
            tabname=self.pages.tab(i,"text")
            if tabname==title:
                return self.pages.nametowidget(i)
        return None

    def currentEditor(self)->Text:
        w=self.currentPage()
        if isinstance(w,ScrollText):
            return w.textbox
        return None

    def currentPage(self)->ScrollText:
        w=self.nametowidget(self.pages.select())
        if isinstance(w,ScrollText):
            return w
        return None
    
    def currentTest(self)->Entry:
        w=self.currentPage()
        if isinstance(w,CodeText):
            return w.test
        return None

    def addtarget(self,dest:Text, line:str):
        dest.insert("end",line+"\n")
        dest.see("end")

    def doCheckTest(self,line:str):
        """Check for stack trace messages"""
        if self.getstack: 
            self.addtarget(self.stack,line)
        # #540:test (this == #540), line 5:  Type mismatch (expected integer; got float)
        # #151:+attacks, line 9:  Verb not found: #548:energy_cast()
        # #151:+deploy deploy, line 28:  Range error
        if line.startswith('#') and line.find(', line')>=0:
            startline=line
            (prog,line)=parsesep(line,',')
            line=parse(line)[1] # Skip "line"
            (lno,line)=parsesep(line,':')
            (obj,verb)=self.parseVerb(prog)    #Should strip out trailing defs.
            error=line
            self.getstack=True
            self.stack.delete("1.0","end")
            self.addtarget(self.stack,'Stack')
            self.addtarget(self.stack,error)
            self.addtarget(self.stack,obj+':'+verb+', line '+lno)
            self.setstackvisible(True)
            self.errorverb=''
            if not self.selectError(obj,verb,int(lno)):
                self.errorverb=verb
                self.errorobj=obj
                self.lastlno=int(lno)
        elif (line=='(End of traceback)'):
            self.getstack=False
            if self.errorverb!='':
                self.findVerb(self.errorobj,self.errorverb,self.lastlno)
            self.errorverb=''
    
    def doCheckCompile(self,line:str)->None:
        """Check that verb has compiled"""
#        var lno,x,n:Integer; s1,s2:String;  e:TEdit;
#        adddebug(line);
        if (line.startswith('Line ')):
            (s1,line)=parsesep(line,':');
            lno=atol(s1[4:])
            self.stack.delete("1.0","end")
            self.stack.insert("1.0","Compile Error\n"+line)
            self.setstackvisible(True)
            re=self.currentEditor()
            ix=str(lno+1)+".0"
            re.mark_set(INSERT,ix)
            re.see(ix)
            re.tag_add(SEL,ix,str(lno+1)+".end")
            re.focus_set()
        elif line=='Verb not programmed.':
            self.onExamineLine=self.doCheckTest
        elif line=='Verb programmed.':
            self.onExamineLine=self.doCheckTest
            if not self.checkSendTest():
                self.showmessage(line)
    
    def checkSendTest(self)->bool:
        e=self.currentTest()
        if e and (e.get()!=""):
            self.sendCmd(e.get())
            self.testtab=self.pages.select()
            self.getstack=False
            ifile=SettingsDialog.getConfig()
            ifile["test"][self.currentPage().testName()]=e.get()
            SettingsDialog.saveConfig(ifile)
            self.onExamineLine=self.doCheckTest
            self.pages.select(self)
            return True
        else:
            return False

    def addTab(self,caption:str,text:str,tabtype:int):
        t=CodeText(self.pages,tabtype,background="black",foreground="white",font=("Courier",self.fontsize,"bold"),insertbackground="white")
        self.pages.add(t,text=caption)
        t.tw=self
        t.setText(text)
        t.caption=caption
        t.tabtype=tabtype
        ifile=SettingsDialog.getConfig()
        t.testvar.set(ifile["test"].get(t.testName(),""))
        return t
    
    def doRefresh(self,verbstr:str)->None:
        """Reload a verb"""
        try:
            (verb,obj)=self.parseVerb(verbstr)
            self.fetchVerb(verb,obj)
        except:
            pass

    def doRefreshProperty(self,propstr:str)->None:
        """Reload a property"""
        try:
            (obj,prop)=propstr.split(".")
        except:
            return
        self.sendCmd(";"+propstr)
        self.lastobj=obj
        self.lastproperty=propstr
        self.onExamineLine=self.doCheckProperty

    def doCheckProperty(self,line:str):
        """Examine line for property detail."""
        if not line.startswith('=> '):
            self.showmessage(line)
        else:
            line=line[3:]
            self.proplist[self.lastproperty]=line
            self.updateProperties(False)
            self.editProp(self.lastproperty)
            self.checkName(self.lastobj)
        self.onExamineLine=self.doCheckTest
        
    def doCheckVerb(self, line:str):
        if (line=='***finished***'):
            self.onExamineLine=self.doCheckTest
            t=self.verbcollect.splitlines()
            t.append(".")
            prog=t[0]
            if (prog=='That object does not define that verb.'):
                messagebox.showwarning("MooCoderPy",'Verb not found.')
                return
            for i in range(len(t)):
                if t[i].endswith('[normal]'): # Stupid ansi is stupid.
                    s=t[i]
                    t[i]=s[0:len(s)-len('[normal]')]
            progline=prog
            (obj,prog)=parsesep(prog,':')
            args=prog
            if (args.startswith('"')):
                args=args.replace('"','').strip()
            (verb,prog)=parse(prog)
            if (verb.startswith('"')):
                verb=getsepfield(verb,1,'"')
            i=verb.find('*')
            if (i>=0):
                verb=verb[0:i]
            t[0]='@program '+obj+':'+verb
            if self.selectError(obj,verb,self.lastlno):
                re=self.currentEditor()
                lastix=re.index(INSERT)
                re.delete("1.0","end")
                re.insert("1.0","\n".join(t))
                if (self.lastlno>0):
                    re.see(str(self.lastlno+1)+".0")
                else:
                    re.mark_set(INSERT,lastix)
                    re.see(lastix)
                try:
                    self.currentPage().highlight()
                except:
                    pass
            else:
                self.addTab(obj+':'+verb,"\n".join(t),CodeText.MODE_CODE)
                self.selectError(obj,verb,self.lastlno)
            self.lastlno=0
            self.checkName(obj)
            tag=obj+':'+verb
            self.arglist[tag]=args
            if not(tag in self.verblist):
                self.verblist.append(tag)
            try:                
                pg=self.currentPage().setLabel(progline)
            except:
                pass
            self.updateVerbs()
        else:
            self.verbcollect+=line+"\n"
    
    def findLocalEdit(self,name:str)->CodeText:
        """Find the local editor by name"""
        for tab in self.pages.tabs():
            w=self.pages.nametowidget(tab)
            if (isinstance(w,CodeText) and w.mode==CodeText.MODE_EDIT):
                if (w.caption==name):
                    return w
        return None

    def openEdit(self,name:str, upload:str, text:str):
        """Find and open a tab for a local edit"""
        re=self.findLocalEdit(name)
        if re:
            re.setText(text)
        else:
            re=self.addTab(name,text,CodeText.MODE_EDIT)
        re.upload=upload
        re.syntax=(upload.find("@program")>=0)
        re.setLabel(upload)
        re.highlight()
        self.pages.select(re)
        
    def checkName(self,obj:str)->None:
        """Check that we know the name of an object."""
        if not(obj in self.namelist):
            self.sendCmd(';'+obj+'.name')
            self.onExamineLine=self.doCheckName
        self.lastobj=obj
    
    def doCheckName(self,line:str):
        """Examine stream for name of object."""
        if line.lower().find('***finished***')>=0:
            return # Ignore trailing stuff.
        if line.startswith('=> 0'):
            return # tailing result.
        self.onExamineLine=self.doCheckTest
        if not(line.startswith('=>')):
            self.addln('Name not found.')
            return
        aname=getsepfield(line,1,'"')
        self.namelist[self.lastobj]=aname
        self.updateVerbs()
        self.updateProperties(False)
    
    def updateVerbs(self)->None:
        """Update Verb list window"""
#        var nd:TListItem; s:String; obj,verb:String;
#            oldverb,oldobj:String; i:Integer;
#        lvVerbs.Items.BeginUpdate;
        oldverb=''
        nd=self.lvVerbs.item(self.lvVerbs.focus())
        if nd["text"]!="":
            oldobj=nd["text"].lower()
            oldverb=nd["values"][1].lower()
        for i in self.lvVerbs.get_children(): #Clear list
            self.lvVerbs.delete(i)
        self.verblist.sort() # Todo... make cleverer.
        for s in self.verblist:
            obj=getsepfield(s,0,':')
            verb=getsepfield(s,1,':')
            name=self.namelist[obj] if obj in self.namelist else obj
            args=self.arglist[s] if s in self.arglist else ""
            values=(name,verb,args,self.findVerbHelp(obj,verb))
            self.lvVerbs.insert("","end",text=obj,values=values)
        self.fitListContents(self.lvVerbs)
        if oldverb!="":
            for i in self.lvVerbs.get_children():
                nd=self.lvVerbs.item(i)
                if nd["text"].lower()==oldobj and nd["values"][1].lower()==oldverb:
                    self.lvVerbs.selection_set(i)
                    self.lvVerbs.see(i)
                    break

    def updateProperties(self,focus=True):
        """Update Property List"""
        oldprop=""
        nd=self.lvProperties.item(self.lvProperties.focus())
        if nd["text"]!="":
            oldobj=nd["text"].lower()
            oldprop=nd["values"][1].lower()
        for item in self.lvProperties.get_children():
            self.lvProperties.delete(item)
        for k in sorted(self.proplist.keys()):
            v=self.proplist[k]
            (obj,prop)=k.split(".")
            name=self.namelist[obj] if obj in self.namelist else obj
            self.lvProperties.insert("",END,text=obj, values=(name,prop,v))
        self.fitListContents(self.lvProperties)
        if (focus):
            self.pages.select(self.lvProperties.winfo_parent())
        if oldprop!="":
            for i in self.lvProperties.get_children():
                nd=self.lvProperties.item(i)
                if nd["text"].lower()==oldobj and nd["values"][1].lower()==oldprop:
                    self.lvProperties.selection_set(i)
                    self.lvProperties.see(i)
                    break

    def fitListContents(self,alist:ttk.Treeview):
        cols=alist.cget("columns")
        colnames=["#0"]+list(cols)
        widths=[0 for x in colnames]
        for i in range(len(colnames)):
            n=colnames[i]
            widths[i]=max(widths[i],self.normalfont.measure(alist.heading(n,"text")))
        for iid in alist.get_children():
            line=alist.item(iid)
            widths[0]=max(widths[0],self.normalfont.measure(line["text"]))
            v=line["values"]
            for i in range(1,min(len(colnames),len(v)+1)):
                widths[i]=max(widths[i],self.normalfont.measure(v[i-1]))
        spacing=self.normalfont.measure("  ")
        widths[0]+=spacing*2 # Guessing at present: allow space for image
        for i in range(len(colnames)):
            alist.column(colnames[i],width=widths[i]+spacing)

    def parseExternal(self):
        try:
            t=self.external_edit.split(" name: ")[1]
            tt=t.split(" upload: ")
            return (tt[0].strip(),tt[1].strip())
        except:
            return("","")
    
    def doupdate(self,upload,text:str):
        if upload=="":
            messagebox.showwarning("Send Update","Not in @edit mode")
            return False
        self.sendCmd(upload)
        self.sendCmd(text)
        self.after(500,self.sendtext,"Update complete\n")
        e=self.currentTest()
        if e and (e.get()!=""):
            test=e.get()
            self.testtab=self.pages.select()
            self.getstack=False
            self.onExamineLine=self.doCheckTest
            ifile=SettingsDialog.getConfig()
            ifile["test"][self.currentPage().testName()]=e.get()
            SettingsDialog.saveConfig(ifile)
            self.after(1000,self.sendCmd,test)
        self.pages.select(self)
        return True
    
    def docompile(self,page:ScrollText):
        if not(isinstance(page, CodeText)):
            return
        if page.mode==CodeText.MODE_EDIT:
            self.doupdate(page.upload,page.textbox.get("1.0","end"))
        elif page.mode==CodeText.MODE_PROPERTY:
            text=page.getText()
            if len(text)>0 and not(text[0] in "{["): # Not formatted as a list. Treat as list of strings.
                text=text[:-1] if  text.endswith("\n") else text
                text=text.split("\n")
                text=[line.replace('"',r'\"') for line in text]
                value='{"'+'","'.join(text)+'"}'
            else:
                value=splitlist.joinList(page.getText())
            self.sendCmd(page.upload+"="+value)
            self.proplist[page.caption]=value
            self.updateProperties(False)
            self.onExamineLine=self.doCheckUpdateProperty
        else:
            self.sendCmd(page.textbox.get("1.0","end"))
            self.onExamineLine=self.doCheckCompile

    def doSend(self):
        s = self.mytext.get()
        print("Send:", s)
        self.mytext.set("")
        if self.socket != None:
            self.socket.send((s + "\n").encode("utf-8"))
            self.historylst.insert(0,s)
            self.historyidx=0

    def doSendEvent(self,event):
        self.doSend()
        
    def doConnect(self, server, port):
        self.disconnect()
        self.sendtext("Connecting to %s %d\n" % (server,port))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        self.stopping=False
        self.listenthread = threading.Thread(target=self.doListen)
        self.listenthread.start()
        if (self.connectString!=""):
            self.after(1000,self.sendCmd,self.connectString)
        print("Connected")
    
    def showmessage(self,msg):
        messagebox.showinfo("MooCoderPy",msg)

    def loadVerb(self,verbdef):
        v=self.parseVerb(verbdef)
        if not v:
            self.showmessage("Invalid Verb Syntax")
            return
        (obj,verb)=v
        self.findVerb(obj,verb,0)

    def findVerb(self,obj:str,verb:str, lno:int):
        self.lastlno=lno
        if (obj=='#-1'):
            return # Not a real verb.
        #if not(self.selectError(obj,verb,lno)):
        self.fetchVerb(obj,verb)
    
    def fetchVerb(self,obj,verb):
        self.sendCmd('@list '+obj+':'+verb+' without numbers')
        self.sendCmd(';player:tell("***finished***")')
        self.verbcollect=''
        self.onExamineLine=self.doCheckVerb

    def sendCmd(self,cmd):
        buf=(cmd+"\n").encode("utf-8")
        self.socket.sendall(buf)
        

    def doConnectStr(self):
        if (self.connectString!=""):
            self.sendCmd(self.connectString)

    def disconnect(self):
        print("Disconnecting...")
        try:
            self.stopping=True
            self.socket.close()
            if (self.listenthread!=None):
                threading.join(self.listenthread)
            self.listenthread=None
        except:
            pass

    def doListen(self):
        try:
            while True:
                (readlist,writelist,exceptlist)=select.select([self.socket],[],[self.socket],1) 
                if self.stopping:
                    print("Listen thread stopping.")
                    break
                if self.socket in exceptlist:
                    print("Exception found.")
                    break
                if self.socket in readlist:
                    b = self.socket.recv(2048)
                    if len(b)==0: # Socket probably closed.
                        self.sendtext("\nDisconnected\n")
                        break
                    self.sendtext(b.decode("utf-8"))
        except Exception as err:
            print("Connection error: {0}".format(err))
            try:
                self.sendtext("Connection error: {0}".format(err))
            except:
                pass
        print("Listen thread done.")
        self.listenthread=None

    def getVerbs(self,event:Event=None):
        s=simpledialog.askstring('Verbs','Load Verb list for object:', initialvalue=self.dumpobject)
        if (s):
            self.dumpobject=s
            self.sendCmd('@verbs '+self.dumpobject)
            self.onExamineLine=self.doCheckVerbs

    def getProperties(self,event:Event=None):
        s=simpledialog.askstring('Prpperties','Load Property list for object:', initialvalue=self.dumpobject)
        if (s):
            self.dumpobject=s
            self.sendCmd('@dump '+self.dumpobject+" with noverbs")
            self.onExamineLine=self.doCheckProperties

    def doCheckProperties(self,line:str):
        # ;;#151.("rank_chart") = {"-", "F", "D", "C", "B", "A", "S", "SS", "SSS", "SSSS", "SSSSS"}
        if line.startswith(";;#"):
            (k,v)=parsesep(line," = ")
            k=re.sub(r'["();]',"",k)
            self.proplist[k]=v
            self.lastobj=getsepfield(k,0,".")
            p=self.findPage(k)
            if p:
                p.setText(splitlist.splitList2(v))
        elif "***finished***" in line:
            self.onExamineLine=self.doCheckTest
            self.updateProperties()
            self.checkName(self.lastobj)

    def doCheckVerbs(self,line:str)->None:
        """Fetch verbs for an object"""
        self.onExamineLine=self.doCheckTest
        if not(line.lower().startswith(';verb')):
            messagebox.showerror("MooCoderPy","Verb not found.\n"+line)
            return
        line=parsesep(line,'(')[1]
        (obj,line)=parsesep(line,')')
        line=parsesep(line,'{')[1]
        line=line.strip()
        if line.endswith('}'):
            line=line[0:len(line)-1]
        self.verblist=[x for x in self.verblist if not(x.startswith(obj+":"))]    
        t=line.split(",")
        for s1 in t:
            s=s1.strip()[1:]
            s=s[0:len(s)-1]
            verb=getfield(s,0)
            self.verblist.append(obj+':'+verb);
        self.checkName(obj)
        self.updateVerbs()
        self.pages.select(self.lvVerbs.winfo_parent())
    
    def clearProject(self):
        """Close all open tabs and clear verb list"""
        if messagebox.askyesno("MooCoderPy","Clear this project?"):
            tabs=list(self.pages.tabs())
            tabs.reverse()
            for tab in tabs:
                x=self.pages.nametowidget(tab)
                if (hasattr(x,"tabtype") and x.tabtype==1):
                    x.close()
            self.verblist.clear()
            self.namelist.clear()
            self.arglist.clear()
            self.proplist.clear()
            self.updateVerbs()
            self.updateProperties()
            self.pages.select(self)

    def gotoError(self,text:Text):
        line=text.get(INSERT+" linestart",INSERT+" lineend").strip()
        if line.startswith('... called from'):
            line=line[line.find("#"):]   # Strip off leading stuff.
            (prog,line)=parsesep(line,',')
            line=parse(line)[1]
            lno=atol(line)
            v=self.parseVerb(prog)
            if v:
                self.findVerb(v[0],v[1],lno)
        elif line.startswith('#') and (', line' in line):
            (prog,line)=parsesep(line,',')
            line=parse(line)[1] # Skip "line"
            (tmp,line)=parsesep(line,':')
            lno=atol(tmp)
            v=self.parseVerb(prog)     # Should strip out trailing defs.
            if v:
                (obj,verb)=v
                if not self.selectError(obj,verb,lno):
                    self.fetchVerb(obj,verb)
    
    def editProp(self,propname:str):
        """Edit a property"""
        try:
            (obj,prop)=propname.split(".")
        except:
            messagebox.showwarning("MooCoderPy","Invalid property format.")
            return
        if not(propname in self.proplist):
            messagebox.showwarning("MooCoderPy","Unknown Property.")
            return
        value=self.proplist[propname]
        if value.startswith("[") or value.startswith("{"):
            myedit=self.findPage(propname)
            if not(myedit):
                myedit=self.addTab(propname,"",CodeText.MODE_PROPERTY)
            myedit.syntax=True
            myedit.setText(splitlist.splitList2(value))
            myedit.upload=";;"+propname
            myedit.setLabel(myedit.upload)
            self.pages.select(myedit)
            return
        newvalue=mydialogs.askstring("Edit "+propname,"New Value",initialvalue=value,width=80)
        if (not newvalue):
            return
        self.proplist[propname]=newvalue
        self.sendCmd(";;"+propname+"="+newvalue)
        self.updateProperties()
        self.onExamineLine=self.doCheckUpdateProperty
    
    def doCheckUpdateProperty(self,line:str):
        """Check on the results of an edit prop"""
        if not line.startswith('=> 0'):
            self.showmessage(line)
        else:
            if self.checkSendTest():
                return
        self.onExamineLine=self.doCheckTest

if __name__=="__main__":
    root=Tk()
    tw=TerminalWindow(root)
    tw.pack(fill=BOTH, expand=True)
    tw.sendtext("Mary had a little lamb.")
    root.mainloop()

