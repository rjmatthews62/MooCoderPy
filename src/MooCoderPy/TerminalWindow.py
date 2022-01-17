from ScrollText import *
from tkinter import *
from tkinter import messagebox
import socket, threading,select
import SettingsDialog


class TerminalWindow(ScrollText):
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
        self.sendcmd = Entry(self.bottom, textvariable=self.mytext)
        self.sendbtn.pack(side=RIGHT)
        self.sendcmd.pack(fill=X, expand=True)
        self.sendcmd.bind("<Return>",self.doSendEvent)
        self.sendcmd.bind("<Up>", self.history)
        self.sendcmd.bind("<Down>", self.history)
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
        self.capturefunc=None
        self.external_edit=""
        self.historylst=[]
        self.historyidx=0
        ifile=SettingsDialog.getConfig()
        if ifile.has_section("history"):
            for (key,value) in ifile.items("history"):
                if key.isnumeric():
                    self.historylst.append(value)

    def settag(self):
        tagname = self.myfontcolor + ";" + self.mycolor
        if (tagname!=self.currenttag):
            self.flush()
        if not (tagname in self.taglist):
            cfg = {"background": self.mycolor, "foreground": self.myfontcolor}
            self.textbox.tag_config(tagname, cfg)
            self.taglist.append(tagname)
        self.currenttag = tagname
    
    def parseVerb(self,verb):
        if value.StartsWith('@') then parse(value);
        obj:=parseSepFIeld(value,':');
        verb:=parse(value);
        if (verb.StartsWith('"')) then verb:=GetSepField(verb,2,'"');
        i:=pos('*',verb);
        if (i>0) then verb:=copy(verb,1,i-1);
        result:=(verb<>'') and (obj<>'');


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
        elif self.capturemode==1:
            if self.capturestr!="":
                self.capturestr+="\n"
            self.capturestr+=self.lastline
            if (self.lastline=="."):
                self.capturemode=0
                (name,upload)=self.parseExternal()
                self.capturefunc(self.capturestr,name)

    def parseExternal(self):
        try:
            t=self.external_edit.split(" name: ")[1]
            tt=t.split(" upload: ")
            return (tt[0].strip(),tt[1].strip())
        except:
            return("","")
    
    def doupdate(self,text:str):
        if self.external_edit=="":
            messagebox.showwarning("Send Update","Not in @edit mode")
            return False
        upload=self.parseExternal()[1]    
        self.sendCmd(upload)
        self.sendCmd(text)
        self.after(500,self.sendtext,"Update complete\n")
        return True

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

    def loadVerb(self,verbdef):
        pass
    
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
                (readlist,writelist,exceptlist)=select.select([self.socket],[],[],1) 
                if self.stopping:
                    print("Listen thread stopping.")
                    break
                if self.socket in readlist:
                    b = self.socket.recv(128)
                    self.sendtext(b.decode("utf-8"))
        except Exception as err:
            print("Connection error: {0}".format(err))
            try:
                self.sendtext("Connection error: {0}".format(err))
            except:
                pass
