# Learn Python Tkinter

Welcome to the "Learn Python Tkinter" guide! This repository is designed to help you get started with creating graphical user interfaces (GUIs) using the Tkinter library in Python. Tkinter is the standard GUI library for Python, and it is a great way to build simple and intuitive interfaces for your applications.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Examples](#examples)
  - [Hello World](#hello-world)
  - [Grid Layout](#grid-layout)
  - [Buttons](#buttons)
  - [Entry Widgets](#entry-widgets)
  - [Simple Calculator](#simple-calculator)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Tkinter is a powerful library that allows you to create desktop applications with Python. It is simple to use and comes bundled with Python, so there is no need to install anything extra. This guide provides a series of examples to help you understand the basics of Tkinter and how to create various components for your GUI applications.

## Getting Started

To use Tkinter, you need to have Python installed on your computer. Tkinter comes pre-installed with Python, so you don't need to install it separately. You can verify your Python installation by running the following command:

```sh
python --version
```

If Python is installed, you can start creating your Tkinter applications by importing the library:

## Examples

### Hello World

The "Hello World" example is the simplest Tkinter application. It creates a window with a label that displays the text "Hello World!".

```python
from tkinter import Tk, Label

root = Tk()
label = Label(root, text="Hello World!")
label.pack()
root.mainloop()
```

### Grid Layout

The Grid layout manager allows you to create a more complex layout by arranging widgets in a grid.

```python
from tkinter import Tk, Label

root = Tk()
label1 = Label(root, text="Row 0, Column 0")
label2 = Label(root, text="Row 1, Column 1")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

root.mainloop()
```

### Buttons

Buttons are interactive elements that can trigger functions when clicked.

```python
from tkinter import Tk, Button

def on_click():
    print("Button clicked!")

root = Tk()
button = Button(root, text="Click me", command=on_click)
button.pack()

root.mainloop()
```

### Entry Widgets

Entry widgets allow users to input text data.


from tkinter import Tk, Entry, Button, Label

def show_message():
    message = f"Hello {entry.get()}!"
    label = Label(root, text=message)
    label.pack()

```python
root = Tk()
entry = Entry(root, width=50)
entry.pack()
button = Button(root, text="Enter your name", command=show_message)
button.pack()

root.mainloop()
```

Simple Calculator
A simple calculator application that performs basic arithmetic operations.

```python
from tkinter import Tk, Button, Entry, Label

def add():
    result = float(entry1.get()) + float(entry2.get())
    label_result.config(text=f"Result: {result}")

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    label_result.config(text=f"Result: {result}")

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    label_result.config(text=f"Result: {result}")

def divide():
    result = float(entry1.get()) / float(entry2.get())
    label_result.config(text=f"Result: {result}")

root = Tk()
entry1 = Entry(root, width=10)
entry1.pack()
entry2 = Entry(root, width=10)
entry2.pack()

button_add = Button(root, text="+", command=add)
button_add.pack()

button_subtract = Button(root, text="-", command=subtract)
button_subtract.pack()

button_multiply = Button(root, text="*", command=multiply)
button_multiply.pack()

button_divide = Button(root, text="/", command=divide)
button_divide.pack()

label_result = Label(root, text="Result:")
label_result.pack()

root.mainloop()
```


