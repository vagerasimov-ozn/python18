from car import *

bmw = Car("bmw", 90, condey = True)
jigul = Car('vaz 2110', 110)

bmw.update_odometr(200)
bmw.increment_odometr(200)
print(bmw.odometr)


print(bmw.speed)
print(bmw.marka)
print(bmw.cooling())
print(jigul.cooling())
print(bmw.car_rid())
print(dir(jigul))
