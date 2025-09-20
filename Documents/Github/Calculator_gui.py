import tkinter as tk
import math

# ---------------- Functions ----------------
def press(key):
    entry.insert(tk.END, str(key))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def equalpress():
    try:
        expression = entry.get()
        # Replace '√' with math.sqrt
        expression = expression.replace('√', 'math.sqrt')
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def toggle_dark_mode():
    if root['bg'] == 'white':
        root.config(bg='black')
        entry.config(bg='gray20', fg='white', insertbackground='white')
        for btn in buttons.values():
            btn.config(bg='gray30', fg='white')
    else:
        root.config(bg='white')
        entry.config(bg='white', fg='black', insertbackground='black')
        for btn in buttons.values():
            btn.config(bg='SystemButtonFace', fg='black')

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Advanced Python GUI Calculator")
root.geometry("360x500")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15, padx=5, pady=5)

# ---------------- Buttons ----------------
button_texts = [
    ('7', '8', '9', '/', 'C'),
    ('4', '5', '6', '*', '⌫'),
    ('1', '2', '3', '-', '√'),
    ('0', '.', '%', '+', '='),
    ('Dark Mode',)
]

buttons = {}

for r, row in enumerate(button_texts, 1):
    for c, text in enumerate(row):
        if text == '=':
            action = equalpress
        elif text == 'C':
            action = clear
        elif text == '⌫':
            action = backspace
        elif text == 'Dark Mode':
            action = toggle_dark_mode
        else:
            action = lambda x=text: press(x)
        
        btn = tk.Button(root, text=text, width=7, height=2, font=("Arial", 14), command=action)
        if text == 'Dark Mode':
            btn.grid(row=r, column=0, columnspan=5, sticky="we", padx=3, pady=3)
        else:
            btn.grid(row=r, column=c, padx=3, pady=3)
        buttons[text] = btn

# ---------------- Run App ----------------
root.mainloop()
