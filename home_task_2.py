# Задача из сериализации данных:
# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестирования
# возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца из
# переданного файла.

import pickle
import csv


class CSVConverter:

    def __init__(self, data):
        self.data = data

    def pickle_to_csv(self):
        with open(self.data, 'rb') as pickle_file:
            pickle_data = pickle.load(pickle_file)

        fields = ['i', 'a', 'c']

        with open('csv_file.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fields)
            writer.writeheader()
            writer.writerows(pickle_data)


if __name__ == '__main__':
    pickle_class = CSVConverter("user.pickle")
    pickle_class.pickle_to_csv()
