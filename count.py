min = int(input("min"))
max = int(input("max"))
counter = 0
while min != max + 1:
    if min % 2 == 0:
        print(min)
    min += 1
    if counter > 999:
        break