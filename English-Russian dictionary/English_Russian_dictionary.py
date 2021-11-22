from module import *
rus_list = readFile("rus.txt")
eng_list = readFile("eng.txt")
print(rus_list)
print(eng_list)

while True:
    menu = input("Перевод - T\nНовое слово - U\nИсправить ошибку - V\nСамопроверка - K\nВыход - L\nПросмотр листов - P\n")
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
                rus = input("Новое слово (на русском): ")
                eng = input("New word (in english): ")
                rus_list = newWord("rus.txt", rus.lower())
                eng_list = newWord("eng.txt", eng.lower())
            else:
                pass
    elif menu.upper() == "U":
        rus = input("Новое слово (на русском): ")
        eng = input("New word (in english): ")
        rus_list = newWord("rus.txt", rus.lower())
        eng_list = newWord("eng.txt", eng.lower())
        pass
    elif menu.upper() == "V":
        choice = int(input('Перевод слова на каком языке хотите исправить? англ. или рус. - 1/2: '))
        if choice == 1:
            lang1 = rus_list
            lang2 = eng_list
            correction(lang1, lang2, choice)
            eng_list = readFile('eng.txt')
            print('Перевод исправлен'.center(45, ))
        else:
            lang1 = eng_list
            lang2 = rus_list
            correction(lang1, lang2, choice)
            rus_list = readFile("rus.txt")
            print('Перевод исправлен'.center(45, ))
        pass
    elif menu.upper() == "K":
        print('Проверка перевода слов'.center(35, ))
        choice = int(input('С какого на какой язык переводить слова?\nС англ. на рус. или с рус. на англ. - 1/2: '))
        if choice == 1:
            lang1 = eng_list
            lang2 = rus_list
            chekup(lang1, lang2)
        else:
            lang1 = rus_list
            lang2 = eng_list
            chekup(lang1, lang2)
        pass
    elif menu.upper() == 'P':
        print(rus_list)
        print(eng_list)
    else:
        print('Выход..')
        break
