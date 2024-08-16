from Utilities.read_file_to_string import read_to_string


class Day9:
    input_string = ""

    def __init__(self, file):
        self.input_string = read_to_string(file)

    def decompress(self, input_string):
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

    def task1(self):

        result = self.decompress(self.input_string)
        return str(len(result))

    def task2(self):

        input = self.input_string
        while '(' in input:
            input = self.decompress(input)

        return str(len(input))