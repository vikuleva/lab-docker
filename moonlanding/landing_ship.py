from textwrap import dedent

GRAVITY = 1.68


class LandingShip(object):
    """Ship which lands on Moon"""

    def __init__(self, weight, engine_power, start_height):
        self.weight = weight
        self.engine_power = engine_power
        self.height = start_height
        self.fuel_tank = FuelTank()
        self.speed = 0

    def get_status(self):
        return dedent(f"""\
        Высота: {round(self.height, 2)}
        Вертикальная скорость: {round(self.speed, 2)} м/с
        Осталось {round(self.fuel_tank.percents_left, 2)}% топлива""")

    def move(self):
        self.speed -= GRAVITY * self.weight
        self.height += self.speed

    def run_engine(self, fuel):
        if fuel < 0:
            raise ValueError("Fuel can't be negative!")
        self.speed += self.engine_power * self.fuel_tank.use_fuel(fuel)


class FuelTank:

    def __init__(self):
        self.percents_left = 100
    
    def use_fuel(self, percents):
        can_use = min(percents, self.percents_left)
        self.percents_left -= can_use
        return can_use
