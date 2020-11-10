from time import sleep
from PIL import ImageGrab
import allure



class CaptureScreen:

    def capture_screen(self, pic_name):
        im = ImageGrab.grab(bbox=(645, 316, 1918, 1072))
        im.save(pic_name+".png", "jpeg")

    def attach_pic(self, pic_name, description):
        with open(pic_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, description, allure.attachment_type.PNG)

if __name__ == '__main__':
    sleep(3)
    capture_app = CaptureScreen()
    capture_app.capture_screen("test")
