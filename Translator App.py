from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import googletrans
from googletrans import Translator
import pyttsx3


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(500, label_change)


def translate_now():
    text = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text
    text2.delete(1.0, END)
    text2.insert(END, trans_text)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 100)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)


def speak():
    audio_convert = str(text2.get(1.0, END))
    engine.say(audio_convert)
    engine.runAndWait()


root = ttk.Window(themename='superhero')
root.title('Google Translator')
root.geometry('1200x500')

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()
combo1 = ttk.Combobox(root, values=languageV, font='Roboto 10', bootstyle='info')
combo1.place(x=110, y=20)
combo1.set('ENGLISH')
label1 = ttk.Label(root, text='ENGLISH', font='segoe 10 bold', relief=RIDGE, width=40, border=5, padding=5)
label1.place(x=50, y=70)
combo2 = ttk.Combobox(root, values=languageV, font='Roboto 10', bootstyle='danger')
combo2.place(x=730, y=20)
combo2.set('SELECT LANGUAGE')
label2 = ttk.Label(root, text='ENGLISH', font='segoe 10 bold', relief=GROOVE, width=40, border=5, padding=5)
label2.place(x=650, y=70)
f = ttk.Frame(root, bootstyle='dark', border=5)
f.place(x=10, y=118, width=450, height=250)
text1 = ttk.Text(f, font='Roboto 20', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=240)
scrollbar = ttk.Scrollbar(f)
scrollbar.pack(side='right', fill='y')
scrollbar.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar.set)
f1 = ttk.Frame(root, bootstyle='dark', border=5)
f1.place(x=620, y=118, width=450, height=250)
text2 = ttk.Text(f1, font='Roboto 20', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=240)
scrollbar1 = ttk.Scrollbar(f1)
scrollbar1.pack(side='right', fill='y')
scrollbar1.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar.set)
image = Image.open("arrows.png").resize((30, 30))
photo = ImageTk.PhotoImage(image)
translate_button = ttk.Button(root, image=photo, bootstyle='secondary-outline-toolbutton', command=translate_now)
translate_button.place(x=500, y=250)
image1 = Image.open("voice.png").resize((30, 30))
photo1 = ImageTk.PhotoImage(image1)
voice_button = ttk.Button(root, text='Voice', bootstyle='secondary-outline-toolbutton', command=speak, image=photo1)
voice_button.place(x=500, y=300)


label_change()
root.mainloop()



