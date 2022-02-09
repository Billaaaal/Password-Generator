import time
from tkinter import *
import tkinter as tk
import random
from tkinter import font
import keyboard
import string
import pyperclip
from tkinter import Tk, Label
from time import sleep
import os


lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
keyboard_characters=list(lower+upper)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')



def generate():
    tag="Password_text"
    if tag == "Password_text":
        canvas.delete("Password_text")
    else:
        pass
    global password
    all = lower + upper + digits + symbols 
    password_length = textbox.get()
    try:
        password_length = int(password_length)
    except ValueError:
        password_length = 8
    if password_length > 20:
        global font_size_for_text_display
        font_size_for_text_display = 15
      
    else:
        font_size_for_text_display = 20
    try:
        temp = random.sample(all, password_length)
    except ValueError:
        temp = random.sample(all, 22)

    password = "".join(temp)

    if password:
        Password_text = canvas.create_text(
        182.5, 200,
        text = password,
        fill = "#654554",
        tag="Password_text",
        font = ("SFProText-Bold", font_size_for_text_display))

def copy_password():
    try:
        pyperclip.copy(password)
    except NameError:
        pass


window = Tk()

window.geometry("360x640")
window.configure(bg = "#ffffff")
window.title("Password Generator")

home = tk.Frame(window,bg="#ffffff")
home.place(x=0,y=0,width=360,height=640)

canvas = Canvas(
    home,
    bg = "#ffffff",
    height = 640,
    width = 360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

generate_image = PhotoImage(file = path + "generate.png")
generate_button = Button(
    canvas,
    image = generate_image,
    borderwidth = 0,
    highlightthickness = 0,
    command = generate,
    relief = "flat")

generate_button.place(
    x = 60, y = 435,
    width = 239,
    height = 62)

copy_image = PhotoImage(file = path + "copy.png")
copy_button = Button(
    canvas,
    image = copy_image,
    borderwidth = 0,
    highlightthickness = 0,
    command = copy_password,
    relief = "flat")

copy_button.place(
    x = 115, y = 537,
    width = 129,
    height = 56)

textbox_image = PhotoImage(file = path + "textbox.png")
textbox = canvas.create_image(
    182.5, 352.5,
    image = textbox_image)

textbox = Entry(
    canvas,
    bd = 0,
    bg = "#cbd7d5",
    highlightthickness = 0)

textbox.place(
    x = 35.0, y = 329,
    width = 295.0,
    height = 45)

for characters in keyboard_characters:
    textbox.bind(characters, lambda e: "break")  





background_img = PhotoImage(file = path + "main_widget.png")
background = canvas.create_image(
    181.0, 182.0,
    image=background_img)



#home.tkraise()




window.resizable(False, False)
window.mainloop()
