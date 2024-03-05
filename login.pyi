import pyttsx3 as pt
import os
import datetime

def engin(bol):
    engine = pt.init('sapi5')
    change = engine.getProperty('voices')
    engine.setProperty('voice',change[1].id)
    engine.setProperty('rate',150)
    engine.say(bol)
    engine.runAndWait()
    
def wishme():
    hou = int(datetime.datetime.now().hour)
    if hou>=0 and hou<12:
        engin('good morning boss')
    elif hou >= 12 and hou <= 18:
        engin('good afternoon boss')
    else:
        engin('good evening boss')
        
wishme()
engin('welcome in your computer, have a grate day')

date = datetime.date.today()
fol = f'{datetime.date.today().month}-{datetime.date.today().year}'
# print(fol)
i= datetime.datetime.now().hour
z= datetime.datetime.now()

if i >= 12:
    i -= 12
    login = f'{i}:{z.minute}:{z.second} PM '
    if i == 0:
        i = 12
        login = f'{i}:{z.minute}:{z.second} PM '
else:
    login = f'{i}:{z.minute}:{z.second} AM '  
    
# print(login)

try:
    os.mkdir('D:/login')
except:
    pass

try:
    os.mkdir(f'D:/login/{fol}')
except:
    pass

mon = datetime.date.today().day

try:
    with open(f'D:/login/{fol}/{mon}.txt','r') as font:
        a = font.readlines()
    for line in a:
        pass
       
    if "PM" in line:
        line = line[:-8]
        line = line.replace('This device is login at >>','').replace(':',"\t")
        engin(f'last time tis device is login at {line} PM ')
    else:
        line = line[:-8]
        line = line.replace('This device is login at >>','').replace(':',"\t")
        engin(f'last time tis device is login at {line} AM ')
except:
    pass

with open(f'D:/login/{fol}/{mon}.txt','a') as source:
    source.write(f'This device is login at >> {login} \n')    
