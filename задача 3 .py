a = ("procent")
b = ("procenta")
c = ("procentov")
numbs = {1, 12, 13, 14}
for i in range(0, 100):
    i = i + 1
    if i in numbs:
        print(i, "procent")
    elif i % 10 == 1:
        print(i, "procentov")
    elif i % 10 >= 1 and i % 10 <5:
        print(i, "procenta")
    else:
        print(i, "procentov")