from unittest import TestCase

from Days.Day8 import Day8


class TestDay8(TestCase):
    def test_task1(self):
        expected_value = str('6')
        actual_value = Day8('../Resources/Day8/test1-1').task1()
        self.assertEqual(expected_value, actual_value)

        Day8('../Resources/Day8/test1-2').task1()
        Day8('../Resources/Day8/test1-3').task1()
        Day8('../Resources/Day8/test1-4').task1()

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
