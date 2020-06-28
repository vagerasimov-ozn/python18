"""Числа от 1 до 10 считаем
в императивной парадигме мы могли бы решить это с помощью циклов"""

def print_num(n):
    if n > 20:
        return
    print(n)
    n += 1
    print_num(n)

print_num(3)