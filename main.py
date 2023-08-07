import csv
import json
from random import randint


def coef(func):
    def wrapper():
        with open('coef.csv', 'r', encoding='utf-8') as f:
            filereader = csv.reader(f)
            for line in filereader:
                res = func(line)
        return res

    return wrapper


def json_writer(func):
    res = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        dic = {f'{[x for y in args for x in map(int, y)]}': result}
        # dict = {f'{args}': result}
        res.append(dic)
        with open(f'{func.__name__}_result.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)
        return result

    return wrapper


@coef
@json_writer
def qeq(string):
    res = None
    if string:
        a, b, c = map(int, string)
        d = b * b - 4 * a * c
        if a == 0:
            if b != 0:
                res = -c / b
        elif d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            res = x1, x2
        elif d == 0:
            res = -b / (2 * a)
    return res


def gen_coef(min_, max_):
    with open('coef.csv', 'w', encoding='utf-8', newline='') as f:
        count = randint(100, 1000)
        c = 0
        csv_write = csv.writer(f)
        while c < count:
            csv_write.writerow([str(randint(min_, max_)) for x in range(3)])
            c += 1


gen_coef(-100, 100)
qeq()
