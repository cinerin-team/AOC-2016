import re

import six

from Utilities.read_file_to_string import read_to_string


class Day9:
    input_string = ""

    def __init__(self, file):
        self.input_string = read_to_string(file)

    @staticmethod
    def decompress(input_string):
        result = ""

        index = 0
        while index < len(input_string):
            if input_string[index] != "(":
                result += input_string[index]
                index += 1
            else:
                index += 1
                mennyit = ""
                mennyivel = ""
                while input_string[index] != "x":
                    mennyit += input_string[index]
                    index += 1
                index += 1
                while input_string[index] != ")":
                    mennyivel += input_string[index]
                    index += 1
                index += 1
                mit = input_string[index:index + int(mennyit)]
                result += (mit * int(mennyivel))
                index += len(mit)

        return result

    def decompress2(self):
        pass

    def task1(self):

        result = self.decompress(self.input_string)
        return str(len(result))


    def task2(self):
        decompressed_count = 0
        while "(" in self.input_string:
            match = re.search(r'\((\d+)x(\d+)\)', self.input_string)
            if match:
                mit = match.group(1)
                mennyivel = match.group(2)
                match2 = re.search(r'\('+mit+'x'+mennyivel+'\).{'+mit+'}', self.input_string)
                if match2:
                    decompressed_count += int(mit)*int(mennyivel)
                    self.input_string = re.sub(match2.group(0).replace("(","\(").replace(")","\)"), "", self.input_string)

        return str(len(self.input_string) + decompressed_count)

