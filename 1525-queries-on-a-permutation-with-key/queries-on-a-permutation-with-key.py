class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))
        result = []

        for query in queries:
            position = p.index(query)
            result.append(position)

            p.remove(query)
            p.insert(0, query)

        return result