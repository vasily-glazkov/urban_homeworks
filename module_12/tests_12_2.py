import unittest

from module_12.module_12_2 import Runner, Tournament

"""
Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. 
Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. 
Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. 
У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. 
В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) 
и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. 
В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.

Пример результата выполнения тестов:
Вывод на консоль:
{1: Усэйн, 2: Ник}
{1: Андрей, 2: Ник}
{1: Андрей, 2: Усэйн, 3: Ник}

Ran 3 tests in 0.001s
OK
"""


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def setUp(self):
        self.usein = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def test_tournament_usein_nick(self):
        t = Tournament(90, self.usein, self.nick)
        results = t.start()
        index = len(self.__class__.all_results) + 1
        self.__class__.all_results[index] = {key: value.name for key, value in
                                             results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_andrei_nick(self):
        t = Tournament(90, self.andrei, self.nick)
        results = t.start()
        index = len(self.__class__.all_results) + 1
        self.__class__.all_results[index] = {key: value.name for key, value in
                                             results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_andrei_usein_nick(self):
        t = Tournament(90, self.andrei, self.usein, self.nick)
        results = t.start()
        index = len(self.__class__.all_results) + 1
        self.__class__.all_results[index] = {key: value.name for key, value in
                                             results.items()}
        self.assertEqual(results[1].name, 'Усэйн')  # Усэйн должен быть первым
        self.assertEqual(results[2].name, 'Андрей')  # Андрей должен быть вторым
        self.assertEqual(results[3].name, 'Ник')  # Ник должен быть последним


if __name__ == "__main__":
    unittest.main()
