import main
import os
def shop(p_name, p_hp, p_money, p_potions):
    while True:
        os.system("cls")
        print(f"{p_name} приехал в магазин с {p_money} в кармане. У него {p_potions} зелий.")
        print("зелье лечения - 200")
        print("1. купить")
        print("2. уехать")
        while True:
            choice = input("что делать? ")
            if choice == "1" or choice == "2":
                break
        if choice == "1":
            if p_money >= 200:
                p_money -= 200
                p_potions += 1
                print(f"теперь у {p_name} {p_potions} зелий")
                input("для продолжения нажмите ENTER")
            else:
                print("у вас нет столько денег")
        if choice == "2":
            main.game(p_name, p_hp, p_money, p_potions)