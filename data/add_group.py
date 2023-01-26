from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# генерируем случайные тестовые данные
def random_string(prefix, maxlen):
    # символы из случайно сгенерированной строки (*10 - частота встречающихся пробелов)
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # гененируем случайную строку
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
        Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
        for i in range(5)
]
#testdata = [Group(name=name, header=header, footer=footer)
#        for name in ["", random_string("name", 10)]
#        for header in ["", random_string("header", 10)]
#        for footer in ["", random_string("footer", 10)]
#        ]
