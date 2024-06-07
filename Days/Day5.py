import hashlib

from Utilities.read_file_to_string import read_to_string


class Day5:
    input_string = ""

    def __init__(self, file):
        self.input_string = read_to_string(file)

    def task1(self):
        result = ""

        i = 0
        while len(result) != 8:
            hash_input = self.input_string + str(i)
            tmp = self.md5_hash(hash_input)
            if tmp[:5] == "00000":
                result += tmp[5]
            i += 1

        return result

    def task2(self):
        result = "________"

        i = 0
        while '_' in result:
            hash_input = self.input_string + str(i)
            tmp = self.md5_hash(hash_input)
            try:
                if tmp[:5] == "00000":
                    if result[int(tmp[5])] == '_':
                        # result[int(tmp[5])] = tmp[6]
                        # __r_2_g_ = __r + x + 2_g_   tmp[5] = 4  tmp[6] = x
                        result = result[:int(tmp[5])] + tmp[6] + result[int(tmp[5]) + 1:]
            except (ValueError, IndexError):
                pass

            finally:
                i += 1

        return str(result)

    def md5_hash(self, bemenet):
        result = hashlib.md5(bemenet.encode()).hexdigest()

        return str(result)
