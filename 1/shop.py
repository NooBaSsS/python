
import os
def shop(player):
    while True:
        os.system("cls")
        print(f"{player[0]} приехал в магазин с {player[1]} в кармане. У него {player[3]} зелий.")
        print("зелье лечения - 200")
        print("1. купить")
        print("2. уехать")
        while True:
            choice = input("что делать? ")
            if choice == "1" or choice == "2":
                break
        if choice == "1":
            if player[1] >= 20:
                player[1] -= 200
                player[3] += 1
                print(f"теперь у {player[0]} {player[3]} зелий")
                input("для продолжения нажмите ENTER")
            else:
                print("у вас нет столько денег")
        if choice == "2":
            return player