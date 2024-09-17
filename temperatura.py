from sensor import Sensor

class Temperatura(Sensor):
    def __init__(self, id, num_serie, sensor_temp):
        super().__init__(id, num_serie)
        self.sensor_temp = sensor_temp

    @property
    def sensor_temp(self):
        return self.sensor_temp
    
    @sensor_temp.setter
    def sensor_temp(self, sensor_temp):
        self.sensor_tem = sensor_temp

    
