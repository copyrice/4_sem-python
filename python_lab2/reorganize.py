import argparse, pathlib, os, datetime, time, glob, shutil
from datetime import date, datetime as d


'''
Напишите скрипт reorganize.py, который в директории --source создает 
две директории: Archive и Small. В первую директорию помещаются 
файлы с датой изменения, отличающейся от текущей даты на 
количество дней более параметра --days (т.е. относительно старые 
файлы). Во вторую – все файлы размером меньше параметра --size байт. 
Каждая директория должна создаваться только в случае, если найден 
хотя бы один файл, который должен быть в нее помещен. Пример
вызова:
source = 'A:\\Prog_Labs\\4_sem python\python_lab2\\task6'
reorganize --source "C:\TestDir" --days 2 --size 4096

'''
p = argparse.ArgumentParser()
p.add_argument('--source', type=str, default=pathlib.Path.cwd() / 'task6')
p.add_argument('--days', type=int, default=0)
p.add_argument('--size', type=int, default=0)
args = p.parse_args()

def create_dir(source, name):
    try:
        os.mkdir(source / name)
    except OSError:
        pass


def archive(days, source):
    flag = 0
    delta = datetime.timedelta(days=days)
    cur_time = d.now()
    files: list = glob.glob(f'{source}\\*.*')
    for file in files:
        convert_time = time.localtime(os.path.getmtime(file))
        format_time = time.strftime('%d%m%Y %H:%M:%S', convert_time)
        datetime_object = datetime.datetime.strptime(format_time, '%d%m%Y %H:%M:%S')
        if cur_time - delta > datetime_object:
            if flag == 0:
                create_dir(source, 'Archive')
                flag = 1
            shutil.move(file, source / 'Archive')



def small(size, source):
    flag = 0
    files: list = glob.glob(f'{source}\\*.*')
    for file in files:
        if os.path.getsize(file) < size:
            if flag == 0:
                create_dir(source, 'Small')
                flag = 1
            shutil.move(file, source / 'Small')

def main(source, days, size):
    archive(days, source)
    small(size, source)


if __name__ == '__main__':
    main(args.source, args.days, args.size)