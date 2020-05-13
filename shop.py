info_shop = "сковородки сковородка история книга памперсы чайники"
new_spi=[]
arr_info = info_shop.split()

for word in arr_info:
    if word.startswith("сковород"):
        new_spi.append(word)
    else:
        print("не сковородка")
print(new_spi)
print(arr_info)