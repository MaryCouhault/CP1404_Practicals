from Pract_08.taxi import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_num = random.randint(0, 100)
        if random_num < self.reliability:
            distance = super().drive(distance)

        else:
            distance = 0
        return distance