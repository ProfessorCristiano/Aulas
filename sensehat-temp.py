# sensehat-temp.py
# Na aplicação use sense_hat no emulador use sense_emu https://sense-emu.readthedocs.io/en/v1.0/install.html
# from sense_hat import SenseHat
from sense_emu import SenseHat
sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp=sense.temp
    pixels = [red if i < temp else blue for i in range (64)]
    sense.set_pixels(pixels)
