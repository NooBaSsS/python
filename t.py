import random
user = 0
cas = 0
user_money = 100
cas_money = 100
tr = 0
while user_money and cas_money:
    user = random.randint(1, 6)
    cas = random.randint(1, 6)
    if user > cas:
        print("вы выиграли")
        print("вы выбросили ", user)
        print("противник выбросил ", cas)
        user_money += 10
        cas_money -= 10
        print("у вас ", user_money)
        print("у противника ", cas_money)
        input("для продолжения нажмите ENTER")
        tr += 1
        print()
    elif cas > user:
        print("вы проиграли")
        print("вы выбросили ", user)
        print("противник выбросил ", cas)
        user_money -= 10
        cas_money += 10
        print("у вас ", user_money)
        print("у противника ", cas_money)
        input("для продолжения нажмите ENTER")
        tr += 1
        print()
    elif user == cas:
        print("ничья")
        print("у вас ", user_money)
        print("у противника ", cas_money)
        input("для продолжения нажмите ENTER")
        tr += 1
        print()
if cas_money == 0:
    print("вы выиграли за", tr, "попыток")
elif user_money == 0:
    print("противник выиграл за", tr, "попыток")