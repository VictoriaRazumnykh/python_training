import calendar
import locale
import pymorphy2
import random


def random_month():
    morph = pymorphy2.MorphAnalyzer()
    locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
    symbols = []
    for name in calendar.month_name:
        symbols.append(morph.parse(name)[0].normal_form.capitalize())
    return random.choice(symbols)


print(random_month())
