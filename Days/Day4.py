import re

from Utilities.read_file_to_string_array import read_to_string_array


class Day4:
    input_array = []

    def __init__(self, file):
        self.input_array = read_to_string_array(file)

    def task1(self):
        result = 0
        for item in self.input_array:
            match = re.match(r"^(.*)-(\d+)\[(.*)\]$", item)
            if self.calc_checksum(match.group(1)) == match.group(3):
                result += int(match.group(2))

        return str(result)

    def calc_checksum(self, alma):
        letter_dict = {}
        # '-' kitörlése
        alma = re.sub(r'-', '', alma)
        for letter in alma:
            if letter in letter_dict.keys():
                letter_dict[letter] = int(letter_dict[letter]) + 1
            else:
                letter_dict[letter] = 1
        # a sorted visszaad egy tupléból álló tömbot és a tuple tartalmazza a kulcsot és az értéket, az első értéke a kulcs, a második a value
        tmp = sorted(letter_dict.items(), key=lambda x: (-x[1], x[0]))
        result = tmp[0][0] + tmp[1][0] + tmp[2][0] + tmp[3][0] + tmp[4][0]

        return result

    def task2(self):
        result = 0
        for item in self.input_array:
            match = re.match(r"^(.*)-(\d+)\[(.*)\]$", item)
            if self.encrypt(match.group(1), int(match.group(2))) == "northpole object storage":
                result = match.group(2)

        return str(result)

    def encrypt(self, banan, cekla):
        result = ""
        banan = re.sub(r'-', ' ', banan)

        for letter in banan:
            if letter == " ":
                result += " "
            else:
                if ord(letter) + cekla % 26 > 122:  # ord visszaadja az ASCII karakter számát
                    result += chr(ord(letter) + cekla % 26 - 26)  # chr visszaadja a szám ASCII karakter értékét
                else:
                    result += chr(ord(letter) + cekla % 26)
        return result
