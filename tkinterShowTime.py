"""
Display time in a tkiinter label
- display continuoously updates
"""

import tkinter.messagebox
import tkinter as tk
import datetime

root = tk.Tk()
root.title("Dashboard")
root.geometry("270x175")
root.config(bg="white", highlightbackground="blue", highlightthickness=2)
root.eval('tk::PlaceWindow . top')

# creating values for entry
now = datetime.datetime.now()

lbl2 = tk.Label(root, text=now, font=("Bell MT", 14, "bold"), bg="white",fg="black")
lbl2.place(x=15, y=70)

while True:
  lbl2.configure(text=datetime.datetime.now())
  root.update() # these 2 have the same function as mainloop but can be added to.
  root.update_idletasks()