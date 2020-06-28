def fibonacci(n,i=1,z=1):
    # if z > n:
    #     return
    if i > n:
        return
    print(i)
    z = i
    i = z + i
    fibonacci(n,i,z)

fibonacci(10)