class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replace = {}

        for i in range(len(indices)):
            idx = indices[i]
            if s[idx:idx + len(sources[i])] == sources[i]:
                replace[idx] = (sources[i], targets[i])

        ans = []
        i = 0

        while i < len(s):
            if i in replace:
                source, target = replace[i]
                ans.append(target)
                i += len(source)
            else:
                ans.append(s[i])
                i += 1

        return "".join(ans)