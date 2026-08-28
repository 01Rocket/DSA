class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []

        def build(s):
            if len(s) == n:
                result.append(s)
                return

            for ch in "abc":
                if not s or s[-1] != ch:
                    build(s + ch)

        build("")

        if k > len(result):
            return ""

        return result[k - 1]