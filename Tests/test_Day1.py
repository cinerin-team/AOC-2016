from unittest import TestCase

from Days.Day1 import Day1


class TestDay1(TestCase):
    def test_task1(self):
        expected_value = str(5)
        actual_value = Day1('../Resources/Day2/test1-1').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str(2)
        actual_value = Day1('../Resources/Day2/test1-2').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str(12)
        actual_value = Day1('../Resources/Day2/test1-3').task1()
        self.assertEqual(expected_value, actual_value)
