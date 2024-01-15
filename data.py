import tkinter as tk
from tkinter import ttk

def buttonfuntion():
    newText = entry.get()
    label['text'] = newText
    entry['state'] = 'disable'
def buttonfuntion1():
    ogText = ('some text')
    label['text'] = ogText
    entry['state'] = 'disable'





window = tk.Tk()
window.title('Getting and Setting widgets')

label = ttk.Label(master = window, text = 'some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'a button', command = buttonfuntion)
button.pack()
button = ttk.Button(master = window, text = 'Reset', command = buttonfuntion1)
button.pack()

window.mainloop()
