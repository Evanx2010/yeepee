import tkinter as tk
from tkinter import ttk

def buttonfunction():
    print(VarVar.get())
    VarVar.set("button pressed")

window = tk.Tk()
window.title('tkinter variable')

VarVar = tk.StringVar(value='start value')

label = ttk.Label(master=window, textvariable=VarVar)
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text = "a button", command=buttonfunction)
button.pack()

VarVar2 = tk.IntVar(value=0)

exercise_label = ttk.Label(master=window, textvariable=VarVar2)
exercise_label.pack()
entry = ttk.Entry(master=window, textvariable=VarVar2)
entry.pack()

entry = ttk.Entry(master=window, textvariable=VarVar2)
entry.pack()

window.mainloop()
