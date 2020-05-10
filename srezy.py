numbers = list(range(0,14,2))
print(numbers)

massiv = ["volvo","bmv","suzuki"]

# massiv2 = massiv
massiv2 = massiv[:] #клон, чтобы разделить в памяти, иначе оба списка будут идентичны
massiv2.append("jigul")
massiv.append("kopeika")
massiv.insert(0,"ford") #Расходный по памяти
print(massiv)
print(massiv2)
