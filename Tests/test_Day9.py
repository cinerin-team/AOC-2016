from unittest import TestCase

from Days.Day9 import Day9


class TestDay9(TestCase):
    def test_task1(self):
        expected_value = str('6')
        actual_value = Day9('../Resources/Day9/test1').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('7')
        actual_value = Day9('../Resources/Day9/test2').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('9')
        actual_value = Day9('../Resources/Day9/test3').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('11')
        actual_value = Day9('../Resources/Day9/test4').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('6')
        actual_value = Day9('../Resources/Day9/test5').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('18')
        actual_value = Day9('../Resources/Day9/test6').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str('6')
        actual_value = Day9('../Resources/Day9/test1').task2()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('9')
        actual_value = Day9('../Resources/Day9/test3').task2()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('3')
        actual_value = Day9('../Resources/Day9/test5').task2()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('20')
        actual_value = Day9('../Resources/Day9/test6').task2()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('241920')
        actual_value = Day9('../Resources/Day9/test7').task2()
        self.assertEqual(expected_value, actual_value)

        expected_value = str('445')
        actual_value = Day9('../Resources/Day9/test8').task2()
        self.assertEqual(expected_value, actual_value)


    def test_orig(self):
        expected_value = str(70186)
        actual_value = Day9('../Resources/Day9/input').task1()
        self.assertEqual(expected_value, actual_value)

        # expected_value = str('7')
        # actual_value = Day9('../Resources/Day9/test2').task2()
        # self.assertEqual(expected_value, actual_value)
    #     #
    #     expected_value = str('C2C28')
    #     actual_value = Day8('../Resources/Day8/input').task2()
    #     self.assertEqual(expected_value, actual_value)
