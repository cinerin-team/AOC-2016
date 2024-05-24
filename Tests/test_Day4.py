from unittest import TestCase

from Days.Day4 import Day4


class TestDay1(TestCase):
    def test_task1(self):
        expected_value = str(1514)
        actual_value = Day4('../Resources/Day4/test1').task1()
        self.assertEqual(expected_value, actual_value)

    # def test_task2(self):
    #     expected_value = str('5DB3')
    #     actual_value = Day4('../Resources/Day4/test1').task2()
    #     self.assertEqual(expected_value, actual_value)

    # def test_orig(self):
    #     pass
    #     expected_value = str(61529)
    #     actual_value = Day4('../Resources/Day4/input').task1()
    #     self.assertEqual(expected_value, actual_value)
    #     #
    #     expected_value = str('C2C28')
    #     actual_value = Day4('../Resources/Day4/input').task2()
    #     self.assertEqual(expected_value, actual_value)