#Randomizer ok
import random

spi = ['volvo','suzuki','bmv','nissan']

print(random.random())
print(random.randint(1,10))
#random.shuffle(spi)
car_random = random.choice(spi)
print(spi)
print(car_random)