import tkinter as tk
window = tk.Tk()
tk.Label(window, text="first name").grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)
entry.insert(0, "Hello")
label = tk.Label(window, text="tekst z entry")
label.grid(row=1, column=1)


def showData():
    label.config(text=entry.get())
    print(entry.get())
    entry.delete(0, "end")


tk.Button(window, text="show info", command=showData).grid(row=1)
window.mainloop()
