import re

import six

from Utilities.read_file_to_string import read_to_string


class Day9:
    input_string = ""
    input_string2 = ""

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

    # (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN
    def decompress2(self, decompressed_count, temp):
        match = re.search(r'\((\d+)x(\d+)\)', temp)
        if match:
            mit = match.group(1)
            mennyivel = match.group(2)
            match2 = re.search(r'\(' + mit + 'x' + mennyivel + '\)(.{' + mit + '})', temp)
            if match2:
                temp = re.sub(match2.group(0).replace("(", "\(").replace(")", "\)"), "", temp, 1)
                if "(" in match2.group(1):
                    decompressed_count += self.decompress2(decompressed_count, match2.group(1)) * int(mennyivel)
                else:
                    decompressed_count += int(mit) * int(mennyivel)

        return decompressed_count + len(temp)

    def decomp3(self, decompressed_count, str):
        pass

    def task1(self):

        result = self.decompress(self.input_string)
        return str(len(result))


    def task2(self):
        self.input_string2 = self.input_string
        decompressed_count = 0
        decompressed_count = self.decompress2(decompressed_count, self.input_string2)

        return str(decompressed_count)

