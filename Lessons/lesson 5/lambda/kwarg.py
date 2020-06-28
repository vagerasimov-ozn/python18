# def adder(*nums):
#     sum = 0
#     for n in nums:
#         sum+=n
#     return sum
# print(adder(2,3))
# print(adder(4,5,6,7,44,3))
# print(adder(2, 3,))


def intro(**data):
    print("\n Data type of argument", type(data))

    for key, value in data.items():
        print('{} is {}'.format(key,value))

intro(firstname = 'Petr', lastname = 'Ivanov')
intro(firstname = 'Ivan', lastname = 'Ivanov')

slovar = {'name':'Pavel','lasname':'Ivanov'}
intro(**slovar)