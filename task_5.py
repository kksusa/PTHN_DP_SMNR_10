class Animals:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def name_animal(self):
        return self.name


class Fish(Animals):
    def __init__(self, fresh_water, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fresh_water = fresh_water
        self.deep = deep

    def specific(self):
        if self.fresh_water:
            return True
        return False

    def check_deep(self):
        if self.deep <= 3:
            return f"Мелководное до {self.deep} метров"
        elif 3 < self.deep < 20:
            return f"Среднеглубинное до {self.deep} метров"
        return f"Глубоководное глубже {self.deep} метров"


class Birds(Animals):

    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_length = self.wingspan * 0.45
        return wing_length


class Mammals(Animals):

    def __init__(self, hibernate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hibernate = hibernate

    def specific(self):
        if self.hibernate:
            return True
        return False


if __name__ == 'main':
    dog = Mammals(False, 'Собака', True)
    print(f"Название: {dog.name}, Хвост: {dog.tail}, Спячка: {dog.hibernate}")
