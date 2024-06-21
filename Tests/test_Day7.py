from unittest import TestCase

from Days.Day7 import abba, Day7


class TestDay7(TestCase):

    def test_abba(self):
        expected_value = True
        actual_value = abba('abba')
        self.assertEqual(expected_value, actual_value)

    def test_abba2(self):
        expected_value = False
        actual_value = abba('zxcvbn')
        self.assertEqual(expected_value, actual_value)

    def test_task1(self):
        expected_value = str('2')
        actual_value = Day7('../Resources/Day7/test1').task1()
        self.assertEqual(expected_value, actual_value)

    # def test_task2(self):
    #     expected_value = str('5DB3')
    #     actual_value = Day7('../Resources/Day7/test1-1').task2()
    #     self.assertEqual(expected_value, actual_value)

    # def test_orig(self):
    #     pass
    #     expected_value = str(61529)
    #     actual_value = Day7('../Resources/Day7/input').task1()
    #     self.assertEqual(expected_value, actual_value)
    #     #
    #     expected_value = str('C2C28')
    #     actual_value = Day7('../Resources/Day7/input').task2()
    #     self.assertEqual(expected_value, actual_value)
