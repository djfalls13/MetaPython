#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

# tkinter._test()

# ---------- MULTIPLE COMPONENTS  ----------
# Some of the different Widgets : Button, Label,
# Canvas, Menu, Text, Scale, OptionMenu, Frame,
# CheckButton, LabelFrame, MenuButton, PanedWindow,
# Entry, ListBox, Message, RadioButton, ScrollBar,
# Bitmap, SpinBox, Image

root = Tk()

# Give your app a title
root.title("First GUI")

# Frame widgets surround other widgets
frame = Frame(root)

# We'll use a TkInter variable for our label text
# so we can change it with set
labelText = StringVar()

# Create a label and button object
# You can set attributes on creation or by calling
# methods

label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

# Change the label text
labelText.set("I am a label")

# Define where the widgets should be placed and
# how they should be stretched to fill the space
Label(frame, text="A Bunch of Buttons").pack()
Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B3").pack(side=RIGHT, fill=X)
Button(frame, text="B4").pack(side=LEFT, fill=X)

frame.pack()

root.mainloop()