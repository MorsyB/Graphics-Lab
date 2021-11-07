from djitellopy import Tello
import time
import keyboard
import tkinter as tk
import tkinter.font as tkFont
import threading

import cv2


class App:
    drone = Tello()

    def __init__(self, root):
        # setting title        StreamTest.start()
        root.title("undefined")
        # setting window size
        width = 423
        height = 256
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_412 = tk.Button(root)
        GButton_412["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_412["font"] = ft
        GButton_412["fg"] = "#000000"
        GButton_412["justify"] = "center"
        GButton_412["text"] = "Up"
        GButton_412.place(x=70, y=40, width=70, height=25)
        GButton_412["command"] = self.GButton_412_command

        GButton_132 = tk.Button(root)
        GButton_132["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_132["font"] = ft
        GButton_132["fg"] = "#000000"
        GButton_132["justify"] = "center"
        GButton_132["text"] = "Down"
        GButton_132.place(x=70, y=100, width=70, height=25)
        GButton_132["command"] = self.GButton_132_command

        GButton_889 = tk.Button(root)
        GButton_889["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_889["font"] = ft
        GButton_889["fg"] = "#000000"
        GButton_889["justify"] = "center"
        GButton_889["text"] = "Right"
        GButton_889.place(x=140, y=70, width=70, height=25)
        GButton_889["command"] = self.GButton_889_command

        GButton_387 = tk.Button(root)
        GButton_387["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_387["font"] = ft
        GButton_387["fg"] = "#000000"
        GButton_387["justify"] = "center"
        GButton_387["text"] = "Left"
        GButton_387.place(x=0, y=70, width=70, height=25)
        GButton_387["command"] = self.GButton_387_command

        GButton_473 = tk.Button(root)
        GButton_473["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_473["font"] = ft
        GButton_473["fg"] = "#000000"
        GButton_473["justify"] = "center"
        GButton_473["text"] = "Forward"
        GButton_473.place(x=350, y=40, width=70, height=25)
        GButton_473["command"] = self.GButton_473_command

        GButton_437 = tk.Button(root)
        GButton_437["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_437["font"] = ft
        GButton_437["fg"] = "#000000"
        GButton_437["justify"] = "center"
        GButton_437["text"] = "Backward"
        GButton_437.place(x=350, y=100, width=70, height=25)
        GButton_437["command"] = self.GButton_437_command

        GButton_356 = tk.Button(root)
        GButton_356["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_356["font"] = ft
        GButton_356["fg"] = "#000000"
        GButton_356["justify"] = "center"
        GButton_356["text"] = "L"
        GButton_356.place(x=170, y=140, width=70, height=25)
        GButton_356["command"] = self.GButton_356_command

        GButton_404 = tk.Button(root)
        GButton_404["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_404["font"] = ft
        GButton_404["fg"] = "#000000"
        GButton_404["justify"] = "center"
        GButton_404["text"] = "R"
        GButton_404.place(x=260, y=140, width=70, height=25)
        GButton_404["command"] = self.GButton_404_command

        GMessage_349 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_349["font"] = ft
        GMessage_349["fg"] = "#333333"
        GMessage_349["justify"] = "center"
        GMessage_349["text"] = "Tello :)"
        GMessage_349.place(x=200, y=20, width=80, height=25)

        GButton_320 = tk.Button(root)
        GButton_320["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_320["font"] = ft
        GButton_320["fg"] = "#000000"
        GButton_320["justify"] = "center"
        GButton_320["text"] = "Connect"
        GButton_320.place(x=0, y=190, width=70, height=25)
        GButton_320["command"] = self.GButton_320_command

        GButton_760 = tk.Button(root)
        GButton_760["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_760["font"] = ft
        GButton_760["fg"] = "#000000"
        GButton_760["justify"] = "center"
        GButton_760["text"] = "Disconnect"
        GButton_760.place(x=0, y=220, width=70, height=25)
        GButton_760["command"] = self.GButton_760_command

        GButton_472 = tk.Button(root)
        GButton_472["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_472["font"] = ft
        GButton_472["fg"] = "#000000"
        GButton_472["justify"] = "center"
        GButton_472["text"] = "Takeoff"
        GButton_472.place(x=350, y=190, width=70, height=25)
        GButton_472["command"] = self.GButton_472_command

        GButton_769 = tk.Button(root)
        GButton_769["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_769["font"] = ft
        GButton_769["fg"] = "#000000"
        GButton_769["justify"] = "center"
        GButton_769["text"] = "Land"
        GButton_769.place(x=350, y=220, width=70, height=25)
        GButton_769["command"] = self.GButton_769_command

    def GButton_412_command(self):
        self.drone.move_up(40)

    def GButton_132_command(self):
        self.drone.move_down(40)

    def GButton_889_command(self):
        self.drone.move_right(40)

    def GButton_387_command(self):
        self.drone.move_left(40)

    def GButton_473_command(self):
        self.drone.move_forward(40)

    def GButton_437_command(self):
        self.drone.move_back(40)

    def GButton_356_command(self):
        self.drone.rotate_clockwise(30)

    def GButton_404_command(self):
        self.drone.rotate_counter_clockwise(30)

    def showStream(self):
        self.drone.streamon()
        while True:
            img = self.drone.get_frame_read().frame
            cv2.imshow("image", img)
            cv2.waitKey(1)

    def GButton_320_command(self):
        self.drone.connect()
        streamTest = threading.Thread(target=self.showStream)
        streamTest.start()
        print(self.drone.get_battery())

    def GButton_760_command(self):
        self.drone.end()


    def GButton_472_command(self):
        self.drone.takeoff()

    def GButton_769_command(self):
        self.drone.land()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    print("Running")
