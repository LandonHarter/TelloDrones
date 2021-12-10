from djitellopy import Tello

tello = Tello()
tello.connect(wait_for_state=False)

tello.takeoff()

tello.flip_forward()
tello.flip_back()
tello.flip_left()
tello.flip_right()

tello.land()
