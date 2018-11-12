import tkinter as tk 
t = tk.Tk()


def pow():
    print('co słychać')

pole = tk.Canvas(t, width=600, height=600)
pole.create_line(200, 0, 200, 600)
pole.create_line(400, 0, 400, 600)
pole.create_line(0, 200, 600, 200)
pole.create_line(0, 400, 600, 400)
pole.pack()
prz = tk.Button(t, text="kliknij mnie", command=pow)
prz.pack()