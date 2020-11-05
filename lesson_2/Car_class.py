# 1) Создать класс автомобиля. Создать классы легкового автомобиля
# и грузового. Описать в основном классе базовые атрибуты и методы
# для автомобилей. Будет плюсом если в классах наследниках
# переопределите методы базового класса.


class Car:

    num_of_wheels = 4

    def __init__(self,name,weight,max_speed):
        self.name = name
        self.weight = weight
        self.max_speed = max_speed

    def reachkm(self):
        print(f'Машина {self.name} проедет 100 км за {100/self.max_speed} час. ')

    def chek_weight(self):
        print(f'Масса машины {self.name} - {self.weight}')

class Passenger_Car(Car):
    """Class Passenger Car"""
    def reachkm(self):
        print(f'Машина {self.name} проедет 300 км за {300/self.max_speed} час. ')

class Truck_Car(Car):
    """Class Truck"""
    def reachkm(self):
        print(f'Машина {self.name} проедет 300 км за {300/self.max_speed} час. ')

car = Passenger_Car('Volvo',90,100)
car.reachkm()
car.chek_weight()
