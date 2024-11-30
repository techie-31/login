import pyttsx3 as pt
import os
import datetime as dt
import json
import csv
import cv2
import time
from pygrabber.dshow_graph import FilterGraph

# todo user path


# cp = os.getcwd()
cp = os.path.dirname(os.getcwd()) 
# cjp = os.path.expanduser("~")
cjp = os.getenv('LOCALAPPDATA')
date = dt.date.today()
ck = f"{cjp}/Login.3.0"

# todo initializing main folder
try:
    os.mkdir(f"{cjp}/Login.3.0")
except Exception as err:
    pass

try:
    os.mkdir(f"{ck}/data")
except Exception as err:
    pass

# todo getting data from cc.li
try:
    with open(f"{ck}/cns/cc.li","r") as jsk:
        mata= json.loads(jsk.read())
except Exception as err:
    with open(f"{cp}/reset.li","r") as jsk:
        mata= json.loads(jsk.read())
    pass

# todo counting days
jss = {
    "voice":mata["voice"],
    "version":mata["version"],
    "command":mata["command"],
    "shedule":mata["shedule"],
    "morning":mata["morning"],
    "afternoon":mata["afternoon"],
    "evening":mata["evening"],
    "image":mata["image"],
    "delete":mata["delete"],
    "day":mata["day"] if str(date) == mata["date"] else mata["day"]+1 ,
    "date":f"{date}"
}

try:
    with open(f"{ck}/cns/cc.li","w") as jsa:
        jsa.write(json.dumps(jss))
except Exception as err:
    pass


def engin(bol):
    engine = pt.init('sapi5')
    change = engine.getProperty('voices')
    engine.setProperty('voice',change[1 if mata["version"] == "Female version" else 0].id)
    engine.setProperty('rate',150)
    engine.say(bol)
    engine.runAndWait()
    
def wishme():
    hou = int(dt.datetime.now().hour)
    if hou>=0 and hou<12:
        engin(mata["morning"])
    elif hou >= 12 and hou <= 18:
        engin(mata["afternoon"])
    else:
        engin(mata["evening"])
        
def listc():
    # global devices
    graph = FilterGraph()
    devices = graph.get_input_devices()
    return devices

def capture_image():
    try:
        with open(f"{ck}/cns/cam.li","r") as jso:
            ccv = jso.read()
    except Exception as err:
        pass
    
    try:
        lcck = listc()
        for index,i in enumerate(lcck):
            if ccv == i:
                canum = index
                break
    except Exception as err:
        pass
    
    try:
        # Initialize the camera (0 is usually the default camera)
        cap = cv2.VideoCapture(canum)

        # Capture a frame
        ret, frame = cap.read()

        # Check if the frame was captured
        if ret:
            # Generate a unique filename based on the current date and time
            # filename = f"D:/Coading/Programs/app/data/{date}/{login}" + ".png"
            filename = os.path.join(f"{ck}/data/{date}/",f"{imgtm}.png" )
            # filename = login + ".png"
            
            # Save the captured image
            cv2.imwrite(filename, frame)
            # print(f"Image saved as {filename}")
        else:
            # print("Failed to capture image.")
            pass

        # Release the camera
        cap.release()
    except Exception as err:
        pass


login = dt.datetime.now().strftime("%I:%M %p")
imgtm = dt.datetime.now().strftime("%I-%M-%S-%p")

# todo initializing sub date folder
try:
    os.mkdir(f"{ck}/data/{date}")
except Exception as err:
    # print(err)
    pass

try:   
    with open(f"{ck}/data/{date}/main.csv","r") as dde:
        ded = csv.reader(dde)
        lsk = list(ded)
except Exception as err:
    # print(err)
    pass
    
if mata["image"] == 1:
    capture_image()
    
# todo shedulded
if mata["voice"] == 1:
    if mata["shedule"] == 1:
        wishme()
    # todo main command
    engin(mata["command"])
    try:
        engin(f'last time tis device was login at {lsk[len(lsk)-1][0]}')
    except Exception as err:
        pass

    
# todo initializing and data add , .csv file
try:
    with open(f"{ck}/data/{date}/main.csv","a") as aa:
        aa.write(f"{login},0 hr 00 min,{imgtm}\n")
except Exception as err:
    pass


# todo perform delete function
t = dt.date.today()
lists = os.listdir(f"{ck}/data")
dirc = []
if mata["delete"] == "Month":
    if mata["day"] >= 30:
        for i in range(7):
            d = dt.timedelta(days=i)
            dirc += f"{t-d}",
        for i in lists:
            if i in dirc:
                pass
            else:
                # print(i, "removed")
                os.rmdir(f"{ck}/data/{i}")
        jss["day"] = 0
        try:
            with open(f"{ck}/cns/cc.li","w") as js:
                js.write(json.dumps(jss))
        except Exception as err:
            # print(err)
            pass
elif mata["delete"] == "Year":
    if mata["day"] >= 365:
        for i in range(7):
            d = dt.timedelta(days=i)
            dirc += f"{t-d}",
        for i in lists:
            if i in dirc:
                pass
            else:
                # print(i, "removed")
                try:
                    os.rmdir(f"{ck}/data/{i}")
                except:
                    pass
        jss["day"] = 0
        try:
            with open(f"{ck}/cns/cc.li","w") as jsj:
                jsj.write(json.dumps(jss))
        except Exception as err:
            # print(err)
            pass
        
# todo time counting
mins = 0
while True:
    time.sleep(60)
    mins += 1
    hr,mi = divmod(mins,60)
    mi= f"0{mi}" if len(str(mi)) == 1 else mi
    tame = f"{hr} hr {mi} min"
    
    with open(f"{ck}/data/{date}/main.csv","r") as dd:
        de = csv.reader(dd)
        ls = list(de)
    
    ls[len(ls)-1][1] = tame
    with open(f"{ck}/data/{date}/main.csv","w",newline="") as dk:
        dz = csv.writer(dk)
        dz.writerows(ls)
