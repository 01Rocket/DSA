class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        for ch in reversed(s):
            k %= size

            if ch.isalpha():
                if k == 0:
                    return ch
                size -= 1
            else:
                size //= int(ch)