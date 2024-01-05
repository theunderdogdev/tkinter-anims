from tkinter import Tk
from animation import AnimFrame

if __name__ == "__main__":
    win = Tk()
    frame = AnimFrame(win, SNOW_DENSITY=2, DELAY_MS=100, CHAR_WIDTH=100)
    win.geometry("700x700")
    win.resizable(False, False)
    win.mainloop()
