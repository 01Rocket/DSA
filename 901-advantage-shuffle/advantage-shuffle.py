class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        indexed_nums2 = []
        for i in range(len(nums2)):
            indexed_nums2.append((nums2[i], i))

        indexed_nums2.sort(reverse=True)

        result = [0] * len(nums1)

        left = 0
        right = len(nums1) - 1

        for value, index in indexed_nums2:
            if nums1[right] > value:
                result[index] = nums1[right]
                right -= 1
            else:
                result[index] = nums1[left]
                left += 1

        return result