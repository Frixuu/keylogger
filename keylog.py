#!/usr/bin/python3

from tkinter import messagebox, Tk
import keyboard
import os

# Customize your trigger words and popup contents here
triggers = ["forbidden", "555-02", "55502", "Smith"]
popup_title = "Title"
popup_body = "You should not do that!"

max_buffer_length = 50
buffer = ""

def hook(event : keyboard.KeyboardEvent):
  global buffer
  key = event.name
  if key == "space":
    key = " "
  elif key == "backspace":
    buffer = buffer[:-1]
    return
  elif key.endswith("shift") or key.startswith("alt"):
    return
  buffer = buffer[-max_buffer_length+1:] + key
  # print(buffer)
  for word in triggers:
    if buffer.endswith(word):
      Tk().withdraw()
      messagebox.showinfo(popup_title, popup_body)

keyboard.on_press(hook)
keyboard.wait()