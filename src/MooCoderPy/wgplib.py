"""Some general purpose useful routines"""

def parse(s:str):
    """Get the next space separated word from a string. Return (word,remainder)"""
    s=s.strip()
    i=s.find(" ")
    if i<0:
        i=len(s)
    result=s[0:i].strip()
    remain=s[i+1:].strip()
    return (result,remain)

def parsesep(s:str, sep:str=","):
    """Get the next word from a string, separated ny sep. Return (word,remainder)"""
    i=s.find(sep)
    if i<0:
        i=len(s)
    result=s[0:i]
    remain=s[i+1:]
    return (result,remain)

def getsepfield(s:str, n:int, sep:str=","):
    """Get nth word in s, separated by sep"""
    list=s.split(sep)
    if n<0 or n>=len(list):
        return ""
    return list[n]

def getfield(s:str, n:int):
    """Get nth worh in s, separated by whitespace."""
    list=s.split()
    if n<0 or n>=len(list):
        return ""
    return list[n]

def atol(s:str)->int:
    """Convert string to int in a relaxed fashion... ie, stop when non-integer found."""
    result=""
    for c in s:
        if c=="-" and result=="":
            result+=c
        elif c==" ":
            continue
        elif c.isdigit():
            result+=c
        else:
            break
    try:    
        result=int(result)
    except:
        result=0
    return result

def ansiSameText(s1:str,s2:str)->bool:
    """Compare two strings case insensitive"""
    return (s1.lower()==s2.lower())

if __name__=="__main__":
    print(atol("1234x"))
    print(atol("-234 this is a test"))