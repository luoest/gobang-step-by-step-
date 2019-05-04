from tkinter import *
from tkinter.messagebox import *
import winsound

tk = Tk()
frame = Frame(tk, padx=20, pady=20, bg='burlywood4')
frame.pack()
cv = Canvas(frame, width=510, height=550, bg='burlywood')
for i in range(16):
    cv.create_line(30, 30 * i + 80, 480, 30 * i + 80)
for i in range(16):
    cv.create_line(30 * i + 30, 80, 30 * i + 30, 530)

map = []
for i in range(1, 17):
    for j in range(2, 18):
        map.append([i, j])
MAP = map.copy()


def winning_info():
    global stop
    if flag == 0:
        winsound.Beep(900, 500)
        showinfo('提示', '本局白方获胜！')
        stop = 1
    elif flag == 1:
        winsound.Beep(900, 500)
        showinfo('提示', '本局黑方获胜。')
        stop = 1


def judeWinLose():
    global flag
    j = 0
    while j < len(map):  # in while block, it is to judge y-axis winning, while 循环内为y轴方向的判断。其余判断另外三个方向。
        for i in range(j, j + 12):
            if map[i] == 0 and map[i + 1] == 0 and map[i + 2] == 0 and map[i + 3] == 0 and map[i + 4] == 0:
                flag = 0
                winning_info()

            elif map[i] == 1 and map[i + 1] == 1 and map[i + 2] == 1 and map[i + 3] == 1 and map[i + 4] == 1:
                flag = 1
                winning_info()
        j += 16

    try:
        i = 0
        while i < len(map):
            if map[i] == 0 and map[i + 15] == 0 and map[i + 30] == 0 and map[i + 45] == 0 and map[i + 60] == 0:
                flag = 0
                winning_info()
            elif map[i] == 0 and map[i + 16] == 0 and map[i + 32] == 0 and map[i + 48] == 0 and map[i + 64] == 0:
                flag = 0
                winning_info()
            elif map[i] == 0 and map[i + 17] == 0 and map[i + 34] == 0 and map[i + 51] == 0 and map[i + 68] == 0:
                flag = 0
                winning_info()

            elif map[i] == 1 and map[i + 15] == 1 and map[i + 30] == 1 and map[i + 45] == 1 and map[i + 60] == 1:
                flag = 1
                winning_info()
            elif map[i] == 1 and map[i + 16] == 1 and map[i + 32] == 1 and map[i + 48] == 1 and map[i + 64] == 1:
                flag = 1
                winning_info()
            elif map[i] == 1 and map[i + 17] == 1 and map[i + 34] == 1 and map[i + 51] == 0 and map[i + 68] == 1:
                flag = 1
                winning_info()
            i += 1
    except:
        IndexError


color = ['white', 'black']
colorTag = 0
steps = []
stepper = []
stop = 0  # 0时为可以走棋，1 为已不能走棋。
j_list = []  # 保存走的步数
flash_text = [['^^该白方走棋了^^', '^^该黑方走棋了^^'], ['^^本局黑方获胜^^', '^^本局白方获胜^^']]

def moveChess(event):
    global mapper, stop
    """
    Call to move chess, 通过事件绑定，点击坐标下子。

    """
    x = event.x // 30
    y = event.y // 30
    # cannot put chesses outside board. 超过棋盘不能落子
    if [x, y] not in map:
        winsound.Beep(500, 100)
    # cannot put chesses where there is one. 有棋子出不能落子
    elif [x, y] in stepper:
        winsound.Beep(500, 100)
    else:
        winsound.Beep(100, 100)

        if stop == 0:
            # create chess, change color by colorTag. 创建棋子，通过colorTag改变棋子颜色。
            id = cv.create_oval(x * 30 - 15, y * 30 + 5, x * 30 + 15, y * 30 + 35, fill=color[colorTag])

            print(id, x, y)
            steps.append([id, x, y])
            stepper.append([x, y])

            i = 0
            while i < len(map):
                if map[i] == [x, y]:
                    map[i] = colorTag
                    j_list.append(i)
                i += 1
            mapper = map.copy()
            print(map)

            colorTurn()
            drawMap()
            judeWinLose()

            font = ('simfang', 19, 'normal')
            flash = Label(frame, text=flash_text[stop][colorTag], bg=bg, fg=color[colorTag], font=font)
            flash.place(x=150, y=5)

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
    """
    draw board map and show chess's posision
    画出棋盘，实时显示棋子位置
    """
    count = 0
    for i in range(len(mapper)):
        if mapper[i] != 0 and mapper[i] != 1:
            mapper[i] = '*'
        print(mapper[i], end=' ')
        count += 1
        if count % 16 == 0:
            print()


def back():
    global map, stop
    """
    call for back, 用于悔棋

    """
    if len(steps) == 0 or len(stepper) == 0:
        showwarning('提示', '棋盘上已经没有棋子了!')
    else:
        backing = steps.pop()
        stepper.pop()
        id = backing[0]
        x = backing[1]
        y = backing[2]
        j = j_list.pop()
        cv.delete(id)
        map[j] = [x, y]
        stop = 0
        colorTurn()


def restart():
    global map, stop
    """
    call to restar game. 开始新游戏

    """
    map = []
    for i in range(1, 17):
        for j in range(2, 18):
            map.append([i, j])

    for step in steps:
        id = step[0]
        cv.delete(id)
    steps.clear()
    stepper.clear()
    j_list.clear()
    stop = 0
    colorTurn()

bg = 'seagreen'
fg = 'yellow'
font = ('simfang', 20, 'bold')
functionArea = Canvas(frame, width = 510, height = 50, bg = bg)
functionArea.place(x = 0, y = 0)
Button(frame, text = '悔棋', command = back, bg = bg, fg = fg, font = font).place(x=70, y = 3)
Button(frame, text = '重开', command = restart, bg = bg, fg = fg, font = font).place(x=370, y = 3)


cv.bind('<Button - 1>', moveChess)
# cv.bind('<Button - 2>', restart)
# cv.bind('<Button - 3>', back)
cv.pack()
tk.mainloop()