"""
Задание №1 Создайте класс Моя Строка, где: будут доступны все возможности str
 дополнительно хранятся имя автора строки и время создания
(time.time)
"""

import time
from datetime import datetime


class MyStr(str):
    """
    MyStr - class, наследует все возможности класса str
    также имеет дополнительные атрибуты
    """

    def __new__(cls, value, author_name):
        """
        Создает экземпляр класса с дополнительными атрибутами
        value: Переданная строка
        author_name: имя автора-создателя
        creation_time = datetime.datetime.now() - время создания
        """
        my_srt = super().__new__(cls, value)
        my_srt.author_name = author_name
        # my_srt.creation_time = time.time()
        my_srt.creation_time = datetime.now()
        return my_srt


if __name__ == '__main__':
    s = MyStr('Новая Строка Теста', 'Sergey')
    print(f'{s}\nавтор: {s.author_name}, время создания: {s.creation_time}')
    print(s.lower())
    # print(help(MyStr))