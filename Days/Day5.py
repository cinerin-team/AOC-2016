import hashlib

from Utilities.read_file_to_string import read_to_string


class Day5:
    input_string = ""

    def __init__(self, file):
        self.input_string = read_to_string(file)

    def task1(self):
        result = ""

        # code

        return result

    def task2(self):
        pass

    def md5_hash(self, bemenet):
        result = hashlib.md5(bemenet.encode()).hexdigest()

        return result
