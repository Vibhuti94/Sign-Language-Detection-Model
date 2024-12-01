import tkinter as tk
from tkinter import ttk
import subprocess

def collect_data():
    subprocess.Popen(["python", "datacollection.py"])

def detect_sign():
    subprocess.Popen(["python", "test.py"])


root = tk.Tk()
root.title("Sign Language Detection")
root.geometry("400x200")  


style = ttk.Style()
style.configure('Custom.TButton', font=('Arial', 12), background='#4CAF50', foreground='black')


root.configure(background='#800080')


label = tk.Label(root, text="Welcome to Sign Language Detection!", font=('Arial', 14), bg='#800080', fg='white')
label.pack(pady=10)

collect_button = ttk.Button(root, text="Collect Data", command=collect_data, style='Custom.TButton')
collect_button.pack(pady=5, padx=20, ipadx=10, ipady=5, side=tk.LEFT)

detect_button = ttk.Button(root, text="Detect Sign", command=detect_sign, style='Custom.TButton')
detect_button.pack(pady=5, padx=20, ipadx=10, ipady=5, side=tk.RIGHT)


def button_pressed(event):
    event.widget.config(relief='sunken')

def button_released(event):
    event.widget.config(relief='raised')

collect_button.bind('<ButtonPress-1>', button_pressed)
collect_button.bind('<ButtonRelease-1>', button_released)

detect_button.bind('<ButtonPress-1>', button_pressed)
detect_button.bind('<ButtonRelease-1>', button_released)


root.mainloop()
