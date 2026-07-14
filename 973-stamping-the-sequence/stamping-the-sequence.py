class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m = len(stamp)
        n = len(target)

        target = list(target)
        answer = []
        visited = [False] * (n - m + 1)
        replaced = 0

        while replaced < n:
            changed = False

            for i in range(n - m + 1):
                if not visited[i] and self.canStamp(target, stamp, i):
                    count = self.doStamp(target, i, m)
                    if count > 0:
                        replaced += count
                        changed = True
                        visited[i] = True
                        answer.append(i)

            if not changed:
                return []

        return answer[::-1]

    def canStamp(self, target, stamp, pos):
        matched = False

        for i in range(len(stamp)):
            if target[pos + i] == '*':
                continue
            if target[pos + i] != stamp[i]:
                return False
            matched = True

        return matched

    def doStamp(self, target, pos, length):
        changed = 0

        for i in range(length):
            if target[pos + i] != '*':
                target[pos + i] = '*'
                changed += 1

        return changed