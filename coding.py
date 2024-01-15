import tkinter as tk

from tkinter import ttk



# window

window = tk.Tk()

window.geometry("600x500")

window.title("Event Binding")



# widgets

text = tk.Text(master=window)

text.pack()



entry = ttk.Entry(master=window)

entry.pack()



button = ttk.Button(master=window, text="A button")

button.pack()



# events

window.bind('<Shift-KeyPress-a>', lambda event: print(event))

#window.bind('<KeyPress>', lambda event: print("a button was pressed " + event.char))



def getPostion(event):

    print("x: " + str(event.x) + ", y: " + str(event.y))




window.mainloop()
