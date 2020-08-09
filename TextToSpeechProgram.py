import pyttsx3
from tkinter import *
from tkinter.messagebox import showinfo

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def help():
    notice = "It is A Simple Text To Speech Application Developed By Abhishek Kumar In Python Programming Language."
    showinfo("Help", notice)

def speak_text(*audio):
    engine.say(*audio)
    engine.runAndWait()

def speaker():
    global screen_val
    speak_text(screen_val.get())

root = Tk()
root.title("Text To Speech")
root.geometry("300x200")
root.wm_iconbitmap("App Components\\Icons\\my_mic.ico")
root.maxsize(300, 200)
root.minsize(300, 200)

filemenu = Menu(root)
filemenu.add_command(label="Help", command=help)
root.config(menu=filemenu)

screen_val = StringVar()
screen_val.set("Text Here")
screen = Entry(root, textvar=screen_val, font=("Forte 30"))
screen.pack(padx=10, pady=10)

b = Button(root, text="Speak", font=("Forte 30 bold"), command=speaker)
b.pack(pady=10)

root.mainloop()