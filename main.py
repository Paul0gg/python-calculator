import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to take user input
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Function to add buttons
r = 1
c = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=10, command=calculate).grid(row=r, column=c, columnspan=2)
    else:
        tk.Button(root, text=button, width=5, command=lambda x=button: entry.insert(tk.END, x)).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=r, column=0, columnspan=4)

root.mainloop()
