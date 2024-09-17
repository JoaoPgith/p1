from sensor import Sensor

#O objeto "atuador" é criado apenas quando os sensores temperatura e pressao sao criados
class Atuador(Sensor):
    def __init__(self, id, num_serie, point_temp,point_press):
        super().__init__(id, num_serie)
        self.point_temp = point_temp
        self.point_press = point_press
        self.ar_condicionado    

    
