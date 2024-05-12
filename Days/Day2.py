from Utilities.read_file_to_string_array import read_to_string_array


class Day2:
    input_array = []  # ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    keypad_dict = {}
    x = None
    y = None

    def __init__(self, file):
        self.input_array = read_to_string_array(file)


    def task1(self):
        self.x = 1
        self.y = 1

        self.keypad_dict.clear()      # x, y
        self.keypad_dict = {(-1, 1): 1, (0, 1): 2, (1, 1): 3,
                            (-1, 0): 4, (0, 0): 5, (1, 0): 6,
                            (-1, -1): 7, (0, -1): 8, (1, -1): 9}

        result = ""

        for digits in self.input_array:
            for letter in digits:
                if letter == 'U':
                    self.up()
                    continue
                if letter == 'D':
                    self.down()
                    continue
                if letter == 'L':
                    self.left()
                    continue
                if letter == 'R':
                    self.right()
                    continue

            result += str(self.keypad_dict[(self.x, self.y)])

        return result

    def task2(self):
        self.x = -2
        self.y = 0

        self.keypad_dict.clear()
        self.keypad_dict = {(0, 2): '1', (-1, 1): '2', (0, 1): '3',
                            (1, 1): '4', (-2, 0): '5', (-1, 0): '6',
                            (0, 0): '7', (1, 0): '8', (2, 0): '9',
                            (0, -1): 'B', (-1, -1): 'A', (1, -1): 'C', (0, -2): 'D'}

        result = ""

        for digits in self.input_array:
            for letter in digits:
                if letter == 'U':
                    self.up()
                    continue
                if letter == 'D':
                    self.down()
                    continue
                if letter == 'L':
                    self.left()
                    continue
                if letter == 'R':
                    self.right()
                    continue

            result += self.keypad_dict[(self.x, self.y)]

        return result

    def up(self):
        if (self.x, self.y + 1) in self.keypad_dict.keys():
            self.y += 1

    def down(self):
        if (self.x, self.y - 1) in self.keypad_dict.keys():
            self.y -= 1

    def left(self):
        if (self.x - 1, self.y) in self.keypad_dict.keys():
            self.x -= 1

    def right(self):
        if (self.x + 1, self.y) in self.keypad_dict.keys():
            self.x += 1