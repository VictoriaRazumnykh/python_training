from model.group import Group
import random
import string
import os.path
# import json
import jsonpickle
# чтение опций командной строки
import getopt
# получить доступ к этим опциям
import sys

try:
    # n - кол-во генерируемых данных, f - файл, в который это должно помещаться
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# дефолтные значения
n = 5
f = "data/groups.json"

# переменная opts, прочитанная парсером getopt
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# генерируем случайные тестовые данные
def random_string(prefix, maxlen):
    # символы из случайно сгенерированной строки (*10 - частота встречающихся пробелов)
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    # гененируем случайную строку
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(n)
]
# testdata = [Group(name=name, header=header, footer=footer)
#        for name in ["", random_string("name", 10)]
#        for header in ["", random_string("header", 10)]
#        for footer in ["", random_string("footer", 10)]
#        ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
