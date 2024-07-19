import re

from Utilities.read_file_to_string_array import read_to_string_array


class Day8:
    MAX_COLUMN = 50
    MAX_ROW = 6
    input_array = []
    display = []

    class Point:
        x = 0
        y = 0
        state = False

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.state = False

        def get_point(self):
            return self.x, self.y, self.state

        def switch_on(self):
            self.state = True

        def switch_off(self):
            self.state = False

        def rotate_x(self, a):
            self.y += a
            if self.y > Day8.MAX_ROW - 1:
                self.y -= Day8.MAX_ROW

        def rotate_y(self, a):
            self.x += a
            if self.x > Day8.MAX_COLUMN - 1:
                self.x -= Day8.MAX_COLUMN

    # rect 3x2
    # ###....
    # ###....
    # .......
    def rect(self, a, b):
        for i in range(b):
            for j in range(a):
                for item in self.display:
                    if item.get_point()[0] == j and item.get_point()[1] == i:
                        item.switch_on()

    def rotate_x_column(self, a, b):
        for item in self.display:
            if item.get_point()[0] == a:
                item.rotate_x(b)

    def rotate_y_row(self, a, b):
        for item in self.display:
            if item.get_point()[1] == a:
                item.rotate_y(b)

    def display_display(self):
        for i in range(self.MAX_ROW):
            for j in range(self.MAX_COLUMN):
                for item in self.display:
                    if item.get_point()[0] == j and item.get_point()[1] == i:
                        if item.get_point()[2] == True:
                            print("#", end="")
                        else:
                            print(" ", end="")
            print("")
        print("")

    def counter(self):
        result = 0
        for item in self.display:
            if item.get_point()[2]:
                result += 1

        return result

    def __init__(self, file):
        self.input_array = read_to_string_array(file)

        # 50 pixels wide and 6 pixels tall

        for i in range(self.MAX_ROW):
            for j in range(self.MAX_COLUMN):
                self.display.append(self.Point(j, i))

    def task1(self):
        for item in self.input_array:
            match = re.search(r'\Arect (\d+)x(\d+)', item)
            if match:
                self.rect(int(match.group(1)), int(match.group(2)))
            match = re.search(r'\Arotate column x=(\d+) by (\d+)', item)
            if match:
                self.rotate_x_column(int(match.group(1)), int(match.group(2)))
            match = re.search(r'\Arotate row y=(\d+) by (\d+)', item)
            if match:
                self.rotate_y_row(int(match.group(1)), int(match.group(2)))

        self.display_display()
        self.counter()

        return str(self.counter())

    def task2(self):
        pass
