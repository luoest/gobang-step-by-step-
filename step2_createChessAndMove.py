from tkinter import *

tk = Tk()
frame = Frame(tk, padx = 20, pady = 20, bg = 'burlywood4')
frame.pack()
cv = Canvas(frame, width = 510, height = 550, bg = 'burlywood')
for i in range(16):
    cv.create_line(30, 30*i+80, 480, 30*i+80)
for i in range(16):
    cv.create_line(30*i+30, 80, 30*i+30, 530)

color = ['white', 'black']
colorTag = 0
def moveChess(event):
    """
    Call to move chess, 通过事件绑定，点击坐标下子。

    """
    x = event.x // 30
    y = event.y // 30
    # create chess, change color by colorTag. 创建棋子，通过colorTag改变棋子颜色。
    cv.create_oval(x*30-15, y*30+5, x*30+15, y*30+35, fill = color[colorTag])

    colorTurn()


def colorTurn():
    """
    shift between white chess and black chess. 切换黑白棋子
    :return:
    """
    global colorTag
    if colorTag == 0:
        colorTag = 1
    else:
        colorTag = 0





cv.bind('<Button - 1>', moveChess)
cv.pack()
tk.mainloop()