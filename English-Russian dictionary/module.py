def readFile(file: str)->list:
    """
    Читаем строки из файла и добавляем их в список

    :param str f: Название файла
    """
    file = open(file, 'r', encoding = "utf-8-sig")
    mas = []
    for line in file:
        mas.append(line.strip())
    file.close()
    return mas

def newWord(file: str, x: str)->list:
    """
    Добавляем новое слово в файл и список

    :param str f: Название файла
    :param str x: Добавляемое слово
    """
    mas = [] 
    with open(file, "a", encoding = "utf-8-sig") as f:
        f.write(x+"\n")
    mas = readFile(file)
    return mas

def wordSearch(n: str, l: list):
    """
    Ищем слово в списке

    Возвращает True или False
    :param str n: ищет логин
    :rtype: bool
    """
    if n in l:
        t = True
    else:
        t = False
    return t
    

def translate(lang1: list, lang2: list):
    """
    Ищем индекс слова в списке и выводим его перевод

    Возвращает False, если такого слова нет в списке
    :param list lang1: Список первого языка
    :param list lang2: Список второго языка
    """
    word = input('Введите слово: ')
    t = wordSearch(word, lang1)
    if t == True:
        index1 = lang1.index(word)
        transword = lang2[index1]
        print(f'Перевод: {transword}')
    else:
        print('Такого слова нет в словаре')
        return False
