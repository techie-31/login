from tkinter import *
import os

mpath = os.path.dirname(os.getcwd()) # to run in exe
# mpath = os.getcwd()

root = Tk()
root.geometry("600x445")
root.iconbitmap(f"{mpath}/file.ico")
root.title("Gathering the latest information...")
root.resizable(False, False)

import json
import csv
import datetime as dt
import cv2
from tkcalendar import Calendar
import webbrowser
import tkinter.messagebox as tmsg
import subprocess
import requests

url = "https://techie-31.github.io/API/Login/data.json"
kiko = os.getenv('LOCALAPPDATA')
mkiko = f"{kiko}/Login.3.0"
junction = f"{mkiko}/cns"
date2 = dt.date.today()
win_open = False
version = "Login.3.2"

try:
    os.mkdir(f"{kiko}/Login.3.0")
except Exception as err:
    pass

def show_image(even):
    try:
        label_text = even.widget.cget("textvariable")   
        image = cv2.imread(f"{mkiko}/data/{date2}/{label_text}.png")
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as err:
        pass

def clear_scrollable_frame():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
        
def cal():
    global win_open
    
    def on_date_click(event):
        global win_open
        selected_date = cal.get_date()
        date_obj = dt.datetime.strptime(selected_date, "%m/%d/%y")
        formatted_date = date_obj.strftime("%d-%m-%Y  %A")
        win_open = False
        roo.destroy()
        global date2
        date2 = date_obj.strftime("%Y-%m-%d")
        dd.config(text=f"Selected Date : {formatted_date}")
        clear_scrollable_frame()
        info()
        logup.config(text=f"Logins : {lognum()}")
    
    win_open = True
    
    def close_date():
        roo.destroy()
        global win_open
        win_open = False
    
    roo = Tk()
    roo.iconbitmap(f"{mpath}/file.ico")
    roo.resizable(False, False)
    roo.title("Date Picker")
    roh = dt.datetime.strptime(str(date2), "%Y-%m-%d")
    # cal = Calendar(roo, selectmode='day', year=dt.date.today().year, month=dt.date.today().month, day=dt.date.today().day)
    cal = Calendar(roo, selectmode='day', year=roh.year, month=roh.month, day=roh.day)
    cal.pack()
    cal.bind("<<CalendarSelected>>", on_date_click)
    roo.protocol("WM_DELETE_WINDOW",close_date)
    roo.mainloop()
     


def SettingToggle():
    try:
        with open(f"{junction}/toggle.li","r") as tog:
            readToggle = tog.read()
    except:
        pass
    
    if readToggle == "0":
        try:
            with open(f"{junction}/toggle.li","w") as tog:
                tog.write("1")      
        except:
            pass
        
        subprocess.run(f"{mpath}/Adjustments/Adjustments.exe")
    

#todo IOT 
try:
    update = requests.get(url,timeout=5)
    update.raise_for_status()
    with open(f"{junction}/api.li","w") as lik:
        lik.write(json.dumps(update.json()))
except Exception as err:
    pass

#todo json extraction
try:
    with open(f"{junction}/api.li","r") as pik:
        content = json.loads(pik.read())
except:
    content = {
        "update":"Login.3.2",
        "content":"Not available",
        "instagram":"Connect-to-internet",
        "feedback":"Connect-to-internet",
        "credit":"Syncing....",
        "devloper":"Syncing...."
    }
    pass


# todo Gui code

root.title("Login")
menu = Menu(root)
m1 = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=m1)
m1.add_command(label="Adjustments",command=SettingToggle)
m1.add_command(label="Close",command=lambda:root.destroy())
m2 = Menu(menu, tearoff=0)
menu.add_cascade(label="About",menu =m2)
m2.add_command(label="Software",command= lambda:tmsg.showinfo("Software","Login"))
m2.add_command(label="Version",command= lambda:tmsg.showinfo("Version",version))
m2.add_command(label="Developer",command= lambda:tmsg.showinfo("Developer",content["devloper"]))
m2.add_command(label="Credit",command= lambda:tmsg.showinfo("Credit",content["credit"]))
m2.add_command(label="Instagram",command=lambda:webbrowser.open(content["instagram"]))
menu.add_command(label="Feedback",command=lambda:webbrowser.open(content["feedback"]))
root.config(menu=menu)

def DateWindowToggle():
    if win_open == False:
        cal()
    else:
        pass
    
frame = Frame(root)

f1 = Frame(frame, pady=2)
Label(f1, text="Login", font="lucid 10 bold", pady=5, width=24, relief="solid", borderwidth=1).pack(side="left")
Label(f1, text="Up time", font="lucid 10 bold", pady=5, width=24, relief="solid", borderwidth=1).pack(side="left", padx=10)
Button(f1, text="Date", pady=2, relief="groove", padx=10, command=DateWindowToggle,width=20,font="lucid 10").pack(padx=20)
f1.pack(anchor="nw", fill="x")

listframe = Frame(frame, relief="solid", borderwidth=1)
listframe.pack(fill="x", pady=20)
canvas = Canvas(listframe)
canvas.pack(side="left", fill="both", expand=True, pady=5)

scrollbar = Scrollbar(listframe, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

scrollable_frame = Frame(canvas)
scrollable_frame.bind("<MouseWheel>", on_mouse_wheel)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def show_err(eve):
    pass

try:
    with open(f"{junction}/cc.li","r") as js:
        mdata = json.loads(js.read())
except Exception as err:
    with open(f"{mpath}/reset.li","r") as js:
        mdata = json.loads(js.read())   
    pass

def info():
    try:
        with open(f"{mkiko}/data/{date2}/main.csv", "r") as k:
            file = csv.reader(k)
            for i in file:
                f2 = Frame(scrollable_frame, borderwidth=2)
                f2.bind("<MouseWheel>", on_mouse_wheel)
                kj = Label(f2, text=i[0], font="lucid 10", width=24, pady=5)
                kj.bind("<MouseWheel>", on_mouse_wheel)
                kj.pack(side="left")
                kg = Label(f2, text=i[1], font="lucid 10", width=24, pady=5)
                kg.bind("<MouseWheel>", on_mouse_wheel)
                kg.pack(side="left")
                lssk = os.listdir(f"{mkiko}/data/{date2}")
                btn = Button(f2, text="View image", font="lucid 10", padx=5, relief="groove", state="disabled" if mdata["image"] == 0 else "normal", textvariable=i[2])
                btn.bind("<MouseWheel>", on_mouse_wheel)
                if mdata["image"] == 0:
                    pass
                else:
                    btn.bind("<Button-1>", show_image)
                    if f"{i[2]}.png" in lssk:
                        btn.config(state="normal")
                    else:
                        btn.config(state="disabled")
                        btn.bind("<Button-1>", show_err)
                btn.pack(side="left", padx=40)
                f2.pack(side="top", anchor="nw", pady=2)
    except Exception as err:
        pass

frame.pack(fill="both", pady=20, padx=20)

info()

def lognum():
    try:
        with open(f"{mkiko}/data/{date2}/main.csv", "r") as dh:
            dl = csv.reader(dh)
            lsk = list(dl)
    except Exception as err:
        lsk = ""
        pass
    
    return len(lsk)

status = Frame(frame, relief="groove", borderwidth=2)
ktime = dt.datetime.now().strftime("%d-%m-%Y  %A")
dd = Label(status, text=f"Selected Date : {ktime}", font="lucid 10 bold")
dd.pack(side="left", padx=20, pady=2)
logup = Label(status, text=f"Logins : {lognum()}", font="lucid 10 bold")
logup.pack(side="right", padx=40, pady=2)
status.pack(fill="x", side="bottom")

try:
    os.mkdir(junction)
except Exception as err:
    pass
    
try:
    with open(f"{junction}/toggle.li","w") as tog:
        tog.write("0")
except:
    pass

if version != content["update"]:
    tmsg.showinfo("Update",content["content"])

root.mainloop()
