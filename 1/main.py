import fight, dice, shop
p_name = "1"
p_hp = 100
p_money = 500
p_potions = 1
def game(p_name, p_hp, p_money, p_potions):
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
        shop.shop(p_name, p_hp, p_money, p_potions)
game(p_name, p_hp, p_money, p_potions)