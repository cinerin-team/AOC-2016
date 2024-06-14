from Utilities.read_file_to_string_array import read_to_string_array


class Day6:
    input_array = []

    def __init__(self, file):
        self.input_array = read_to_string_array(file)

    def task1(self):
        result = ""

        dict_array = []
        for i in range(len(self.input_array[0])):
            dict_array.append({})

        for message in self.input_array:
            for i, character in enumerate(message):
                if character not in dict_array[i].keys():
                    dict_array[i][character] = 1
                else:
                    dict_array[i][character] = dict_array[i][character] + 1

        for _dict in dict_array:
            result += max(_dict, key=_dict.get)

        return result

    def task2(self):
        result = ""

        dict_array = []
        for i in range(len(self.input_array[0])):
            dict_array.append({})

        for message in self.input_array:
            for i, character in enumerate(message):
                if character not in dict_array[i].keys():
                    dict_array[i][character] = 1
                else:
                    dict_array[i][character] = dict_array[i][character] + 1

        for _dict in dict_array:
            result += min(_dict, key=_dict.get)

        return result
