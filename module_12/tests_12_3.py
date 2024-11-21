import unittest

from module_12.module_12_1 import Runner
from module_12.module_12_2 import Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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


class TournamentTest(unittest.TestCase):
    """
        Test case to check correctness of the results of the class Tournament
    """
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usein_nick(self):
        """
        Test that Usain and Nick compete correctly in the tournament.
        Usain, with a higher speed, should finish first.
        """
        t = Tournament(90, self.usein, self.nick)
        results = t.start()
        index = len(self.__class__.all_results) + 1
        self.__class__.all_results[index] = {key: value.name for key, value in
                                             results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_andrei_nick(self):
        """
       Test that Andrei and Nick compete correctly in the tournament.
       Andrei, with a higher speed, should finish first.
       """
        t = Tournament(90, self.andrei, self.nick)
        results = t.start()
        index = len(self.__class__.all_results) + 1
        self.__class__.all_results[index] = {key: value.name for key, value in
                                             results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_andrei_usein_nick(self):
        """
       Test that Usain, Andrei, and Nick compete correctly in the tournament.
       The order of finishers should match their speeds:
       - Usain (fastest) should finish first.
       - Andrei (second fastest) should finish second.
       - Nick (slowest) should finish last.
       """
        t = Tournament(90, self.andrei, self.usein, self.nick)
        results = t.start()
        index = len(self.__class__.all_results) + 1
        self.__class__.all_results[index] = {key: value.name for key, value in
                                             results.items()}
        self.assertEqual(results[1].name, 'Усэйн')  # Усэйн должен быть первым
        self.assertEqual(results[2].name, 'Андрей')  # Андрей должен быть вторым
        self.assertEqual(results[3].name, 'Ник')  # Ник должен быть последним
