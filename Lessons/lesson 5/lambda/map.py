import random

spi = ['Хороший','Очень хороший']

main_data = ["Маша", "Паша", "Ян"]

def pohvala(name):
    return name +' '+ random.choice(spi)

names_with_characters = map(pohvala, main_data)

print(names_with_characters)
print(main_data)