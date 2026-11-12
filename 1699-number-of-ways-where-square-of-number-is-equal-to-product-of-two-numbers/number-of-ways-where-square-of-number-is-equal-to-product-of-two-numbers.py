class Solution:
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        def countTriplets(a, b):
            freq = Counter(b)
            ans = 0

            for x in a:
                target = x * x

                for y in freq:
                    if target % y == 0:
                        z = target // y

                        if z in freq:
                            if y == z:
                                ans += freq[y] * (freq[y] - 1) // 2
                            elif y < z:
                                ans += freq[y] * freq[z]

            return ans

        return countTriplets(nums1, nums2) + countTriplets(nums2, nums1)