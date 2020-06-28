import json
numbers = [2, 3, 5, 6, 11, 16, 32]

slovar = {"name": "Ivan", "surname": "Ivanov"}

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

filename = 'data.json'
with open(filename, 'w') as f:
    json.dump(slovar, f)