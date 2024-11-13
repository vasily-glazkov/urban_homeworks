import unittest

from module_12.module_12_1 import Runner

"""
Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. 
Далее вызовите метод walk у этого объекта 10 раз. 
После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. 
Далее вызовите метод run у этого объекта 10 раз. 
После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. 
Далее 10 раз у объектов вызываются методы run и walk соответственно. 
Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
Скачайте исходный код для тестов.
Создайте класс RunnerTest и соответствующие описанию методы.
Запустите RunnerTest и убедитесь в правильности результатов.
Пример результата выполнения программы:
Вывод на консоль:
Ran 3 tests in 0.001s OK"""


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        Tests the walk method of the Runner class.
        Creates a Runner instance and calls walk 10 times.
        Verifies if the distance covered is 50 units.
        """
        runner = Runner('Bolt')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """
        Tests the run method of the Runner class.
        Creates a Runner instance and calls run 10 times.
        Verifies if the distance covered is 100 units.
        """
        runner = Runner('Bolt')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

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
