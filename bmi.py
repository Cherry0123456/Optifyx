import tkinter as tk
from tkinter import messagebox
import math

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("Error", "Please enter valid positive numbers!")
            return

        bmi = round(weight / (height ** 2), 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Function for calculator button clicks
def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("BMI & Scientific Calculator")
root.geometry("500x500")
root.configure(bg="#DFFFD6")

# BMI Calculator UI
tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="#DFFFD6").pack()

frame_bmi = tk.Frame(root, bg="#DFFFD6")
frame_bmi.pack(pady=10)

tk.Label(frame_bmi, text="Weight (kg):", bg="#DFFFD6").grid(row=0, column=0)
weight_entry = tk.Entry(frame_bmi)
weight_entry.grid(row=0, column=1)

tk.Label(frame_bmi, text="Height (m):", bg="#DFFFD6").grid(row=1, column=0)
height_entry = tk.Entry(frame_bmi)
height_entry.grid(row=1, column=1)

tk.Button(frame_bmi, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#DFFFD6")
result_label.pack()

# Scientific Calculator UI
tk.Label(root, text="Scientific Calculator", font=("Arial", 16, "bold"), bg="#DFFFD6").pack()

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), bd=5, relief=tk.SUNKEN, justify="right")
entry.pack(pady=10, fill="x")

button_frame = tk.Frame(root, bg="#DFFFD6")
button_frame.pack()

buttons = [
    ['7', '8', '9', '+', '-', '*'],
    ['4', '5', '6', '/', '(', ')'],
    ['1', '2', '3', 'sin', 'cos', 'tan'],
    ['0', '.', 'pi', 'sqrt', 'log', '^'],
    ['C', '=', 'asin', 'acos', 'atan']
]

for row in buttons:
    frame = tk.Frame(button_frame, bg="#DFFFD6")
    frame.pack(side="top")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 14), width=5, height=2, bg="#F0F0F0")
        btn.pack(side="left", padx=5, pady=5)
        btn.bind("<Button-1>", on_button_click)

root.mainloop()
