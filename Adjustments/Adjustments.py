from tkinter import *
import os

cpath = os.path.dirname(os.getcwd()) # to run in environment

roof = Tk()
roof.geometry("600x515")
roof.title("Gathering the latest information...")
roof.iconbitmap(f"{cpath}/file.ico")
roof.resizable(False, False)

import json
import winshell
import cv2
from pygrabber.dshow_graph import FilterGraph
import tkinter.messagebox as tmsg

# cpath = os.getcwd() 
path_admin = os.getenv('LOCALAPPDATA')
node = f"{path_admin}/Login.3.0/cns"

try:
    os.mkdir(f"{path_admin}/Login.3.0/cns")
except Exception as err:
    pass

def list_c():
    # global devices
    graph = FilterGraph()
    devices = graph.get_input_devices()
    return devices

def camera_open():
    # Open the camera (0 is usually the default camera)   
    try:
        with open(f"{node}/cam.li","r") as jsr:
            cnum = jsr.read()
    except Exception as err:
        # print(err)
        pass
    
    lcc = list_c()
    for index,i in enumerate(lcc):
        if cnum == i:
            cam_num = index
            break
    try:
        cap = cv2.VideoCapture(cam_num)

        # Check if the camera opened successfully
        if not cap.isOpened():
            # print("Error: Could not open camera.")
            exit()

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If frame is read correctly ret is True
            if not ret:
                # print("Failed to grab frame")
                break
            # Display the resulting frame
            cv2.imshow('Camera', frame)

            # Check if the 'q' key is pressed or the window is closed
            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
                break
        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()
    except Exception as err:
        pass
    
    
def cam_wri(eve):
    try:
        with open(f"{node}/cam.li","w") as jsr:
            jsr.write(eve)
    except Exception as err:
                # print(err)
                pass

   
def windowCloser():
    roof.destroy()
    try:
        with open(f"{node}/toggle.li","w") as tog:
            tog.write("0")
    except:
        pass
    

try:
    with open(f"{node}/cc.li","r") as js:
        data = json.loads(js.read())
except:
    with open(f"{cpath}/reset.li","r") as js:
        data = json.loads(js.read())
        

# todo Gui code
roof.title("Adjustments")
roof.protocol("WM_DELETE_WINDOW",windowCloser)

Frame(roof).pack(fill ="x",pady=5)

frame = Frame(roof,relief="groove",borderwidth=2)
greet = IntVar()
greet.set(data["voice"])

def voicegreet():
    if greet.get() == 1:
        ver.config(state="normal")
        mcom.config(state="normal")
        shedule.config(state="normal")
        if sh.get() == 1:
            for i in comss:
                i.config(state="normal")
        else:
            for i in comss:
                i.config(state="disabled")
    else:
        ver.config(state="disabled")
        mcom.config(state="disabled")
        shedule.config(state="disabled")
        for i in comss:
            i.config(state="disabled")
            
voic_com = Checkbutton(master=frame,text="Voice Command", font="lucid 10 bold",variable=greet,command=voicegreet)
voic_com.pack(pady=5,padx = 10)
frame.pack(pady = 5,fill="x",padx =20)

f1 = Frame(roof,relief="solid",borderwidth=1)

f11 = Frame(f1)
var = StringVar()
var.set(data["version"])
Label(master=f11, text="Version", font="lucid 10 bold").pack(side="left",padx = 20)
ver = OptionMenu(f11,var,"Male version","Female version")
ver.config(state="disabled" if data["voice"] == 0 else "normal")
ver.pack(side= "left",padx =20)
ver.config(relief="ridge")
f11.pack(fill="x",pady =10)

f12 = Frame(f1)
Label(master=f12,text="Command", font="lucid 10 bold").pack(side="left",padx = 20)
comm = StringVar()
comm.set(data["command"])
mcom = Entry(master=f12,font="lucid 10",width=50,textvariable=comm,state="disabled" if data["voice"] == 0 else "normal")
mcom.pack(side= "left",padx =20)
f12.pack(fill ="x",pady =10)

f14 = Frame(f1,relief="solid",borderwidth=1)
sh = IntVar()
sh.set(data["shedule"])

def shed():
    if sh.get() == 1:
        for i in comss:
            i.config(state="normal")
    else:
        for i in comss:
            i.config(state="disabled")
            
shedule = Checkbutton(master=f14,text="Scheduled Command", font="lucid 10 bold",variable=sh,state="disabled" if data["voice"] == 0 else "normal",command=shed)
shedule.pack(pady = 2,padx = 60)
f14.pack(pady = 10)

gmm = StringVar()
gmm.set(data["morning"])
am = StringVar()
am.set(data["afternoon"])
em = StringVar()
em.set(data["evening"])
mix = [gmm,am,em]
gaf = ["Morinig Command","Afternoon Command","Evening Command"]

comss =[]

for index,i in enumerate(gaf):
    f13 = Frame(f1)
    Label(master=f13, text=i, font="lucid 10 bold").pack(side="left",padx = 20)
    com = Entry(master=f13,textvariable=mix[index], font="lucid 10",width=50)
    comss += [com]
    com.pack(side= "left",padx =20)
    f13.pack(fill ="x",pady=10)
f1.pack(fill="x",padx =20,pady=5)


if data["voice"] == 1:
    if data["shedule"] == 1:
        for i in comss:
            i.config(state="normal")
    else:
        for i in comss:
            i.config(state="disabled")
else:
    for i in comss:
        i.config(state="disable")


f2 = Frame(roof,relief="solid",borderwidth=1)
imgche = IntVar()
imgche.set(data["image"])

def cam():
    listof = list_c()
    if len(listof) == 0:
        tmsg.showerror("Can't find webcam","Connect webcam to enable this feature")
        imgche.set(0)
        opecam.config(state="disabled")
    else:
        if imgche.get() == 1:
            opecam.config(state="normal")
            try:
                with open(f"{node}/cam.li","w") as jsk:
                    jsk.write(listof[0])
            except Exception as err:
                # print(err)
                pass 
        else:
            opecam.config(state="disabled")

gm = Checkbutton(master=f2,text="Capture image", font="lucid 10 bold",variable=imgche,command=cam)
gm.pack(pady = 10,side="left",padx = 20)

def open_set():
    window = Tk()
    window.geometry("310x100")
    window.iconbitmap(f"{cpath}/file.ico")
    window.title("Camera Settings")
    window.resizable(False, False)
    global stro
    fr = Frame(window)
    stro = StringVar(fr)
    devi = list_c()
    try:
        with open(f"{node}/cam.li","r") as jsa:
            cumra = jsa.read()
        stro.set(cumra)
    except Exception as err:
        stro.set(devi[0])
        pass
    Label(fr,text="Select camera",font="lucid 10 bold").pack(side="left",padx=10)
    OptionMenu(fr,stro,*devi,command=cam_wri).pack(side="left")
    fr.pack(pady=10)
    fr2 = Frame(window)
    Button(fr2,text="Open camera",width=15,pady=5,command=camera_open).pack(side="left",padx=10)
    Button(fr2,text="Apply",width=15,pady=5,command=window.destroy).pack(side="left",padx=10)
    fr2.pack(fill="x",padx=20,pady=5)
    
    window.mainloop()
    
opecam = Button(master=f2, text="Settings", relief="raised", width=10,borderwidth=3,state="disabled" if data["image"] == 0 else "normal",command=open_set)
opecam.pack(side="right", padx=20)
f2.pack(fill="x",padx =20,pady=10)

f3 = Frame(roof)
davar = StringVar()
davar.set(data["delete"])
Label(master=f3, text="Auto Delete", font="lucid 10 bold").pack(padx=20,side="left")
date = OptionMenu(f3,davar,"Year","Month","Never")
date.config(relief="ridge")
date.pack(padx = 20,side="left")
f3.pack(fill="x",padx = 20,pady= 5)

f4 = Frame(roof)
btnlist = ["Cancle","Reset","Apply"]

def restart():
    win = Tk()
    win.iconbitmap(f"{cpath}/file.ico")
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
    
def apply():
    roof.destroy()
    restart()
    data_r = {
    "voice":greet.get(),
    "version":var.get(),
    "command":comm.get(),
    "shedule":sh.get(),
    "morning":gmm.get(),
    "afternoon":am.get(),
    "evening":em.get(),
    "image":imgche.get(),
    "delete":davar.get(),
    "day":data["day"],
    "date":data["date"]
    }
    
    try:
        with open(f"{node}/cc.li","w") as js:
            js.write(json.dumps(data_r))
    except Exception as err:
        # print(err)
        pass
    desktop = winshell.startup()
    path = os.path.join(desktop, 'log.lnk')
    # Set the target path (e.g., path to an executable or script)
    target = f'{cpath}\log\log.exe'

    # Create the shortcut
    winshell.CreateShortcut(
        Path=path,
        Target=target,
        StartIn=f"{cpath}\log",
        Description="developer--@techie_31",
    )
    # todo hiding the login
    # os.system(f'attrib +h "{path}"')

    try:
        with open(f"{node}/toggle.li","w") as tog:
            tog.write("0")
    except:
        pass
    

try:
    with open(f"{cpath}/reset.li","r") as jsr:
        datarm= json.loads(jsr.read())
except Exception as err:
    # print(err)
    pass

def reset():
    greet.set(datarm["voice"])
    var.set(datarm["version"])
    comm.set(datarm["command"])
    sh.set(datarm["shedule"])
    gmm.set(datarm["morning"])
    am.set(datarm["afternoon"])
    em.set(datarm["evening"])
    imgche.set(datarm["image"])
    davar.set(datarm["delete"])
    voicegreet()
    cam()
    
fun = [windowCloser,reset,apply]
for index,i in enumerate(btnlist):
    btn = Button(master = f4,text=i, font="lucid 10 bold",width=20,pady=5,command=fun[index])
    btn.pack(side="left",padx=10)
f4.pack(fill="x",padx =30,pady=10)

roof.mainloop()
