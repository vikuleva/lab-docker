from moonlanding.game import Game


def main():
    game = Game(ship_engine_power=3, ship_weight=5, height=5)
    game.play()

if __name__ == "__main__":
    main()
