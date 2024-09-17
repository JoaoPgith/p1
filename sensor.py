from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, id, num_serie):
        self.id = id
        self.num_serie = num_serie

