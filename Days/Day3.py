import re

from Utilities.read_file_to_string_array import read_to_string_array


class Day3:
    input_array = []

    def __init__(self, file):
        self.input_array = read_to_string_array(file)

    def task1(self):
        result = 0
        for triangle in self.input_array:
            a = int(triangle[0:5])
            b = int(triangle[6:10])
            c = int(triangle[11:15])
            if a + b > c and a + c > b and c + b > a:
                result += 1
        return str(result)

    def task2(self):
        result = 0
        oszlop1 = []
        oszlop2 = []
        oszlop3 = []
        for triangle in self.input_array:
            oszlop1.append(int(triangle[0:5]))
            oszlop2.append(int(triangle[6:10]))
            oszlop3.append(int(triangle[11:15]))
            if len(oszlop1) == 3:
                if self.test_values(oszlop1[0], oszlop1[1], oszlop1[2]):
                    result += 1
                if self.test_values(oszlop2[0], oszlop2[1], oszlop2[2]):
                    result += 1
                if self.test_values(oszlop3[0], oszlop3[1], oszlop3[2]):
                    result += 1
                oszlop1.clear()
                oszlop2.clear()
                oszlop3.clear()

        return str(result)

    def test_values(self,a, b, c):
        if a + b > c and a + c > b and c + b > a:
            return True





