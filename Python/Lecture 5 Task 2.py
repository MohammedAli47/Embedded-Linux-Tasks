from tkinter import *


def led_off_command():
    canvas.delete("all")
    canvas.create_oval(110, 80, 190, 160, fill="white")
    label.config(text="Led is Off")


def led_on_command():
    canvas.delete("all")
    canvas.create_oval(110, 80, 190, 160, fill="red")
    label.config(text="Led is On")


window_width = 300
window_height = 300
main = Tk()
main.title("LED")
main.geometry("%dx%d" % (window_width, window_height))
canvas = Canvas(main, height=window_height, width=window_width)
led_off = Button(main, text="Led Off", width=6, command=led_off_command).pack(side="bottom")
led_on = Button(main, text="Led On", width=6, command=led_on_command).pack(side="bottom")
label = Label(main, text="")
label.pack(side="bottom")
canvas.pack()
main.mainloop()
