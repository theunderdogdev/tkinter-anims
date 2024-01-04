from tkinter import *
root = Tk()

def update(event):
    var.set(str(len(msg.get("1.0", 'end-1c'))))

msgLabel = Label(text="Message")
msgLabel.grid(row=0, column=0)
msg = Text(width=40, height=4, wrap="word")
msg.grid(row=0, column=1, padx=10, pady=5)

var = StringVar()

#Try to display number of characters within message to user
charCount = Label(textvariable=var)
charCount.grid(row=1, column=1, pady=5, padx=5)

msg.bind("<KeyRelease>", update)

root.mainloop()