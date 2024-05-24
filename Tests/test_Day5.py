from unittest import TestCase

from Days.Day5 import Day5


class TestDay5(TestCase):
    def test_task1(self):
        expected_value = "18f47a30"
        actual_value = Day5('../Resources/Day5/test1').task1()
        self.assertEqual(expected_value, actual_value)

    # def test_task2(self):
    #     expected_value = str('very encrypted name')
    #     actual_value = Day5('../Resources/Day5/test2').task2()
    #     self.assertEqual(expected_value, actual_value)

    # def test_orig(self):
    #     expected_value = str(409147)
    #     actual_value = Day5('../Resources/Day5/input').task1()
    #     self.assertEqual(expected_value, actual_value)
    #
    #     expected_value = str(991)
    #     actual_value = Day5('../Resources/Day5/input').task2()
    #     self.assertEqual(expected_value, actual_value)
