# Модуль №6. Наследование классов. Множественное наследование

class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        self.power = 100
        return '{}: мощность - {} л.с.'.format(self.__class__.__name__, self.power)


class Nissan(Car, Vehicle):
    price = 3000000
    vehicle_type = "Car"

    def horse_powers(self):
        self.power = 140
        return '{}: мощность - {} л.с.'.format(self.__class__.__name__, self.power)


my_car = Nissan()
print(my_car.horse_powers())
print(f'Цена: {my_car.price} рублей')
print(f'Тип транспортного средства: {my_car.vehicle_type}')
