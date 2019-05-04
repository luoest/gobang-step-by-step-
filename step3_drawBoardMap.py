from tkinter import *
from tkinter.messagebox import *
import winsound

tk = Tk()
frame = Frame(tk, padx = 20, pady = 20, bg = 'burlywood4')
frame.pack()
cv = Canvas(frame, width = 510, height = 550, bg = 'burlywood')
for i in range(16):
    cv.create_line(30, 30*i+80, 480, 30*i+80)
for i in range(16):
    cv.create_line(30*i+30, 80, 30*i+30, 530)

map = []
for i in range(1, 17):
    for j in range(2, 18):
        map.append([i, j])
MAP = map.copy()


color = ['white', 'black']
colorTag = 0
steps = []
stepper = []
def moveChess(event):
    global mapper
    """
    Call to move chess, 通过事件绑定，点击坐标下子。

    """
    x = event.x // 30
    y = event.y // 30
    if [x, y] not in map:
        winsound.Beep(500, 100)
    elif [x, y] in stepper:
        winsound.Beep(500, 100)
    else:
        winsound.Beep(100, 100)
        # create chess, change color by colorTag. 创建棋子，通过colorTag改变棋子颜色。
        id = cv.create_oval(x*30-15, y*30+5, x*30+15, y*30+35, fill = color[colorTag])

        print(id, x, y)
        steps.append([id, x, y])
        stepper.append([x, y])

        i = 0
        while i < len(map):
            if map[i] == [x, y]:
                map[i] = colorTag
            i += 1
        mapper = map.copy()
        print(map)
        colorTurn()
        drawMap()


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

def drawMap():
    count = 0
    for i in range(len(mapper)):
        if mapper[i] != 0 and mapper[i] != 1:
            mapper[i] = '*'
        print(mapper[i], end = ' ')
        count += 1
        if count % 16 == 0:
            print()


cv.bind('<Button - 1>', moveChess)
cv.pack()
tk.mainloop()