import glob, pathlib, hashlib, os, re

'''
#1
Напишите скрипт, который читает текстовый файл и выводит символы 
в порядке убывания частоты встречаемости в тексте. Регистр символа 
не имеет значения. Программа должна учитывать только буквенные 
символы (символы пунктуации, цифры и служебные символы слудет 
игнорировать). Проверьте работу скрипта на нескольких файлах с 
текстом на английском и русском языках, сравните результаты с 
таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.
'''
def task_1():
    lc = {}
    s = ""
    with open("1.txt", "r") as file1:
        
        for line in file1:
            line = line.lower()
            for letter in line:
                if letter.capitalize() != letter:
                    if not(letter in lc.values()):
                        lc.update({line.count(letter):letter})

    a = list(lc.keys())
    a.sort()
    a.reverse()
    for i in a:
        s += lc[i] + ' '
    print(s)


'''
#2
Напишите скрипт, позволяющий искать в заданной директории и в ее 
подпапках файлы-дубликаты на основе сравнения контрольных сумм 
(MD5). Файлы могут иметь одинаковое содержимое, но отличаться 
именами. Скрипт должен вывести группы имен обнаруженных файлов-дубликатов.

                        
'''

def task_2():
    # директория
    path = pathlib.Path.cwd() / 'task2'
    #path = "A:\Prog_Labs\4_sem python\python_lab2\task2"
    x_str = ""
    d = {}
    b = []
    files_paths = glob.glob(str(path)+"/*.*")
    for p in files_paths:
        with open(p, "r") as file1:
            x_str = file1.read()
            file1 = str(file1)
            d.update({str(file1)[file1.rindex('\\')+1:file1.rindex("mode")-2]: x_str})
            x_str = ""
    for roots, dirs, files in os.walk(path):
        for dir in dirs:
            for roots, dirs, files in os.walk(path / dir):
                for file in files:
                    with open(str(path)+"\\" + dir + "\\"+ file, "r") as file1:
                        x_str = file1.read()
                        d.update({str(file): x_str})
                        x_str = ""
    for key1 in d:
        for key2 in d:
            if hashlib.md5(d[key1].encode('utf-8')).hexdigest() == hashlib.md5(d[key2].encode('utf-8')).hexdigest() and key1 != key2 and not key1 in b and not key2 in b:
                print("Duplicates: " + key1 + " & " + key2)
                b.append(key1)
                b.append(key2)

'''
#3
Задан путь к директории с музыкальными файлами (в названии 
которых нет номеров, а только названия песен) и текстовый файл, 
хранящий полный список песен с номерами и названиями в виде строк 
формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
имена файлов в директории на основе текста списка песен
'''


def task_3():
    mp3_files = []
    path = pathlib.Path.cwd() / 'task3'
    pattern = r" .*\s\["
    txt_path = pathlib.Path.cwd() / 'task3' / 'text' / 'text.txt'
    for roots, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.mp3'):
                    with open(txt_path, 'r') as text_file:
                        for line in text_file:
                            match = re.findall(r" .*\s\[", line)
                            match[0] = match[0].replace('[', '').replace(' ', '')
                            if match[0] == file.replace('.mp3', '').replace(' ', ''):
                                file_oldname = os.path.join(path / file)
                                file_newname = os.path.join(path / (line.replace('\n', '').replace(':', '.')+ '.mp3'))
                                #newFileName=shutil.move(file_oldname, file_newname)

                                os.replace(file_oldname, file_newname)

'''
def replace_name_track():
    path = pathlib.Path.cwd() / 'task3'
    txt_file = path.joinpath('text.txt')
    with open(txt_file) as f:
        for file in os.listdir(path):
            if file.endswith('.mp3'):
                os.replace(str(path) + '/' + file, str(path) + '/' + f.readline().rstrip() + '.mp3')
'''
#'A:\\Prog_Labs\\4_sem python\\python_lab2\\task3\\10,000 Days (Wings Pt 2).mp3'
#'A:\\Prog_Labs\\4_sem python\\python_lab2\\task3\\04 10,000 Days (Wings Pt 2) [11:13].mp3'

'''
#4
Напишите скрипт, который позволяет ввести с клавиатуры имя 
текстового файла, найти в нем с помощью регулярных выражений все 
подстроки определенного вида, в соответствии с вариантом. Например, 
для варианта № 1 скрипт должен вывести на экран следующее:
Вариант 5: найдите все номера телефонов – подстроки вида 
«(000)1112233» или «(000)111-22-33»
'''

def task_4():
    path = pathlib.Path.cwd() / 'task4' / 'text.txt'
    pattern = r'\(\d{3}\)\d{3,}|-\d{2}-\d{2}'
    res = []
    with open(path, 'r') as text_file:
       numbers: list = text_file.readlines()
    numbers = [x.rstrip() for x in numbers]
    for number in numbers:
        if re.match(pattern, number):
            res.append(number)
    for i in res:
        print(i)

'''
#5
Введите с клавиатуры текст. Программно найдите в нем и выведите
отдельно все слова, которые начинаются с большого латинского 
символа (от A до Z) и заканчиваются 2 или 4 цифрами, например 
«Petr93», «Johnny70», «Service2002». Используйте регулярные 
выражения.
'''
def task_5():
    text = 'Lorem12 ipsum Service2002 dolor sit amet, consectetur312123 adipiscing543345 Petr93 elit, sed354435 do5445 eiusmod tempor incididunt Johnny70 ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    pattern = r'[A-Z]\w*\d{2}|[A-Z]\w*\d{4}'
    a = re.findall(pattern, text)
    print(a)

def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()

if __name__ == "__main__":
    main()

