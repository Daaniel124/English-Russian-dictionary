from random import *
from gtts import gTTS
import os
import pyttsx3
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

def correction(lang1: list, lang2: list, choice: int):
    """
    Ищем слово в файле и исправляем его

    :param list lang1: Список первого языка
    :param list lang2: Список второго языка
    :param int choice: Выбор языка
    """
    print("Введите слово, перевод которого хотите исправить".center(70, ))
    if choice == 1:
        wordup = input('На русском: ')
        word = wordup.lower()
        check = wordSearch(word, lang1)
    else:
        wordup = input('На английском: ')
        word = wordup.lower()
        check = wordSearch(word, lang1)

    if check == False:
        print('Такого слова нет в словаре.')
    else:
        wordindex = lang1.index(word)
        transword = lang2[wordindex]
        print(f'Изначальный перевод - {transword}')
        print('Введите заменяемое слово'.center(50, ))
        if choice == 1:
            replaceup = input('На английском: ')
            replace = replaceup.lower()
            with open ('eng.txt', 'r') as f:
                old_data = f.read()
            new_data = old_data.replace(transword, replace)
            with open ('eng.txt', 'w') as f:
                f.write(new_data)
        else:
            replaceup = input('На русском: ')
            replace = replaceup.lower()
            with open ('rus.txt', 'r') as f:
                old_data = f.read()
            new_data = old_data.replace(transword, replace)
            with open ('rus.txt', 'w') as f:
                f.write(new_data)

def chekup(lang1: list, lang2: list):
    """
    Проверяет правильность перевода слов у пользователя

    :param list lang1: Список первого языка
    :param list lang2: Список второго языка
    """
    r = 0
    i = 0
    print('Вам будет даваться по пять слов один раз. Дается слово и рядом нужно написать его перевод\nПосле написания слова будет показано, верен ли перевод. В конце вы узнаете результат знания этих слов')
    while True:
        for i in range(5):
            word = choice(lang1)
            index = lang1.index(word)
            transword = lang2[index]
            chek = input(f'{i+1}. {word} - ')
            if chek == transword:
                i += 1
                r += 1
                print('Перевод верный')
            else:
                i += 1
                print('Перевод не верный')
        result = r/i * 100
        print(f'Ваш результат: {r} правильных ответов, {result}%')
        ans = input('Желаете закончить? y/n ')
        if ans == 'y':
            break

def ttsG():
    '''
    Синтез речи от Google
    '''
    #from playsound import playsound #pip install
    print('Синтез речи'.center(24, ))
    lang = int(input('На каком языке хотите воспроизводить речь? рус/англ - 1/2: '))
    blabla = input('Введите слово: ')
    if lang == 1:
        tts = gTTS(text=blabla, lang='ru')
        #tts.save("C:\\Users\\opilane\\Desktop\\test.mp3")
        tts.save('test.mp3')
    else:
        tts = gTTS(text=blabla, lang='en')
        #tts.save("C:\\Users\\opilane\\Desktop\\test.mp3")
        tts.save('test.mp3')
    #playsound()
    #os.system('C:\\Users\\opilane\\Desktop\\test.mp3')
    os.system('test.mp3')

def ttsP():
    #https://ichi.pro/ru/vvedenie-v-pyttsx3-preobrazovatel-teksta-v-rec-dla-python-81905511310787
    engine = pyttsx3.init()
    engine.say("Hello this is me talking")
    engine.setProperty('rate',120)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()

def ttsAuto(text: str, lang: str):
    '''
    Синтез речи всех слов в списке
    '''
    #language = 'en', 'fi', 'ru'
    obj = gTTS(text=text, lang=lang).save('test.mp3')
    os.system('test.mp3')