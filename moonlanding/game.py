from moonlanding.landing_ship import LandingShip


class Game:

    SAFE_SPEED = 5

    def __init__(self, ship_engine_power, ship_weight, height):
        self.start_height = height
        self.ship = LandingShip(ship_weight, ship_engine_power, self.start_height)

    def ask_fuel(self):
        while True:
            try:
                request = float(input("Сколько процентов топлива вы хотите использовать?\n> "))
            except ValueError:
                print("Вы ввели некорректное значение, попробуйте ещё раз")
                continue
            if request >= self.ship.fuel_tank.percents_left:
                print("Невозможно! В баках осталось только {round(self.ship.fuel, 2)}% топлива")
                continue
            if request < 0:
                print("Невозможно! Двигатели работают только на торможение")
                continue
            return request

    def play(self):
        print("Посадка начинается!")
        while self.ship.height > 0:
            print(self.ship.get_status())
            self.ship.run_engine(self.ask_fuel())
            self.ship.move()
        print(f"Корабль приземлился на скорости {round(self.ship.speed, 2)}")
        if abs(self.ship.speed) > Game.SAFE_SPEED:
            print("Корабль разбился")
        else:
            print("Корабль совершил мягкую посадку")
