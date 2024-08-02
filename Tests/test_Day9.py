from unittest import TestCase

from Days.Day9 import Day9


class TestDay9(TestCase):
    def test_task1(self):
        expected_value = str('6')
        actual_value = Day9('../Resources/Day9/test1').task1()
        self.assertEqual(expected_value, actual_value)

    # def test_task2(self):
    #     expected_value = str('5DB3')
    #     actual_value = Day8('../Resources/Day8/test1-1').task2()
    #     self.assertEqual(expected_value, actual_value)

    # def test_orig(self):
    #     pass
    #     expected_value = str(119)
    #     actual_value = Day8('../Resources/Day8/input').task1()
    #     self.assertEqual(expected_value, actual_value)
    #     #
    #     expected_value = str('C2C28')
    #     actual_value = Day8('../Resources/Day8/input').task2()
    #     self.assertEqual(expected_value, actual_value)
