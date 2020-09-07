from abc import ABCMeta
from Flower import Flower
from FlowerBuilder import FlowerBuilder


class Rose(FlowerBuilder):

    def __init__(self):
        super().__init__()

    def set_color(self):
        self.flower.color = 'red'

    def set_petal_amount(self):
        self.flower.petal_amount = 12

