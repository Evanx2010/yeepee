import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("buttons")
window.geometry('600x400')

def buttonFunction1():
    print("check button value = true " + str(radioVar1.get()))
    checkVar1.set(False)
def buttonfuntion():
    print("I clicked on button")
    print("radio var selected" + radioVar.get())

button = ttk.Button(master=window, text='A button', command=buttonfuntion)
button.pack()

checkVar = tk.IntVar(value=10)
checkButton = ttk.Checkbutton(
    master=window,
    text="checkbox 1",
    command=lambda: print(checkVar.get()),
    variable=checkVar,
    onvalue=10,
    offvalue=5)
checkButton.pack()


radioVar = tk.StringVar()
radio1 = ttk.Radiobutton(master=window, text = "Radiobutton", value="radio1",variable=radioVar, command=lambda: print(radioVar.get()))
radio1.pack()
radio2 = ttk.Radiobutton(master=window, text = "Radiobutton 1", value=2, variable=radioVar,command=lambda: print(radioVar.get()))
radio2.pack()

checkVar1 = tk.BooleanVar()
checkButton1 = tk.Checkbutton(
    master=window,
    text="checkbox 1",
    command=lambda: print(radioVar1.get()),
    variable=checkVar1)
checkButton1.pack()
radioVar1 = tk.StringVar()
radio3 = ttk.Radiobutton(master=window, text="Radiobutton A", value="radio A selected", variable=radioVar1, command=buttonFunction1)
radio3.pack()
radio4 = ttk.Radiobutton(master=window, text="Radiobutton B", value="Radio B selected", variable=radioVar1, command=buttonFunction1)
radio4.pack()



window.mainloop()
