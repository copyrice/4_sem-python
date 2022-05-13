import datetime
import functools
import itertools
from random import shuffle, randrange, random
import math


def convert_to_decimal_1():
    num = float(input())
    if num < 0:
        print("Error. Negative number")
    else:
        p = math.floor(num)
        d = (num - p) % 1
        print(p, "руб.", int(round(d, 2)*100), "коп.")


def ascending_list_2(a):
    if a == sorted(a):
        return True
    else:
        return False


def card_number_3():
    s = input()
    # s = '1234567890123456'
    a = s[4:len(s)-4]
    s = s.replace(a, "*" * len(a))
    print(s)


def splitter_4():
    # s = input()
    s = "lorem ipsum dolor sit amet consectetuer adipiscing elit"
    a = s.split()
    result = ""
    b = list(filter(lambda x: len(x) > 7, a))
    for word in b:
        result += word + ' '

    b = list(filter(lambda x: 7 >= len(x) >= 4, a))
    for word in b:
        result += word + ' '

    b = list(filter(lambda x: len(x) < 4, a))
    for word in b:
        result += word + ' '

    print(result)


def uppercase_5():
    """
    s = input()
    b = ""
    s = "city Donetsk, river Kalmius"
    a = re.split(" |,", s)
    a = list(map(lambda x: x.upper() if x.istitle() else x, a))
    a = filter(None, a)
    print(' '.join(a))
    """
    s = "city Donetsk, river Kalmius".split()
    print(" ".join(i.upper() if i[0].isupper() else i for i in s))


def symbols_6():
    # s = input()
    s = "1lorem ipsum dolor sit amet 3consectetuer adipiscing elitz"
    result = ""
    for letter in s:
        if s.count(letter) <= 1:
            result += letter + " "
    print(result)


def www_com_7():
    s = ["www.instagram.com", "vk.com", "www.youtube.com", "www.kinopoisk.ru"]
    a = ["http://"+i for i in s if i.startswith("www")]
    a = [i if i.endswith(".com") else i.replace(i[i.rindex('.'):len(i)], ".com") for i in a]
    # a = list(filter(lambda x: x if x.startswith("www") else None, s))
    # a = list(map(lambda x: "http://" + x, a))
    print(a)


def create_mas_8():
    n = randrange(1, 10)
    a = [randrange(1, 10) for i in range(0, n)]
    print(n)
    for i in range(0, 10):
        if 2**i > n:
            for j in range(n, 2**i):
                a.insert(j, 0)
            n = 2**i
            print(n)
            break
    print(a)


def bankomat_9():
    balance = 100000
    result = ""
    # x = int(input())
    x = 5170
    notes = [5000, 2000, 1000, 500, 200, 100, 50, 10]
    print(balance)
    if x > balance:
        print("Error")
    else:
        balance -= x
        for note in notes:
            print(f'{x//note} x {note}')
            x %= note
    print(balance)


def password_10():
    password = "qwQrty12122112"
    if len(password) > 9 and not password.isdigit() and password.upper():
        print("The password is secure")
    else:
        print("The password is not secure")


def frange_11(start, stop, step):
    i = start
    while i < stop:
        yield round(i, 2)
        i += step


def get_frames_12(signal, size, overlap):
    step = int(size * overlap)
    stop = len(signal) - 1
    for start in range(0, stop, step):
        yield [i for i in signal[start: start + size]]


def extra_enumerate_13(x):
    cum = 0
    frac = 0
    sum = 0
    for i in x:
        sum += i
    for i in x:
        cum += i
        frac = cum/sum
        yield i, cum, round(frac, 2)


def non_empty_14(func):
    def inner(*args, **kwargs):
        result = func()
        for i in range(0, result.count('')):
            result.remove('')
        return result
    return inner


@non_empty_14
def get_pages_14():
    return ['chapter1', '', 'contents', '', 'line1']

# s[i] = s[i]–a∙s[i–1]


def pre_process(a_):
    def decorator(func):
        def inner(s):
            return func(list(filter(lambda x: x == x-a_*s[s.index(x)-1], s)))
        return inner
    return decorator
# [round(s[i]-a_*s[i-1], 2) for i in range(len(s))]


@pre_process(0.93)
def plot_signal_15(s):
    print(s)


def football_manager_16(teams):
    shuffle(teams)
    dates = datetime.datetime(2022, 9, 14, 12, 55)
    groups = [teams[i * 4:i * 4 + 4] for i in range(4)]
    print("Matсhes: ")
    for group in groups:
        for i in range(len(group)//2):
            print(group[i], "-", group[i+1], "|", dates.strftime("%d/%m/%Y %H:%M"))
            dates += datetime.timedelta(days=14, hours=randrange(0, 4))
            i += 2


def main():
    print("Task 1: ")
    convert_to_decimal_1()

    a = [-1, 3, 8, 10]
    print("\nTask 2: ")
    print(ascending_list_2(a))

    print("\nTask 3: ")
    card_number_3()

    print("\nTask 4: ")
    splitter_4()

    print("\nTask 5: ")
    uppercase_5()

    print("\nTask 6: ")
    symbols_6()

    print("\nTask 7: ")
    www_com_7()

    print("\nTask 8: ")
    create_mas_8()

    print("\nTask 9: ")
    bankomat_9()

    print("\nTask 10: ")
    password_10()

    print("\nTask 11: ")
    for x in frange_11(1, 5, 0.1):
        print(x)

    print("\nTask 12: ")
    [print(frame) for frame in get_frames_12(range(10), 2, 0.5)]

    print("\nTask 13: ")
    x = list(range(1, 6))
    print(list(extra_enumerate_13(x)))

    print("\nTask 14: ")
    print(get_pages_14())

    print("\nTask 15: ")
    sp = [0, 0.93,]
    print(plot_signal_15())

    print("\nTask 16: ")
    teams = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens',
             'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals',
             'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions',
             'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts',
             'Jacksonville Jaguars', 'Kansas City Chiefs']
    print(football_manager_16(teams))


if __name__ == '__main__':
    main()