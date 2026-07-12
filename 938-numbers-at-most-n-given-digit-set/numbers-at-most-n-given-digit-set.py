class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m = len(s)
        d = len(digits)

        count = 0

        # Count numbers with fewer digits than n
        for length in range(1, m):
            count += d ** length

        # Count numbers with the same number of digits
        for i in range(m):
            smaller = 0

            for digit in digits:
                if digit < s[i]:
                    smaller += 1
                elif digit == s[i]:
                    break
                else:
                    break

            count += smaller * (d ** (m - i - 1))

            if s[i] not in digits:
                return count

        return count + 1