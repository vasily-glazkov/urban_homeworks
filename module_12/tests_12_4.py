import unittest
from module_12_4 import Runner
import logging

"""
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и 
если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением 
"Неверная скорость для Runner".

test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением 
"Неверный тип данных для объекта Runner"."""

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
    encoding="utf-8",
    format="%(asctime)s || %(levelname)s || %(message)s"
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        Tests the walk method of the Runner class.
        Creates a Runner instance and calls walk 10 times.
        Verifies if the distance covered is 50 units.
        """
        try:
            runner = Runner('Bolt', -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner. {e}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Tests the run method of the Runner class.
        Creates a Runner instance and calls run 10 times.
        Verifies if the distance covered is 100 units.
        """
        try:
            runner = Runner(True)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner. {e}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
       Tests the combined use of walk and run methods on two Runner instances.
       Creates two Runner instances, calling walk on one and run on the other 10 times each.
       Verifies that the distances covered by each instance are different.
       """
        runner1 = Runner('Bolt')
        runner2 = Runner('Turtle')

        for _ in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
