class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def isPrime(num):
            if num < 2:
                return False

            i = 2
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1

            return True

        prime_count = 0

        for i in range(1, n + 1):
            if isPrime(i):
                prime_count += 1

        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % MOD
            return result

        non_prime_count = n - prime_count

        return (factorial(prime_count) * factorial(non_prime_count)) % MOD