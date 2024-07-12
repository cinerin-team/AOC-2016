from Utilities.read_file_to_string_array import read_to_string_array


class Day8:
    input_array = []
    display = []

    def switch_on(self, x, y):
        self.display[y][x] = 1

    def switch_off(self, x, y):
        self.display[y][x] = 0

    # rect 3x2
    # ###....
    # ###....
    # .......
    def rect(self, a, b):
        for i in range(b):
            for j in range(a):
                self.switch_on(j,i)



    def __init__(self, file):
        self.input_array = read_to_string_array(file)

        # 50 pixels wide and 6 pixels tall
        column = 50
        row = 6

        for i in range(row):
            row = []
            for j in range(column):
                row.append(0)
            self.display.append(row)

    def task1(self):
        result = ""

        self.rect(3,2)
        for row in self.display:
            print(row)



        # code

        return result

    def task2(self):
        pass
