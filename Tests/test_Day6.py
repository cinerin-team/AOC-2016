from unittest import TestCase

from Days.Day6 import Day6


class TestDay6(TestCase):
    def test_task1(self):
        expected_value = "easter"
        actual_value = Day6('../Resources/Day6/test1').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str('advent')
        actual_value = Day6('../Resources/Day6/test1').task2()
        self.assertEqual(expected_value, actual_value)

    def test_orig(self):
        pass
        expected_value = str("qqqluigu")
        actual_value = Day6('../Resources/Day6/input').task1()
        self.assertEqual(expected_value, actual_value)
        #
        expected_value = str("lsoypmia")
        actual_value = Day6('../Resources/Day6/input').task2()
        self.assertEqual(expected_value, actual_value)
