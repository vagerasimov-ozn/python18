def cikl(n):
    if n == 0 or n == 1:
        return 1
    else:
        prod = 1
        for i in range(1, n+1):
            prod *= i
        return prod