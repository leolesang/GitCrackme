class Unscrambler:
    def __init__(self):
        self.flag = ""
        self.pad = "abcdefghijklmnopqrstuvwxyz"
        self.scr_flag = "qw4r_q0c_nc4nvx3_0i01_srq82q8mx"

    def unscramble(self):
        string_builder = []
        array_of_string = str(1337.0).split(".")
        j = int(array_of_string[0])
        array_of_char = list(self.scr_flag)
        i = len(array_of_char)
        b = 0

        while b < i:
            c = array_of_char[b]
            print(f"Char: {c}")
            k = self.pad.index(c) if c in self.pad else -1
            print(f"indexOf: {k}")

            if k < 0:
                str_val = c
            else:
                k = (k - j) % len(self.pad)
                if k < 0:
                    str_val = self.pad[k + len(self.pad)]
                else:
                    str_val = self.pad[k]

            print(f"letter {str_val}")
            string_builder.append(str_val)
            b += 1

        flag = ''.join(string_builder)
        print(f"FLAG: {flag}")
        return flag

# Example usage
unscrambler = Unscrambler()
unscrambler.unscramble()
