#coding=utf-8

import pyxhook
import os

klawisze = "000000"
slowa = ["aannn1", "aammm2", "555032", "555-03"]

def OnKeyPress(event):
  global klawisze
  temp = klawisze[1:] + chr(event.Ascii)
  klawisze = temp
  for slowo in slowa:
    if slowo == klawisze:
      os.system("python /home/frix/dialog.py")

hook = pyxhook.HookManager()
hook.KeyDown=OnKeyPress
hook.HookKeyboard()
hook.start()
