# -- coding:utf-8 --

import tkinter
import sys

def on_pressed(event):
    sys.exit()
    return

window = tkinter.Tk()
label = tkinter.Label(window, text = "マウスボタンを押すと終了")
label.bind("<Button-1>", on_pressed)
label.pack()

window.mainloop()