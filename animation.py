import random
from tkinter import BOTH, Tk, Label, StringVar, Widget
from tkinter.font import Font
from random import random, choice


grid = []


class AnimFrame:
    def __init__(self, parent: Widget, SNOW_DENSITY, DELAY_MS, CHAR_WIDTH=85) -> None:
        self.__DENSITY = SNOW_DENSITY
        self.__CW = CHAR_WIDTH
        self.__DELAY = DELAY_MS
        self.data_grid = []
        self.__var = StringVar()
        self.f_config = Font(size=12)
        self.__label = Label(
            master=parent,
            textvariable=self.__var,
            font=self.f_config,
        )
        self.__label.pack(expand=1, fill=BOTH, padx=5, pady=5)
        self.__label.bind("<Visibility>", self.init_grid)
        self.__FLAKES = ["❆", "❇", "○", "•", "❄️"]

    def init_grid(self, *args):
        fh = self.f_config.metrics("linespace")
        lines = self.__label.winfo_height() // fh
        for _ in range(lines):
            grid.append(" " * self.__CW)
        self.__animate()

    def __animate(self):
        row = []
        self.__var.set("")
        for _ in range(self.__CW):
            if random() < self.__DENSITY / 100:
                row.append(choice(self.__FLAKES))
            else:
                row.append(" ")
        grid.insert(0, "".join(row))
        self.__var.set("\n".join(grid))
        grid.pop()
        self.__label.after(self.__DELAY, self.__animate)


if __name__ == "__main__":
    win = Tk()
    anim = AnimFrame(win)
    win.geometry("700x700")
    win.resizable(False, False)
    win.mainloop()
