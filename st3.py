import os
name = input("введите имя: ")
if not name: name = "Илья"
way_1 = True
way_2 = True
way_3 = True
game = True
key = ""
while game:
    if (way_1 or way_2 or way_3) and key == "":
        key = ""
        os.system("cls")
        print(f"Подъезжает {name} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть». Призадумался {name}:")
        if way_1:
            print("1. Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
        if way_2:
            print("2. Ну, поеду где женатому быть!")
        if way_3:
            print("3. Ну, поеду в дорожку, где богатому быть.")
        choice = input("куда пойти? ")
        if choice == "1" and way_1:
            key += choice
        if choice == "2" and way_2:
            key += choice
        if choice == "3" and way_3:
            key += choice

    if key == "1" and way_1:
        os.system("cls")
        print(f"Только {name} отъехал три версты, напали на него сорок разбойников. Хотят его с коня стащить, хотят его ограбить, до смерти убить.")
        print("1. За один взмах десять разбойников лежат, за второй - и двадцати на свете нет!")
        print("2. вариант")
        choice = input("куда пойти ")
        if choice == "1" or choice == "2":
            key += choice

    if way_1 and key == "11":
        os.system("cls")
        print("хорошая концовка")
        way_1 = False
        key = ""
        input("для продолжения нажмите ENTER")

    if way_1 and key == "12":
        os.system("cls")
        print("плохая концовка")
        game = False
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

    if way_1 == way_2 == way_3 == False:
        os.system("cls")
        print("пройдeно все")
        game = False
        input("для продолжения нажмите ENTER")

print("конец")