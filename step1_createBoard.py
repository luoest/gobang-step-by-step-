from tkinter import *

tk = Tk()
frame = Frame(tk, padx = 20, pady = 20, bg = 'burlywood4')
frame.pack()
cv = Canvas(frame, width = 510, height = 550, bg = 'burlywood')
for i in range(16):
    cv.create_line(30, 30*i+80, 480, 30*i+80)
for i in range(16):
    cv.create_line(30*i+30, 80, 30*i+30, 530)








cv.pack()
tk.mainloop()