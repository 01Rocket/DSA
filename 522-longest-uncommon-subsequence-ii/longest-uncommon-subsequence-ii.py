class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s, t):
            i = 0
            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1
            return i == len(s)

        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            ok = True
            for j in range(len(strs)):
                if i != j and is_subseq(strs[i], strs[j]):
                    ok = False
                    break
            if ok:
                return len(strs[i])

        return -1