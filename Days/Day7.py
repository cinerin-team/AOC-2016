from Utilities.read_file_to_string_array import read_to_string_array


# ucibfxxivatgxlupp
# abba 0123
def abba(abba_input):
    for index in range(len(abba_input) - 3):
        if abba_input[index] == abba_input[index + 3] and abba_input[index + 1] == abba_input[index + 2] and \
                abba_input[index] != abba_input[index + 1]:
            return True

    return False


class Day7:
    input_array = []

    def __init__(self, file):
        self.input_array = read_to_string_array(file)

    def task1(self):
        result = 0

        subnet = ""
        hypernet = ""

        # rnqfzoisbqxbdlkgfh[lwlybvcsiupwnsyiljz]kmbgyaptjcsvwcltrdx[ntrpwgkrfeljpye]jxjdlgtntpljxaojufe
        # abba[mnop]qrst

        for ip in self.input_array:

            subnet_counter = 0
            hypernet_counter = 0
            counter = 0

            while counter < len(ip):
                subnet = ""

                while counter < len(ip) and ip[counter] != '[':
                    subnet += ip[counter]
                    counter += 1

                if abba(subnet):
                    subnet_counter += 1

                counter += 1
                subnet = ""
                hypernet = ""

                while counter < len(ip) and ip[counter] != ']' :
                    hypernet += ip[counter]
                    counter += 1

                if abba(hypernet):
                    hypernet_counter += 1

                counter += 1
                hypernet = ""

            if hypernet_counter == 0 and subnet_counter > 0:
                result += 1

        return str(result)

    def task2(self):
        pass



