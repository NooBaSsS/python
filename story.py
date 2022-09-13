print("1. убит")
print("2. женат")
print("3. богат")
choise = int(input("выберите путь: "))
if choise == 1:
    print("вас отправили на казнь")
    print("1. сопротивляться")
    print("2. сдаться и принять смерть")
    choise = int(input("что делать? "))
    if choise == 1:
        print("вы чудом вырвались")
    elif choise == 2:
        print("вы умерли")
elif choise == 2:
    print("вы женились")
elif choise == 3:
    print("вы стали богат")
else:
    print("введен некорректный ответ")
