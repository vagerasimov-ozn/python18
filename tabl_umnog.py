# Таблица умножения
arr1 = (1,2,3,4,5,6,7,8,9)
arr2 = (1,2,3,4,5,6,7,8,9)
i=0
while (i <=8):
    j=0
    while (j <=8):
        print(str(arr1[i]) + ' * ' + str(arr2[j]) + ' = ' + str(arr1[i]*arr2[j]))
        j +=1
    i += 1
    print('\n')