# Давайте напишем программу русской рулетки

import random

amount_of_bullets = int(input("Сколько патронов? "))

baraban = [0,0,0,0,0,0]
# 0 - пустое гнездо
# 1 - гнездо с патроном

for i in range(amount_of_bullets):
    baraban[i] = 1

print("Посмотрите на барабан", baraban)

how_much = int(input("сколько раз вы собираетесь нажать на курок? "))
for i in range(how_much):
    random.shuffle(baraban)
    if baraban[0] == 1:
        print("бабах")
    else:
        print("щелк")