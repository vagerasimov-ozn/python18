from simple_benchmark import benchmark
from factorial import fact_rec
from cikl import cikl
import matplotlib.pyplot as plt

func = [fact_rec, cikl] # список с нашими функциями
arguments = {} #у нас аргументы передаются в словаре
for i in range(2,30):
    arguments[str(i)] = i
print(arguments)

arguments_name = 'натуральные числа'

aliases = {fact_rec:'простая рекурсия', cikl:'использование цикла'}
b = benchmark(func, arguments, arguments_name, aliases)
b.plot()

plt.show(b)