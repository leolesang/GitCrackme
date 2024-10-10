class Unscrambler:
    def __init__(self):
        self.c1 = 10
        self.c2 = 13.3
        self.flag = ""
        self.pad = "abcdefghijklmnopqrstuvwxyz"
        self.scr_flag = "es1d_1d_qw4r_q0c_nc4nvx3_0i02_us4mz"

    def unscramble(self):
        string_builder = []
        array_of_string = str((self.c1 * self.c2 + 0.7) * self.c1).split(".")
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
