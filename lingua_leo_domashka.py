import random

amount_of_words = input("Как много слов вы хотите занести в словарь: ")
aow = int(amount_of_words)
slovar = {}

for i in range(aow):
    key = input("Введите слово на английском: \n ")
    value = input("Введите слово на русском: \n ")
    slovar[key] = value

for i in range(aow):
    random.shuffle(slovar[key])
    ts=random.choice(slovar[key])
print(ts)

    # for key in slovar.keys():
    #     print("Переведи слово ", key, ": ")
    #     answer = input("Ваш вариант перевода: \n ")
    #     if slovar[key] == answer:
    #         print("Все верно! Лев сыт!")
    #     else:
    #         print("А правильный ответ был", slovar[key])

