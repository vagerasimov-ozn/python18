name = "Matt"
first = name
age = 1000
print(id(age))
print(name, age)
age = age + 1
print(id(age))
print(name, age)
names = []
print(id(names))
names.append("Fred")
print(id(names))
i=0
while i < len(names):
    print(names[i], age)
    i +=1
