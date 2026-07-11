class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()

        for word in words:
            even = sorted(word[::2])
            odd = sorted(word[1::2])
            groups.add(("".join(even), "".join(odd)))

        return len(groups)