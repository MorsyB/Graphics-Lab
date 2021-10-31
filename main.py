from djitellopy import Tello
import time

drone = Tello()
drone.connect()
drone.takeoff()
print("Im taking off guys")
time.sleep(5)
print("im about to end")
drone.end()
