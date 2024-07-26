from tkinter import *


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def calc():
    if n.get().isnumeric():
        int_n = int(n.get())
        facto_label.config(text="The factorial of %d = %d" % (int_n, factorial(int_n)))
    else:
        facto_label.config(text="Non-valid value")
    n.set("")


window_width = 400
window_height = 300
main = Tk()
main.title("facto")
main.geometry("%dx%d" % (window_width, window_height))
main.resizable(True,False)
n = StringVar()
entry_of_n = Entry(main, textvariable=n)
label = Label(main, text="Enter value of integer N:", pady=10, padx=10)
facto_label = Label(main, text="Result is shown here")
calc_btn = Button(main, text="Calculate", command=calc)
label.grid(row=1, column=1)
entry_of_n.grid(row=1, column=2)
facto_label.grid(row=2, column=2)
calc_btn.grid(row=3, column=2)
main.mainloop()
