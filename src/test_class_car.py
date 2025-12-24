import pytest

from car import Car  


@pytest.fixture()
def car():
    return Car(model="BMW X5", fuel_capacity=80)


def test_refuel_ok(car):
    car.refuel_car(20)
    assert car.get_current_fuel_level() == 20


def test_refuel_overflow(car):
    with pytest.raises(Exception, match=r"слишком много бензина"):
        car.refuel_car(1000)


def test_drive_ok(car):
    car.refuel_car(20)
    remaining = car.drive(20)
    assert remaining < 20


def test_drive_not_enough_fuel(car):
    with pytest.raises(Exception, match=r"Не доедем жеж..."):
        car.drive(100)
