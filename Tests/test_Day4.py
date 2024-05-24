from unittest import TestCase

from Days.Day4 import Day4


class TestDay4(TestCase):
    def test_task1(self):
        expected_value = str(1514)
        actual_value = Day4('../Resources/Day4/test1').task1()
        self.assertEqual(expected_value, actual_value)

    def test_encrypt(self):
        expected_value = str('very encrypted name')
        actual_value = Day4('../Resources/Day4/test2').encrypt("qzmt-zixmtkozy-ivhz", 343)
        self.assertEqual(expected_value, actual_value)

    def test_orig(self):
        expected_value = str(409147)
        actual_value = Day4('../Resources/Day4/input').task1()
        self.assertEqual(expected_value, actual_value)
        #
        expected_value = str(991)
        actual_value = Day4('../Resources/Day4/input').task2()
        self.assertEqual(expected_value, actual_value)
