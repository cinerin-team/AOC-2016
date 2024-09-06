import re

from Utilities.read_file_to_string_array import read_to_string_array


def give(value, dest, igen):
    if igen.keys().__contains__(dest):
        igen[dest].vodor.append(value)

    else:
        igen[dest] = Bot()
        igen[dest].vodor.append(value)

    if len(igen[dest].vodor) == 2:
        if igen[dest].vodor[0] < igen[dest].vodor[1]:
            give(igen[dest].vodor[0], igen[dest].lower_dest, igen)
            give(igen[dest].vodor[1], igen[dest].higher_dest, igen)
        else:
            give(igen[dest].vodor[1], igen[dest].lower_dest, igen)
            give(igen[dest].vodor[0], igen[dest].higher_dest, igen)
        igen[dest].vodor.clear()


class Day10:
    input_array = []
    def __init__(self, file):
        self.input_array = read_to_string_array(file)

    def task1(self):
        igen = {}
        for item in self.input_array:
            if item.startswith("value"):
                match = re.match(r'value (\d+) goes to (bot \d+)', item)
                if match:
                    give(match.group(1), match.group(2), igen)

            else:
                match = re.match(r'(bot \d+) gives low to (bot|output \d+) and high to (bot|output \d+)', item)
                if match:


    def task2(self):
        pass


class Bot:
    type = ""
    vodor = []
    lower_dest = ""
    higher_dest = ""

    def __init__(self):
        self.type = "bot"

class Output:
    type = ""
    vodor = []

    def __init__(self):
        self.type = "output"