import os
import random
dice = True
attemps = 3
win = False
number = random.randint(1, 10)
while dice:
    print(number)
    p_number = int(input("Какое число от 1 до 10? "))
    if number == p_number:
        print("молодец, ты угадал")
        win = True
        dice = False
    elif number != p_number:
        attemps -= 1
        print(f"это не то число, которое я загадал. Попробуй еще раз, ты можешь попробовать еще {attemps} раз.")
    if not attemps:
        dice = False
if win:
    print("Ты выиграл")
else:
    print("К сожалению у тебя не получилось угадать")
