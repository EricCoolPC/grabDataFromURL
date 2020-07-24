import requests
import re
from markdown import markdown
from bs4 import BeautifulSoup
from tkinter import *

def strip_char(str, chars,replace):
    return ",".join(c for c in str if c not in chars)

def runCode():
    url = str(t2.get())
    url2 = requests.get(url)
    htmltext = url2.text

    filename = str(t1.get())

    #html = markdown(htmltext)

    clean_text = ''.join(BeautifulSoup(htmltext, "html.parser").stripped_strings)

    #top: editRound
    #bottom: Source
    #https://cheatography.com/mutanclan/cheat-sheets/python-regular-expression-regex/
    #https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python

    clean_text = clean_text.replace("[", "")
    clean_text = clean_text.replace("]", "")

    clean_text = re.findall('(?<=editRound)(.*?)(?=\S*\))', clean_text)
    clean_text = str(clean_text)

    clean_text = strip_char(clean_text, "abcdefghijklmnopqrstuvwxyzABCEFGHIJKMNOPQRSUVXYZ1234567890,:;-_'-,<>!@#$%^&*()–+=\" ", "")

    clean_text = clean_text.replace("W", "3")
    clean_text = clean_text.replace("L", "0")
    clean_text = clean_text.replace("D", "1")
    clean_text = clean_text.replace("T", "1")
    clean_text = clean_text.replace("[,", "")
    clean_text = clean_text.replace(",]", "")

    clean_text = clean_text.split(",")

    clean_text = str(clean_text)

    clean_text = clean_text.replace("[", "")
    clean_text = clean_text.replace("]", "")
    clean_text = clean_text.replace("'", "")


    f = open(filename+'.csv','w')
    f.write(clean_text) #Give your csv text here.
    # Python will convert \n to os.linesep
    f.close()

    print(clean_text)

window=Tk()
btn=Button(window, text="Submit", fg='blue', command=runCode)
btn.place(x=150, y=250)
lbl=Label(window, text="Type URL", fg='red', font=("Helvetica", 16))
lbl.place(x=145, y=50)
lb2=Label(window, text="Type Filename", fg='red', font=("Helvetica", 16))
lb2.place(x=145, y=150)
t1=Entry(window, text="Filename", bd=5)
t1.place(x=150, y=200)
t2=Entry(window, text="URL", bd=5)
t2.place(x=150, y=100)

    
window.title('Soccer Wifi Stat Grabber')
window.geometry("400x300+10+10")
window.mainloop()
