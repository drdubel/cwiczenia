import tkinter as tk
import random
t = tk.Tk()
a = ['blue', 'green', 'red', 'pink', 'yellow', 'violet', 'purple', 'gray', 'brown']

płótno = tk.Canvas(t, bg = random.choice(a), width=800, height=800)
płótno.pack()



tk.mainloop()
