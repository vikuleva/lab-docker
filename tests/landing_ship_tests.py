from nose.tools import *
from moonlanding.landing_ship import LandingShip, GRAVITY


def test_ship():
    ship = LandingShip(0, 0, 0)
    assert_equal(ship.fuel_tank.percents_left, 100)
    assert_equal(ship.speed, 0)


def test_fuel():
    ship = LandingShip(0, 0, 0)
    assert_equal(ship.fuel_tank.percents_left, 100)
    ship.run_engine(20)
    assert_equal(ship.fuel_tank.percents_left, 80)
    ship.run_engine(80)
    assert_equal(ship.fuel_tank.percents_left, 0)
    ship.run_engine(20)
    assert_equal(ship.fuel_tank.percents_left, 0)
    try:
       ship.run_engine(-20)
    except ValueError as e:
        if str(e) != "Fuel can't be negative!":
            raise e


def test_falling():
    start_height, weight = 20, 3
    ship = LandingShip(weight, 0, start_height)
    assert_equal(ship.height, start_height)
    ship.move()
    assert_equal(ship.height, start_height - weight * GRAVITY)
    assert_equal(ship.speed, -weight * GRAVITY)
    ship.move()
    assert_equal(round(ship.height, 3), round(start_height - (weight * GRAVITY) * 3, 3))


def test_engine():
    start_height, weight, engine = 20, 3, 2
    ship = LandingShip(weight, engine, start_height)
    ship.run_engine(3)
    assert_equal(ship.speed, engine * 3)
    ship.move()
    assert_equal(ship.height, start_height - (weight * GRAVITY - engine * 3))
    assert_equal(ship.speed, engine * 3 - weight * GRAVITY)
