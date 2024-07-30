import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x150")
        
        self.label = tk.Label(root, text="Enter time in seconds:", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=10, font=("Helvetica", 12))
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Helvetica", 12))
        self.start_button.pack(pady=5)
        
        self.time_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.time_label.pack(pady=10)
        
    def start_timer(self):
        try:
            t = int(self.entry.get())
            self.countdown(t)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
    
    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.time_label.config(text=timer)
            self.root.update()
            time.sleep(1)
            t -= 1
        
        self.time_label.config(text="Time's up!")
        messagebox.showinfo("Countdown Timer", "Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
