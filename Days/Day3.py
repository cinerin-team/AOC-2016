import re

from Utilities.read_file_to_string_array import read_to_string_array


class Day3:
    input_array = []

    def __init__(self, file):
        self.input_array = read_to_string_array(file)

    def task1(self):
        result = 0
        num_array = []
        num_array.clear()
        for line in self.input_array:
            pattern = r'\d+'
            num_array.append(re.findall(pattern, line))

        # code

        return str(result)

    def task2(self):
        pass
