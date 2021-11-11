import time
from Controller import PS4Controller
from GUI import App
import tkinter as tk

if __name__ == '__main__':
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    print("Running")
