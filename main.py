from tkinter import Tk
from animation import AnimFrame

if __name__ == "__main__":
    win = Tk()
    frame = AnimFrame(win, SNOW_DENSITY=0.5, DELAY_MS=250)
    win.geometry("700x700")
    win.resizable(False, False)
    win.mainloop()
