from picamera2 import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
i = 0
try:
    while True:
        sleep(5)
        camera.capture(f'/home/pi/test_images/image_{i}.jpg')
        print(f'Image {i} captured')
        i += 1
except KeyboardInterrupt:
    print("Exiting...")
finally:
    camera.stop_preview()