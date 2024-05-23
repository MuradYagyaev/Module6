# Модуль №6. Наследование классов. Домашнее задание.

class Car:
    price = 1000000

    def horse_powers(self):
        self.power = 100
        return '{}: мощность - {} л.с.'.format(self.__class__.__name__, self.power)

class Nissan(Car):
    price = 3000000

    def horse_powers(self):
        self.power = 140
        return '{}: мощность - {} л.с.'.format(self.__class__.__name__, self.power)

class Kia(Car):
    price = 2000000

    def horse_powers(self):
        self.power = 110
        return '{}: мощность - {} л.с.'.format(self.__class__.__name__, self.power)


my_car = Nissan()
my_second_car = Kia()
print(my_car.horse_powers())
print(f'Цена: {my_car.price} рублей')
print(my_second_car.horse_powers())
print(f'Цена: {my_second_car.price} рублей')
