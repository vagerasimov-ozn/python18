year = 2020
data = int(input("Сколько вам лет? "))
year_future = int(input("В какои году хотите узнать свой возраст? "))
diff = year_future - year
future_age = data + diff
print("B " + str(year_future) + " вам будет " + str(future_age))
