age = int(input("insert your age: "))
if age > 18 and age <80:
    print("welcome")
elif age >80:
    print("temporarily blocke site")
else:
    print("no access")


job = input("what are yuo? ")
if job == "admin" or job == "superadmin":
    print("full access granted")
else:
    print("standart access")