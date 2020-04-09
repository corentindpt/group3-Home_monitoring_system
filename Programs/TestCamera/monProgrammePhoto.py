from time import sleep
from picamera import PiCamera

camera=PiCamera()
camera.resolution=(1024,768)
camera.rotation=180
camera.start_preview()
sleep(2)
camera.capture('testPhoto.jpg')
camera.stop_preview()
