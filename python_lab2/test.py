from pydub import AudioSegment
import argparse, os, datetime, time, glob, shutil
import subprocess
from sys import argv
from pathlib import Path
'''
Написать скрипт trackmix.py, который формирует обзорный трек-микс 
альбома (попурри из коротких фрагментов mp3-файлов в 
пользовательской директории). Для манипуляций со звуковыми 
файлами можно использовать сторонние утилиты, например, FFmpeg.
Пример вызова и работы скрипта:
 trackmix --source "C:\\Muz\\Album" --count 5 --frame 15 -l -e
--- processing file 1: 01 - Intro.mp3
--- processing file 2: 02 - Outro.mp3
--- done!
13
Параметры скрипта:
--source (-s) – имя рабочей директории с треками, обязателен;
--destination (-d) – имя выходного файла, необязателен (если не указан, 
то имя выходного файла – mix.mp3 в директории source);
--count (-c) – количество файлов в "нарезке", необязателен (если он не 
указан, то перебираются все mp3-файлы в директории source);
--frame (-f) – количество секунд на каждый файл, необязателен (если не 
указан, скрипт вырезает по 10 секунд из произвольного участка каждого 
файла);
--log (-l) – необязательный ключ (если этот ключ указывается, то скрипт 
должен выводить на консоль лог процесса обработки файлов, как в 
примере);
--extended (-e) – необязательный ключ (если этот ключ указывается, то 
каждый фрагмент попурри начинается и завершается небольшим 
fade in/fade out).

A:\\Prog_Labs\\4_sem python\\python_lab2\\music

'''



#files: list = glob.glob(f'{source}\\*.*')


def main():
    source = Path.cwd() / 'music'
    destination = 'mix.mp3'
    count = 2
    frame = 10
    log = True
    extended = True
    mp3_files: list = glob.glob(f'{source}/*.mp3')

    for i in range(count):
        subprocess.call(
            f'ffmpeg -i "{mp3_files[i]}" -t {frame} \
            "{Path.cwd() / "music" / f"tmp_{i}.mp3"}" -y -loglevel quiet'
            )
        if log:
            print('file {0} is completed'.format(mp3_files[i][mp3_files[i].rfind("\\")+1:]))


    tmps: list = glob.glob(f"{Path.cwd() / 'music' / 'tmp*.mp3'}")

    if extended:
        for i, tmp in enumerate(tmps):
            subprocess.call(
                f'ffmpeg -i "{tmp}" \
                -af "afade=t=in:ss=0:d=3,afade=t=out:st={frame-3}:d=3" \
                "{Path.cwd() / "music" / f"tmp_new{i}.mp3"}" -y -loglevel quiet'
                )
            os.remove(tmp)
        tmps: list = glob.glob(f"{Path.cwd() / 'music' / 'tmp_new*.mp3'}")

    with open(f'{Path.cwd() / "music" / "files.txt"}', 'w') as f:
        f.writelines(f"file '{tmp}'\n" for tmp in tmps)

    subprocess.call(
        f'ffmpeg -f concat -safe 0 -i \
        "{Path.cwd() / "music" / "files.txt"}" -c copy \
        "{Path.cwd() / "music" / f"{destination}"}" -y -loglevel quiet'
        )

    if log and os.path.exists(Path.cwd() / "music" / f"{destination}"):
        print(f'file {destination} was created')


    os.remove(Path.cwd() / "music" / "files.txt")
    for tmp in tmps:
        os.remove(tmp)

if __name__ == '__main__':
    main()