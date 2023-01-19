from sys import maxsize
class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

# определяем как будет выглядеть объект при выводе на консоль (какое его строковое представление)
    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

# тк питон считает объекты разными из-за физического расположения, определяем ф-цию, которая реализует логическое сравнение
#чтобы сравнение выполнялось по смыслу
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

#функция для вычисления ключа, по которому сравнивается группа
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
