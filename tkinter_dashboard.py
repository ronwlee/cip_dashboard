""" 
Dashboard prototye
Ron Lee
13 June

"""

import tkinter as tk
import tkinter.ttk as ttk

# create a window
dashboard = tk.Tk()

time = ttk.Label(text="12:00",
         font=("Arial", 64, "bold")
        )

date = ttk.Label(text="Jun 13", font=("Arial", 64, "italic"))

year = ttk.Label(text="2024", font=("Arial", 64, "italic"))

# display dashboard
time.pack()
date.pack()
year.pack()

dashboard.mainloop()