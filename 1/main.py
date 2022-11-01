import fight, dice, shop

player = ("1", 100, 50, 0)
def game(player):
    print("1. битва")
    print("2. кости")
    print("3. лавка")
    while True:
        choice = input("куда? ")
        if choice == "1" or choice == "2" or choice == "3":
            break
    if choice == "1":
        fight.fight(p_name, p_hp, p_money, p_potions)
    if choice == "2":
        dice.dice(p_name, p_hp, p_money, p_potions)
    if choice == "3":
        shop.shop(player)
game(player)