import os
import random
name = input("введите имя: ")
if not name: name = "Илья"
way_1 = True
way_2 = True
way_3 = True
way_4 = True
game = True
playerhp = 100
enemyhp = 100
dice = True
attemps = 3
win = False
key = ""
while game:
    if (way_1 or way_2 or way_3 or way_4) and key == "":
        os.system("cls")
        print(f"Подъезжает {name} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть». Призадумался {name}:")
        if way_1:
            print("1. Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
        if way_2:
            print("2. Ну, поеду где женатому быть!")
        if way_3:
            print("3. Ну, поеду в дорожку, где богатому быть.")
        if way_4:
            print("4. ")
        choice = input("куда пойти? ")
        if choice == "1" and way_1:
            key += choice
        if choice == "2" and way_2:
            key += choice
        if choice == "3" and way_3:
            key += choice
        if choice == "4" and way_4:
            key += choice

    if key == "1" and way_1:
        os.system("cls")
        print(f"Только {name} отъехал три версты, напали на него сорок разбойников. Хотят его с коня стащить, хотят его ограбить, до смерти убить.")
        print("1. Сражаться")
        print("2. Вернуться назад")
        choice = input("куда пойти ")
        if choice == "1" or choice == "2":
            key += choice

    if way_1 and key == "11":
        os.system("cls")
        while playerhp > 0 and enemyhp > 0:
            os.system("cls")
            if playerhp > 0:
                playerd = random.randint(5, 15)
                enemyhp -= playerd
                print(f"{name} нанес {playerd} урона, у противника осталось {enemyhp} жизней")
            if enemyhp > 0:
                enemyd = random.randint(5, 15)
                playerhp -= enemyd
                print(f"{name} получил {enemyd} урона, у {name} осталось {playerhp} жизней")
                input("для продолжения нажмите ENTER")
        if playerhp > enemyhp:
            print(f"{name} победил")
            way_1 = False
            key = ""
        elif enemyhp > playerhp:
            print(f"{name} проиграл")
            game = False
        input("для продолжения нажмите ENTER")

    if way_1 and key == "12":
        os.system("cls")
        key = ""
        input("для продолжения нажмите ENTER")

    if key == "2" and way_2:
        os.system("cls")
        print(f"Как проехал {name} три версты, выехал на лесную поляну. Там стоят терема златоверхие, широко раскрыты ворота серебряные, на воротах петухи поют. Въехал {name} на широкий двор, выбежали к нему на встречу двенадцать девушек, среди них королевна-красавица.")
        print("1. Неспроста она со мной ласкова: что королевич - не простой казак, старый дедушка. Видно, что-то у нее задумано.")
        print("2. вариант")
        choice = input("куда пойти ")
        if choice == "1" or choice == "2":
            key += choice

    if way_2 and key == "21":
        os.system("cls")
        print("хорошая концовка")
        way_2 = False
        key = ""
        input("для продолжения нажмите ENTER")

    if way_2 and key == "22":
        os.system("cls")
        print("плохая концовка")
        game = False
        input("для продолжения нажмите ENTER")

    if key == "3" and way_3:
        os.system("cls")
        print(f"Только отъехал {name} три версты, увидал большой камень в триста пудов. А на том камне написано: «Кому камень под силу свернуть, тому богатому быть».")
        print(f"1. Принатужился {name}, уперся ногами, по колена в землю ушел, поддал могучим плечом - свернул с места камень. Открылся под камнем глубокий погреб - богатства несметные: и серебро, и золото, и крупный жемчуг, и яхонты!")
        print("2. вариант")
        choice = input("куда пойти ")
        if choice == "1" or choice == "2":
            key += choice

    if way_3 and key == "31":
        os.system("cls")
        print("хорошая концовка")
        way_3 = False
        key = ""
        input("для продолжения нажмите ENTER")

    if way_3 and key == "32":
        os.system("cls")
        print("плохая концовка")
        game = False
        input("для продолжения нажмите ENTER")

    if key == "4" and way_4:
        os.system("cls")
        number = random.randint(1, 10)
        print("Я загадал случайное число от 1 до 10, сможешь угадать его?")
        while dice:
            p_number = int(input("Какое число от 1 до 10? "))
            os.system("cls")
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
            way_4 = False
            key = ""
            input("для продолжения нажмите ENTER")
        else:
            print("К сожалению у тебя не получилось угадать")
            way_4 = False
            key = ""
            input("для продолжения нажмите ENTER")
    if way_1 == way_2 == way_3 == way_4 == False and win:
        os.system("cls")
        print("пройдeно все + 4 дорога")
        game = False
        input("для продолжения нажмите ENTER")
    if way_1 == way_2 == way_3 == way_4 == False and not win:
        os.system("cls")
        print("пройдeно все кроме 4 дороги")
        game = False
        input("для продолжения нажмите ENTER")
print("конец")