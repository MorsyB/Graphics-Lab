import time
from Controller import PS4Controller
from GUI import App
import tkinter as tk
from djitellopy import Tello

if __name__ == '__main__':
    # ps4 = PS4Controller()
    # ps4.init()
    # ps4.listen()
    # root = tk.Tk()
    # app = App(root)
    # root.mainloop()
    # print("Running")

    drone = Tello(host='192.168.1.115')
    #drone = Tello()
    drone.connect()
    print(drone.get_battery())
    # drone.set_wifi_credentials('waseemJR', 'mode0874')
    # drone.takeoff()
    # drone.land()

