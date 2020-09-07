import abc
from Flower import Flower


class FlowerBuilder:

    def __init__(self):
        self.flower = Flower()

    @abc.abstractmethod
    def set_color(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_petal_amount(self):
        raise NotImplementedError
