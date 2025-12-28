from __future__ import annotations

from typing import Self


class FuelOverflowError(Exception):
    MESSAGE = "Вы пытаетесь залить слишком много бензина!"

    def __init__(self: Self) -> None:
        super().__init__(self.MESSAGE)


class InsufficientFuelError(Exception):
    MESSAGE = "Не доедем жеж..."

    def __init__(self: Self) -> None:
        super().__init__(self.MESSAGE)


class Car:
    def __init__(self: Self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity = float(fuel_capacity)
        self._fuel_in_tank = 0.0

    def get_current_fuel_level(self: Self) -> float:
        return self._fuel_in_tank

    def refuel_car(self: Self, fuel_quantity: float) -> None:
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise FuelOverflowError from None
        self._fuel_in_tank += fuel_quantity

    def drive(self: Self, distance_km: float) -> float:
        fuel_burned: float = 8.0 * (distance_km / 100.0)

        if self._fuel_in_tank < fuel_burned:
            raise InsufficientFuelError from None

        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
