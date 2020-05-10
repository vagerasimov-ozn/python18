import random

guess_number = input("Введите любое число: ")
limit = int(input("Введите предел рандома: "))

random_number = random.randint(0,limit)
if rundom_number == int(guess.number):
    print("Вы победили!")
else:
    print("А правильное число было", random_number)