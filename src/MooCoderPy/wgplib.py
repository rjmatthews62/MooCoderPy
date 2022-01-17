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

