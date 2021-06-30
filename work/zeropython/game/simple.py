# encoding:utf-8
from tkinter import *

# ウインドウを作成、Canvasを貼り付け
win = Tk()
WIDTH = 600
HEIGHT = 400

cv = Canvas(win, width = WIDTH, height = HEIGHT)
cv.pack()

for x in range(0, WIDTH, 50):
    for y in range(0, HEIGHT, 50):
        cv.create_line(x, 0, x, HEIGHT, fill = "red")
        cv.create_line(0, y, WIDTH, y, fill = "blue")

win.mainloop()
