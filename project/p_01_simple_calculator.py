"""
Create a simple Tkinter application that .....simple calculator???
"""

from tkinter import Tk, Button, Label, Entry


root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def handle_button_click(button_value):
    """
    This function is called when a button is clicked.
    It clears the entry widget and inserts the value of the button.
    """
    # e.delete(0, 'end')
    e.insert(0, str(button_value))

def button_act():
    return


# Define Button
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: handle_button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: handle_button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: handle_button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: handle_button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: handle_button_click(5))
button_6 = Button(root, text="7", padx=20, pady=10, command=lambda: handle_button_click(6)) 
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: handle_button_click(7)) 
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: handle_button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: handle_button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: handle_button_click(0))

button_add = Button(root, text="+", padx=19, pady=10, command=button_act)
button_equal = Button(root, text="=", padx=50, pady=10, command=button_act)
button_clear = Button(root, text="Clear", padx=40, pady=10, command=button_act)


# Put the buttons on the screen

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, columnspan=2, column=1)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, columnspan=2, column=1)


root.mainloop()
