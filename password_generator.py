import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password():
    length = int(length_var.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
    
    if not char_pool:
        messagebox.showerror("Error", "No character set selected!")
        return
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

root = tk.Tk()
root.title("Random Password Generator")

tk.Label(root, text="Password").grid(row=0, column=0, padx=5, pady=5)
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, state='readonly', width=30).grid(row=0, column=1, padx=5, pady=5)

tk.Button(root, text="Copy", command=copy_to_clipboard).grid(row=0, column=2, padx=5, pady=5)
tk.Button(root, text="Generate", command=generate_password).grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="Length").grid(row=1, column=0, padx=5, pady=5)
length_var = tk.StringVar(value="8")
ttk.Combobox(root, textvariable=length_var, values=[8, 12, 16, 20]).grid(row=1, column=1, padx=5, pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Radiobutton(root, text="Low", variable=symbols_var, value=False).grid(row=2, column=1)
tk.Radiobutton(root, text="Medium", variable=symbols_var, value=True).grid(row=2, column=2)
tk.Radiobutton(root, text="Strong", variable=symbols_var, value=True).grid(row=2, column=3)

root.mainloop()
