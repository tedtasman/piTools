from picamera import PiCamera

class Camera:

    def __init__(self, directory, name):
        self.index = -1
        self.path = directory + name + "_"
        self.camera = PiCamera
        print(f"Camera initialized. Saving photos to {self.path}<index>")
    
    def capture(self):
        self.index += 1
        self.camera.capture(f'{self.path}{self.index}')
        return f'{self.path}{self.index}'