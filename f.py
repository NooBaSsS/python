import os
import random
playerhp = 100
enemyhp = 100

while playerhp > 0 and enemyhp > 0:
    os.system("cls")
    if playerhp > 0:
        playerd = random.randint(10, 30)
        enemyhp -= playerd
        print(f"{name} нанес {playerd} урона")
        print(f"у противника осталось {enemyhp} жизней")
        input("для продолжения нажмите ENTER")
    if enemyhp > 0:
        enemyd = random.randint(10, 30)
        playerhp -= enemyd
        print(f"{name} получил {enemyd} урона")
        print(f"у {name} осталось {playerhp} жизней")
        input("для продолжения нажмите ENTER")
if playerhp > enemyhp:
    print(f"{name} победил")
    way_1 = False
    key = ""
elif enemyhp > playerhp:
    print(f"{name} проиграл")
    game = False