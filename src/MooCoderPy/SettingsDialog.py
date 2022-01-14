from tkinter import *
import tkinter.simpledialog
import configparser

class SettingsDialog(tkinter.simpledialog.Dialog):

    def body(self, master):
        self.inifile=getConfig()
        settings=self.inifile["settings"]
        f=("Helvetica",12)
        Label(master, text="Server:",font=f).grid(row=0)
        Label(master, text="Connect:",font=f).grid(row=1)
        self.e1var = StringVar(value=settings.get("Server","example.server.net:8922"))
        self.e2var = StringVar(value=settings.get("Connect","login command here"))
        self.e1 = Entry(master,width=60,font=f,textvariable=self.e1var)
        self.e2 = Entry(master,width=60,font=f,textvariable=self.e2var)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        print(first, second)
        self.result=(first,second)
        settings=self.inifile["settings"]
        settings["Server"]=first
        settings["Connect"]=second
        saveConfig(self.inifile)

def getConfig():
    inifile=configparser.ConfigParser()
    inifile.read("moocoderpy.ini")
    if not inifile.has_section("settings"):
        inifile.add_section("settings")
    if inifile.has_section("DEFAULT"):
        inifile.remove_section("DEFAULT")
    return inifile

def saveConfig(inifile):
    with open("moocoderpy.ini","w") as fp:
        inifile.write(fp)

if __name__ == "__main__":
    
    root=Tk()
    d=SettingsDialog(None,title="MoocoderPy Settings")
    print(d.result)