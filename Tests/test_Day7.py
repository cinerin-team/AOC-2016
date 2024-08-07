from unittest import TestCase

from Days.Day7 import abba, Day7, bab, aba


class TestDay7(TestCase):

    def test_abba(self):
        expected_value = True
        actual_value = abba('abba')
        self.assertEqual(expected_value, actual_value)

    def test_abba2(self):
        expected_value = False
        actual_value = abba('zxcvbn')
        self.assertEqual(expected_value, actual_value)

    def test_aba(self):
        expected_value = ["php"]
        actual_value = aba("php")
        self.assertEqual(expected_value, actual_value)

        expected_value = ["zaz", "zbz"]
        actual_value = aba('zazbz')
        self.assertEqual(expected_value, actual_value)

        expected_value = []
        actual_value = aba("abc")
        self.assertEqual(expected_value, actual_value)

    def test_bab(self):
        expected_value = True
        actual_value = bab("php", ["hph"])
        self.assertEqual(expected_value, actual_value)

        expected_value = False
        actual_value = bab("abc", "cba")
        self.assertEqual(expected_value, actual_value)

        expected_value = False
        actual_value = bab("aba", "cbc")
        self.assertEqual(expected_value, actual_value)

    def test_task1(self):
        expected_value = str('2')
        actual_value = Day7('../Resources/Day7/test1').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str('3')
        actual_value = Day7('../Resources/Day7/test2').task2()
        self.assertEqual(expected_value, actual_value)

    def test_orig(self):
        pass
        expected_value = str('105')
        actual_value = Day7('../Resources/Day7/input').task1()
        self.assertEqual(expected_value, actual_value)
        #
        expected_value = str('258')
        actual_value = Day7('../Resources/Day7/input').task2()
        self.assertEqual(expected_value, actual_value)
