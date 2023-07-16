# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. Внутри класса
# создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from task_5 import Birds, Fish, Mammals


class ClassCreator:

    def create_class(self, animal_class, *args, **kwargs):
        new_class = self.get_class(animal_class)
        return new_class(*args, **kwargs)

    def get_class(self, animal_class):
        if animal_class.lower() == 'fish':
            return Fish
        elif animal_class.lower() == 'birds':
            return Birds
        elif animal_class.lower() == 'mammals':
            return Mammals
        else:
            raise ValueError(animal_class)


if __name__ == '__main__':
    dog = ClassCreator().create_class('Mammals', False, 'Собака', True)
    print(f"Название: {dog.name}, Хвост: {dog.tail}, Спячка: {dog.hibernate}")
