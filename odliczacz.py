import tkinter as tk


class Licznik(tk.Label):
    
    def __init__(self, master, czas_s):
        super().__init__(master)
        self._timer = None
        self.czas_s = czas_s
        self.odliczanie()

        
    def odliczanie(self):
        if self.czas_s > 0:
            self['text'] = f'zostało {self.czas_s}s'
            self.czas_s -= 1
            self._timer = self.after(10000, self.odliczanie)
        else:
            self['text'] = 'Czas minął!'

root = tk.Tk()
l = Licznik(root, 1)
l.pack()
root.mainloop()