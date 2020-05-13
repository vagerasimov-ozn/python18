amount = int(input("Введите количество людей: "))

people_salary = []
for i in range(amount):
    people_salary.append(int(input("Введите доход " + str(i+1) + " человека: ")))

sum = 0
for salary in people_salary:
    sum += salary

average = sum / len(people_salary)
print("Каждый может тратить: " + str(average))