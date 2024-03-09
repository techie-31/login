
## About project

This program will help you to keep record of you device when you login, with proper folder and date management. This program will wish you when you login your device. you can make changes as you want...


## Features

- Wish you when your computer turn on
- Make a records of when device log in
- Notify when last time device log in
- Proper directory management


## Module


```module
  pip install pyttsx3
```



## Changes

You can replace path and intro, if you dont like. Here the code line where you can make changes.

#### For changing path
```python
try:
    os.mkdir('D:/login')
except:
    pass



try:
    os.mkdir(f'D:/login/{fol}')
except:
    pass



try:
    with open(f'D:/login/{fol}/{mon}.txt','r') as font:
        a = font.readlines()
    for line in a:
        pass



with open(f'D:/login/{fol}/{mon}.txt','a') as source:

```

#### To change intro words

```python
engin('welcome in your computer, have a grate day')
```

##  Language
- Python


## Feedback

If you have any feedback, please reach out to us at instagram. 
## 🔗 Links

[![Instagram](https://img.shields.io/badge/instagram-000?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/techie_31/)

