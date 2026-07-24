class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give = 1
        index = 0

        while candies > 0:
            if candies >= give:
                result[index] += give
                candies -= give
            else:
                result[index] += candies
                break

            give += 1
            index = (index + 1) % num_people

        return result