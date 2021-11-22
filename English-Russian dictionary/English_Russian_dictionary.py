from module import *
rus_list = readFile("rus.txt")
eng_list = readFile("eng.txt")
print(rus_list)
print(eng_list)

while True:
    menu = input("Перевод - T\nНовое слово - U\nОшибка - V\nПроверка - K\nВыход - L\nПросмотр листов - P\n")
    if menu.upper() == "T":
        v = int(input('С рус. на англ. или с англ. на рус. (1/2): '))
        if v == 1:
            basic = rus_list
            secondary = eng_list
            t = translate(basic, secondary)
        elif v == 2:
            basic = eng_list
            secondary = rus_list
            t = translate(basic, secondary)

        if t == False:
            ans = input('Хотите добавить слово в словарь? y/n: ')
            if ans == 'y':
                rus_list = newWord("rus.txt", input("Новое слово (на русском): "))
                eng_list = newWord("eng.txt", input("New word (in english): "))
            else:
                pass
    elif menu.upper() == "U":
        rus_list = newWord("rus.txt", input("Новое слово (на русском): "))
        eng_list = newWord("eng.txt", input("New word (in english): "))
        pass
    elif menu.upper() == "V":
        pass
    elif menu.upper() == "K":
        pass
    elif menu.upper() == 'P':
        print(rus_list)
        print(eng_list)
    else:
        print('Выход..')
        break
