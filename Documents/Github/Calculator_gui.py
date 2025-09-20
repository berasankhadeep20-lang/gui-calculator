import tkinter as tk

# Function to update expression in the entry box
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

# Function to evaluate expression
def equalpress():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear entry box
def clear():
    entry.delete(0, tk.END)

# Main GUI window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=5, pady=5)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        action = equalpress
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, width=7, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=3, pady=3)

# Clear button
tk.Button(root, text="C", width=32, height=2, font=("Arial", 14),
          command=clear).grid(row=5, column=0, columnspan=4, padx=3, pady=3)

# Run the app
root.mainloop()
