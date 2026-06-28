class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def get_parts(num):
            real, imag = num[:-1].split("+")
            return int(real), int(imag)

        a, b = get_parts(num1)
        c, d = get_parts(num2)

        real = a * c - b * d
        imag = a * d + b * c

        return str(real) + "+" + str(imag) + "i"