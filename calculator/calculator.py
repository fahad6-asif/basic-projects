import tkinter as tk

def press(v):
    entry_box.insert(tk.END, v)

def clear():
    entry_box.delete(0, tk.END)

def equal():
    try:
        r = eval(entry_box.get())
        clear()
        entry_box.insert(0, r)
    except:
        clear()

window = tk.Tk()
window.title("Calculator")

entry_box = tk.Entry(window, font=("Arial", 18), justify="right", width=18)
entry_box.grid(row=0, column=0, columnspan=4)

tk.Button(window, text="7", width=5, height=2, command=lambda: press("7")).grid(row=1, column=0)
tk.Button(window, text="8", width=5, height=2, command=lambda: press("8")).grid(row=1, column=1)
tk.Button(window, text="9", width=5, height=2, command=lambda: press("9")).grid(row=1, column=2)
tk.Button(window, text="/", width=5, height=2, command=lambda: press("/")).grid(row=1, column=3)

tk.Button(window, text="4", width=5, height=2, command=lambda: press("4")).grid(row=2, column=0)
tk.Button(window, text="5", width=5, height=2, command=lambda: press("5")).grid(row=2, column=1)
tk.Button(window, text="6", width=5, height=2, command=lambda: press("6")).grid(row=2, column=2)
tk.Button(window, text="*", width=5, height=2, command=lambda: press("*")).grid(row=2, column=3)

tk.Button(window, text="1", width=5, height=2, command=lambda: press("1")).grid(row=3, column=0)
tk.Button(window, text="2", width=5, height=2, command=lambda: press("2")).grid(row=3, column=1)
tk.Button(window, text="3", width=5, height=2, command=lambda: press("3")).grid(row=3, column=2)
tk.Button(window, text="-", width=5, height=2, command=lambda: press("-")).grid(row=3, column=3)

tk.Button(window, text="0", width=5, height=2, command=lambda: press("0")).grid(row=4, column=0)
tk.Button(window, text="C", width=5, height=2, command=clear).grid(row=4, column=1)
tk.Button(window, text="=", width=5, height=2, command=equal).grid(row=4, column=2)
tk.Button(window, text="+", width=5, height=2, command=lambda: press("+")).grid(row=4, column=3)

window.mainloop()
