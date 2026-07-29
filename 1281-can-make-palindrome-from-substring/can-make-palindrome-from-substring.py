class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [0]

        mask = 0
        for ch in s:
            mask ^= 1 << (ord(ch) - ord('a'))
            prefix.append(mask)

        answer = []

        for left, right, k in queries:
            # Characters with odd frequency in the substring
            odd_mask = prefix[right + 1] ^ prefix[left]

            # Count set bits (odd-frequency characters)
            odd_count = odd_mask.bit_count()

            # Minimum replacements needed
            answer.append(odd_count // 2 <= k)

        return answer