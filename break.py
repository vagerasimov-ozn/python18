alive = True
while alive:
    status = input("Введите ваш статус по здоровью: ")
    if status == "bad":
        print("Оставвайтесь дома и пейте чай")
        break
    else:
        print(" Приступайте работе")