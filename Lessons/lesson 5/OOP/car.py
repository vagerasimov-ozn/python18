class Car:
    """Базовый класс автомобиля"""
    def __init__(self, marka, speed, condey = None):
        """Инициализирует атрибуты марки и скорости автомобиля"""
        self.marka = marka
        self.speed = speed
        self.condey = condey
        self.odometr = 0
    def car_rid(self):
        return "машина" + self.marka + "Едет со скоростью" + str(self.speed)
    def cooling(self):
        if self.condey:
            print('В машине становится прохладнее')
        else:
            print('купите себе usb - вентилятор')
    # def update_odometr(self, kilometri):
    #     self.odometr += kilometri
    #  def incremen_odometr(self,speed,hours):

# bmw = Car("bmw", 90, condey = True)
# jigul = Car('vaz 2110', 110)
# print(bmw.speed)
# print(bmw.marka)
# print(bmw.cooling())
# print(jigul.cooling())
# print(bmw.car_rid())
# print(dir(jigul))
#
# for item in bmw.__dict__:
#     print(item,bmw.__dict__[item])