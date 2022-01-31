class ParseText:
    line:str
    isquote=False
    isescaped=False
    x:int=0
    c:str

    def __init__(self, line):
        self.line=line
    
    def next(self)->bool:
        if self.x>=len(self.line):
            return False
        c=self.line[self.x]
        self.x+=1
        if self.isquote:
            if self.isescaped:
                self.isescaped=False
            elif c=='"':
                self.isquote=False
            elif c=="\\":
                self.isescaped=True
        else:
            if c=='"' and not self.isescaped:
                self.isquote=True
        self.c=c
        return True


def splitList2(line):
    def indent():
        return "\n"+(" "*pad)

    p=ParseText(line)
    result=""
    pad=0
    while (p.next()):
        c=p.c
        if p.isquote:
            result+=c
        else:
            if c==",":
                result+=c+indent()
            elif c in r"[{":
                pad+=2
                result+=c+indent()
            elif c in "}]":
                pad -=2
                result+=indent()+c
            elif c==" ":
                continue
            else:
                result+=c
    return result

def joinList(data:str):
    result=""
    p=ParseText(data)
    while p.next():
        c=p.c
        if p.isquote or not(c.isspace()):
            result+=c
            if (c==","):
                result+=" "
    return result

def splitList(line):
    isquote=False
    isescaped=False
    isclosing=False
    pad=0
    result=""
    prevchar=""
    hasclosed=True
    for c in line:
        if isquote:
            if isescaped:
                isescaped=False
            elif c=='"':
                isquote=False
            elif c=="\\":
                isescaped=True
        else:
            if c=='"' and not isescaped:
                isquote=True
        if isquote:
            result+=c
        else:
            if c in r"[{":
                if not(hasclosed):
                    result+="\n"+(" " * pad)
                result+=c
                isclosing=False
                hasclosed=False
                pad+=2
            elif c in "}]":
                pad -=2
                if (isclosing):
                    result+="\n"+(" " * pad)+c
                    hasclosed=True
                else:
                    isclosing=True
                    result+=c
            elif c==",":
                if (isclosing):
                    result+=c+"\n"+(" " * pad)
                    hasclosed=True
                else:
                    isclosing=False
                    result+=c
            elif c==" " and prevchar==",":
                continue
            else:
                result+=c
                isclosing=False
            prevchar=c
    return result

if __name__=="__main__":
    s='{{["damage" -> 0.6, "name" -> "Simple", "percent" -> 75], ["damage" -> 0.7, "name" -> "Basic", "percent" -> 60], ["damage" -> 0.8, "name" -> "Standard", "percent" -> 45], ["damage" -> 1.0, "name" -> "Moderate", "percent" -> 30], ["damage" -> 1.0, "name" -> "Difficult", "percent" -> 15], ["damage" -> {1.25,2,5}, "name" -> "Direct", "percent" -> 0], ["damage" -> 1.5, "name" -> "Taxing", "percent" -> -15],{1,2,3}}}'
    print(splitList2(s))
    print(splitList('1'))
    print(splitList2('{"I am a string", "List of", "Strings"}'))
    print("Rejoined: ",joinList(splitList2(s)))
