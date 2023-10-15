import tkinter as tk


def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("Calculator")


entry = tk.Entry(window, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)


button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button_text in button_texts:
    tk.Button(window, text=button_text, width=5, height=2, font=("Arial", 16),
              command=lambda text=button_text: entry.insert(tk.END, text) if text != '=' else calculate()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1


window.mainloop()
