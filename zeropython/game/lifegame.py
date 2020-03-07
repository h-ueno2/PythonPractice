# encoding:utf-8
from random import randint
from tkinter import *

# 変数定数定義

COLS, ROWS = [30, 20] #ステージサイズ
CW = 20 #セルの描画サイズ
data = [] # ステージデータ
for y in range(0, ROWS):
    data.append([(randint(0, 9) == 0) for x in range(0, COLS)])

win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

def check(x, y):
    # 周囲の生存セルを数える
    cnt = 0
    tbl = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    for t in tbl:
        xx, yy = [x + t[0], y + t[1]]
        if 0 <= xx < COLS and 0 <= yy < ROWS:
            if data[yy][xx]:
                cnt += 1
    # ルールに沿って次世代の生死を決める
    if cnt == 3: 
        return True # 誕生
    if data[y][x]:
        if 2 <= cnt <= 3: 
            return True
        return False
    return data[y][x]

# データを次の世代に進める
def next_turn():
    global data
    data2 = []
    for y in range(0, ROWS):
        data2.append([check(x, y) for x in range(0, COLS)])
    data = data2 # データの内容を差し替え

def draw_stage():
    cv.delete('all')
    for y in range(0, ROWS):
        for x in range(0, COLS):
            if not data[y][x]:
                continue
            x1, y1 = [x * CW, y * CW]
            cv.create_oval(x1, y1, x1 + CW, y1 + CW, fill="red", width=0)

def game_loop():
    next_turn()
    draw_stage()
    win.after(300, game_loop)

game_loop()
win.mainloop()
