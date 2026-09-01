class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Make the largest possible number
        max_num = s
        for digit in s:
            if digit != '9':
                max_num = s.replace(digit, '9')
                break

        # Make the smallest possible number
        min_num = s

        if s[0] != '1':
            min_num = s.replace(s[0], '1')
        else:
            for digit in s[1:]:
                if digit not in ('0', '1'):
                    min_num = s.replace(digit, '0')
                    break

        return int(max_num) - int(min_num)