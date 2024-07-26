from tkinter import *

window_width = 640
window_height = 480
main = Tk()
main.title("Gauge")
main.geometry("%dx%d" % (window_width, window_height))
canvas = Canvas(main, height=window_height, width=window_width)
canvas.create_arc(0, 100, 600, 650, start=75, extent=60, fill="green", outline="green")
canvas.create_arc(0, 100, 600, 650, start=60, extent=15, fill="yellow", outline="yellow")
canvas.create_arc(0, 100, 600, 650, start=45, extent=15, fill="red", outline="red")
for i in range(8):
    canvas.create_arc(50, 163, 550, 587, start=47 + i * 10.75, extent=10.75, fill="white")
canvas.create_line(250, 130, 300, 370, fill="black", width=10, arrow=FIRST, arrowshape=(12,15,12))
canvas.create_text(90,220, font="Poppins 15 bold",text="0")
canvas.create_text(510,220, font="Poppins 15 bold",text="100")
canvas.create_text(300,80, font="Poppins 20 italic bold",text="Humidity")
canvas.create_text(300,400, font="Poppins 15 bold",text="37%")
canvas.pack()
main.mainloop()
