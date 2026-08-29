class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = [0] * 5
        frogs = 0
        max_frogs = 0

        order = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}

        for ch in croakOfFrogs:
            i = order[ch]

            if ch == 'c':
                count[0] += 1
                frogs += 1
                max_frogs = max(max_frogs, frogs)

            else:
                # Previous letter must already exist
                if count[i - 1] == count[i]:
                    return -1

                count[i] += 1

                # A frog finishes after 'k'
                if ch == 'k':
                    frogs -= 1

        # All frogs must finish their croak
        if frogs != 0:
            return -1

        return max_frogs