from _typeshed import Self
import math, time

SOS = 343 # Speed of sound m/s
AREA = 3 * math.pi # Are of sensor sense
LENGTH = 3 # m

class sensor:
    def __init__(self, sensor, x, y):
        self.sensor = sensor
        self.x = x
        self.y = y
    
    def send_signal():
        pass

    def listen():
        pass

    def calculate_distance():
        pass