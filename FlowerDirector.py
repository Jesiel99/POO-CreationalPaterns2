from Flower import Flower
from FlowerBuilder import FlowerBuilder


class FlowerDirector:

    def __new__(cls, flower: FlowerBuilder):
        cls.flower_builder = flower
        obj = super().__new__(cls)
        obj.__build()
        return obj.flower_builder.flower

    def __build(self):
        self.flower_builder.set_color()
        self.flower_builder.set_petal_amount()