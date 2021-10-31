from djitellopy import Tello
import time

drone = Tello()
drone.connect()
print(drone.get_battery())
print("Im taking off guys")
drone.takeoff()
time.sleep(5)
print("moving up")
drone.move_up(50)
time.sleep(3)
print(" look at me im about to FLIP!!!!!!")
drone.flip_forward()
drone.flip_forward()
print(drone.get_battery())
print("im about to end")
drone.end()
