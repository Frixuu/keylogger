#!/usr/bin/python3

from tkinter import messagebox, Tk
import keyboard
import os

buffer_length = 20
buffer = " " * buffer_length
triggers = ["tr1", "w"]

def onKeyPress(event):
  global buffer
  buffer = buffer[-buffer_length+1:] + event.name
  print(buffer)
  for word in triggers:
    if buffer.endswith(word):
      Tk().withdraw()
      messagebox.showinfo("Title", "Contents")

keyboard.on_press(onKeyPress)
keyboard.wait()