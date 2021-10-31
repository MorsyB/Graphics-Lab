from djitellopy import Tello
import time
import keyboard


def running():
    return True


if __name__ == '__main__':
    drone = Tello()
    drone.connect()
    print(drone.get_battery())
    print("Im taking off guys")
    drone.takeoff()
    print("Running")
    while running():
        while keyboard.is_pressed("w"):
            drone.move_forward(40)
        while keyboard.is_pressed("a"):
            drone.move_left(40)
        while keyboard.is_pressed("s"):
            drone.move_back(40)
        while keyboard.is_pressed("d"):
            drone.move_right(40)
        while keyboard.is_pressed("q"):
            drone.move_up(40)
        while keyboard.is_pressed("e"):
            drone.move_down(40)
        if keyboard.is_pressed("f"):
            print("im about to end")
            break
    print(drone.get_battery())
    drone.end()