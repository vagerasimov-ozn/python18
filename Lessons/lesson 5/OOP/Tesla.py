from car import Car
from Battery import Battery

class Tesla(Car):
    """Представляет из себя класс автомобиля с электродвигателем"""
    def __init__(self,speed,marka='Tesla',condey = True):
        super().__init__(marka,speed,condey)
        # С помощью супер мы получаем доступ к атрибутам класса родителя
        self.battery = Battery(120, 10)
    @staticmethod
    def get_promo():
        return "самые классные машины это Тесла"

print(Tesla.get_promo())
print(dir(Tesla))

myTesla = Tesla(200);
print(myTesla.car_rid())
myTesla.cooling()
print(myTesla.battery.battery_size)
print(myTesla.battery.discharge_status(100))

myTesla.battery.charge(15)