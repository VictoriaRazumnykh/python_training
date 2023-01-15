class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

# определяем как будет выглядеть объект при выводе на консоль (какое его строковое представление)
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

# тк питон считает объекты разными из-за физического расположения, определяем ф-цию, которая реализует логическое сравнение
#чтобы сравнение выполнялось по смыслу
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
