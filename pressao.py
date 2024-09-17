from sensor import Sensor

class Pressao(Sensor):
    def __init__(self, id, num_serie, sensor_press):
        super().__init__(id, num_serie)
        self.sensor_press = sensor_press

    
    @property
    def sensor_press(self):
        return self.sensor_press
    
    @sensor_press.setter
    def sensor_press(self, sensor_press):
        self.sensor_press = sensor_press
