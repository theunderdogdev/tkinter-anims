import os
import random
import time
from tkinter import Event, Misc, Tk, Frame, Label, StringVar
from tkinter.font import Font
from math import ceil
SNOW_DENSITY = 2
DELAY = 500
chars = 100
snowflakes = ["❆", "❇", "○", "•", '❄️']
grid = []

def _append():
    row = []
    str_var.set('')
    for _ in range(chars):
        if random.random() < SNOW_DENSITY / 100:
            row.append(random.choice(snowflakes))
        else:
            row.append(' ')
    grid.insert(0, ''.join(row))
    str_var.set('\n'.join(grid))
    grid.pop()
    win.after(DELAY, _append)


def start_anim(evt: Event):
    label: Label = evt.widget
    lines = label.winfo_height() // f.metrics('linespace')
    for _ in range(lines):
        grid.append(' ' * chars)
    _append()

win = Tk()
f = Font(win, size=15)
str_var = StringVar(win, name='anim')
lab = Label(textvariable=str_var, font=f)
lab.pack(expand=1, fill='both', padx=5, pady=5)
win.geometry('700x700')
win.resizable(False, False)
lab.bind('<Visibility>', lambda evt: start_anim(evt))

# win.after(ms=DELAY, func=_append)
win.mainloop()

# grid = []

# for _ in range(h):
#     grid.append([" "] * w)


# def draw_grid():
#     os.system('echo -n "\033c\033[3J')
#     print("\033[?25l")
#     output = ""
#     for row in grid:
#         output += "".join(row) + "\n"
#         output = output.strip("\n")
#         print(output, end="")


# draw_grid()

# while True:
#     row = []
#     for _ in range(w):
#         if random.random() < SNOW_DENSITY / 100:
#             row.append(random.choice(snowflakes))
#         else:
#             row.append(" ")
#     grid.insert(0, row)
#     draw_grid()
#     grid.pop()
#     time.sleep(DELAY)
