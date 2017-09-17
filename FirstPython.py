# -*- coding:utf-8 -*-
import tkinter #モジュールの読み込み


def on_clicked():
    print("ボタンが押された!")

window = tkinter.Tk()
label = tkinter.Label(window, text = "サンプル")
label.pack() # ---(1)
button = tkinter.Button(window, 
                        text = "ボタンです。押してください",
                        command = on_clicked)
button.pack()

tkinter.Button(window, text = "ボタン").pack()
tkinter.Checkbutton(window, text = "チェックボタン").pack()

entry = tkinter.Entry(window)
entry.insert(tkinter.END, "エントリ")
entry.pack()

frame = tkinter.LabelFrame(window, text = "ラベル付きフレーム")
frame.pack()
tkinter.Label(frame, text = "ラベル").pack()

listbox = tkinter.Listbox(window, height = 3)
listbox.insert(tkinter.END, "リストボックス")
listbox.insert(tkinter.END, "項目2")
listbox.pack()

tkinter.Scale(window, orient = tkinter.HORIZONTAL).pack()
tkinter.Spinbox(window).pack()

window.mainloop()

