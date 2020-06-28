def square(x):
    return x**2

def show_result(num):
    print(f'А вот это у нас число {num}')

show_result(square(3))

sh = show_result

square_2 = square(2)
sh(square_2)