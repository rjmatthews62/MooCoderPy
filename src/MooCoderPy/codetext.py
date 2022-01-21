from tkinter import simpledialog
from ScrollText import *
from tkinter import *
from time import *
from findreplacedialog import *

class CodeText(ScrollText):
    bottom:Frame
    test:Entry
    caption:str
    testvar:StringVar
    modifying=False
    lastfind:str=""

    KEYWORDLIST=('if','then','else','elseif','for',
           'while','endfor','endwhile','endif',
           'try','except','endtry','break','continue')
    
    COLORLIST=("white","lawn green","cyan","magenta","orange","yellow")

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bottom = Frame(self, bg="LightGray")
        self.bottom.pack(side=BOTTOM, fill=X)
        self.posvar=StringVar()
        self.posvar.set("000.000")
        poslbl=Label(self.bottom,textvariable=self.posvar)
        poslbl.pack(side=LEFT)
        lbl=Label(self.bottom,text="Test ",font="Arial 12")
        lbl.pack(side=LEFT)
        self.testvar=StringVar()
        self.test=Entry(self.bottom,width=60,font="Arial 12",textvariable=self.testvar)
        self.test.pack(side=LEFT,fill=X,expand=True)
        self.setcolors()
        self.textbox.bind("<ButtonRelease>",self.trackLocation)
        self.textbox.bind("<KeyRelease>",self.trackLocation)
        self.textbox.bind("<Enter>",self.trackLocation)
        self.bind_all("<Control-Key-G>",self.gotoLine)
        self.bind_all("<Control-Key-g>",self.gotoLine)
        self.textbox.bind_all("<<Modified>>",self.modified)
        self.bind_all("<Control-Key-F>",self.find)
        self.bind_all("<Control-Key-f>",self.find)
    
    def currentLine(self)->int:
        """Return currently selected line no"""
        return int(self.textbox.index(INSERT).split(".")[0])

    def modified(self, event):
        if not(self.modifying): # Avoid recursion
            try:
                self.modifying=True
                lno=self.currentLine()
                self.syntaxHighlight(lno-1)
                self.syntaxHighlight(lno)
                self.syntaxHighlight(lno+1)
                # Set 'modified' to 0.  This will also trigger the <<Modified>>
                # virtual event which is why we need the sentinel.
                self.textbox.edit_modified(False)
            finally:
                # Clean the sentinel.
                self.modifying = False

    def trackLocation(self,event=None):
        """Update Cursor Location"""
        loc=self.textbox.index(INSERT)
        (x,y)=loc.split(".")
        s="%4d:%3d" % (int(x)-1,int(y))
        self.posvar.set(s)
        if (self.lastfind!="" and self.lastfind!=loc):
            self.textbox.tag_remove("found","1.0",END)

    def gotoLine(self,event=None):
        """Ask User to go to line no"""
        lno=int(self.textbox.index(CURRENT).split(".")[0])-1
        lno=simpledialog.askinteger("MooCoderPy","Go to Line No:",initialvalue=lno)
        if lno==None:
            return
        lno=min(max(lno,0),self.lastLine())
        mark="%d.0"%(lno+1)
        self.textbox.mark_set(INSERT,mark)
        self.textbox.see(mark)
    
    def find(self,event=None):
        """Find text in editor"""
        FindReplaceDialog(self,"Find...")
        if findReplaceSettings.go:
            if findReplaceSettings.backward:
                ix=self.textbox.index(INSERT)+"-1 chars" 
                found=self.textbox.search(findReplaceSettings.search, "1.0",ix,backwards=True,nocase=not(findReplaceSettings.caseSensitive))
                if not(found):
                    found=self.textbox.search(findReplaceSettings.search, END,ix, backwards=True,nocase=not(findReplaceSettings.caseSensitive))
            else:            
                ix=self.textbox.index(INSERT)+"+1 chars" 
                found=self.textbox.search(findReplaceSettings.search, ix,END,nocase=not(findReplaceSettings.caseSensitive))
                if not(found):
                    found=self.textbox.search(findReplaceSettings.search, "1.0",ix,nocase=not(findReplaceSettings.caseSensitive))
            if found:
                self.textbox.mark_set(INSERT,found)
                self.textbox.see(found)
                self.textbox.focus_set()
                self.textbox.tag_remove("found","1.0",END)
                self.textbox.tag_add("found",found,found+"+"+str(len(findReplaceSettings.search))+" chars")
                self.textbox.tag_configure("found",background="blue",foreground="white")
                self.lastfind=found

    def testName(self)->str:
        return self.caption.lower().replace("*","").replace("=","_").replace("#","").replace(":","_")
    
    def setcolors(self):
        """Initialize colour tags"""
        for col in self.COLORLIST:
            self.textbox.tag_configure(col,foreground=col)

    def lastLine(self)->int:
        """Highest line no of edit"""
        return int(self.textbox.index("end").split(".")[0])

    def getLine(self,lno:int)->str:
        """Return a selected line number."""
        return self.textbox.get(str(lno)+".0",str(lno)+".end")
    
    def cleartags(self,lno:int)->None:
        """Remove tags from a line"""
        for tag in self.COLORLIST:
            self.textbox.tag_remove(tag,str(lno)+".0",str(lno)+".end")
    
    def highlight(self):
        """Syntax highlight all lines"""
        for i in range(1,self.lastLine()+1):
            self.syntaxHighlight(i)
        self.trackLocation()

    def syntaxHighlight(self, lno:int):
        line=""
        x:int=0
        
        def nextWord()->str:
            nonlocal x
            result=''
            while x<len(line):
                c=line[x]
                if c in ' "()[]+-/\\*:.\{\}': 
                    if result=="":
                        result=c
                        x+=1
                    return result
                result+=c
                x+=1
            return result
        
        if (lno>=self.lastLine()) or (lno<1):
              return
        self.cleartags(lno)
        if lno==0: return # Leave programming line alone.
        line=self.getLine(lno)

        isquote=False
        isescaped=False
        isverb=False
        isproperty=True
        wordonly=False
        x=0
        color="white"
        nextcolor="white"
        while (x<len(line)-1):
            startx=x
            myword=nextWord()
            if (isescaped):
                isescaped=False
            elif isquote:
                color="yellow"
                if myword=="\\":
                    isescaped=True
                    color="orange"
                elif myword=='"':
                    isquote=False
                    wordonly=True
            elif (myword=='"'):
                isquote=True;
                color="yellow"
            else:
                if myword==':': nextcolor="magenta"
                elif myword=='.': nextcolor="lawn green"
                elif (nextcolor!="white"):
                    color=nextcolor
                    nextcolor="white"
                    wordonly=True
                elif myword.lower() in self.KEYWORDLIST: 
                    color="cyan"
                    wordonly=True
            self.setSynColor(color,lno,startx,x)
            if wordonly:
                color="white"
            wordonly=False
    
    def setSynColor(self,color:str, lno:int, start:int, end:int)->None:
        fromix="%d.%d" % (lno,start)
        toix="%d.%d" % (lno,end)
        self.textbox.tag_add(color,fromix,toix)

if __name__=="__main__":
    root=Tk()
    c=CodeText(root,background="black",foreground="white",font=("Courier",12,"bold"),insertbackground="white")
    c.pack(fill=BOTH,expand=True)
    with open("c:/kev/test.moo","r") as f:
        data=f.read();
        c.textbox.insert("1.0",data)
    c.highlight()
    root.mainloop()

