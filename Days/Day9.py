import six

from Utilities.read_file_to_string import read_to_string


class Day9:
    input_string = ""

    def __init__(self, file):
        self.input_string = read_to_string(file)

    def task1(self):
        result = ""
        index = 0
        while index < len(self.input_string):
            if self.input_string[index] != "(":
                result += self.input_string[index]
                index += 1
            else:
                index += 1
                mennyit = ""
                mennyivel = ""
                while self.input_string[index] != "x":
                    mennyit += self.input_string[index]
                    index += 1
                index += 1
                while self.input_string[index] != ")":
                    mennyivel += self.input_string[index]
                    index += 1
                index += 1
                mit = self.input_string[index:index+int(mennyit)]
                result += (mit * int(mennyivel))
                index += len(mit)

        return str(len(result))

    def task2(self):
        result = ""
        uj_input = self.input_string
        while "(" in uj_input:
            index = 0
            result = ""
            while index < len(uj_input):
                if uj_input[index] != "(":
                    result += uj_input[index]
                    index += 1
                else:
                    index += 1
                    mennyit = ""
                    mennyivel = ""
                    while uj_input[index] != "x":
                        mennyit += uj_input[index]
                        index += 1
                    index += 1
                    while uj_input[index] != ")":
                        mennyivel += uj_input[index]
                        index += 1
                    index += 1
                    mit = uj_input[index:index+int(mennyit)]
                    result += (mit * int(mennyivel))
                    index += len(mit) * int(mennyivel) + 1

            uj_input = result
            continue

        print(result)
        return str(len(result))
