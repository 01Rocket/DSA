class Solution:
    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11

        def is_prime(num):
            if num < 2:
                return False
            if num % 2 == 0:
                return num == 2

            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        x = 1

        while True:
            s = str(x)
            palindrome = int(s + s[-2::-1])

            if palindrome >= n and is_prime(palindrome):
                return palindrome

            x += 1