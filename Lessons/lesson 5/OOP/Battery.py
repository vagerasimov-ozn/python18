import time
class Battery():
    """Простой класс аккуммулятора, который может обслуживать наш автомобиль"""
    def __init__(self,battery_size, weight):
        self.battery_size = battery_size
        self.weight = weight

    def discharge_status(self, kilometri):
        self.battery_size -=kilometri
        return "В аккумуляторе автомобиля осталось только " + str(self.battery_size)
    def charge(self, time_charge):
        for i in range(time_charge):
            if self.battery_size>150:
                print("Все заряжено")
                break
            else:
                self.battery_size +=10
                time.sleep(1)
                print(self.battery_size)