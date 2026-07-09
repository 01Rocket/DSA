class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        # Graph: richer person -> poorer person
        graph = [[] for _ in range(n)]
        for rich, poor in richer:
            graph[poor].append(rich)

        answer = [-1] * n

        def dfs(person):
            if answer[person] != -1:
                return answer[person]

            # Initially, the quietest person is themselves
            answer[person] = person

            # Check all richer people
            for richerPerson in graph[person]:
                candidate = dfs(richerPerson)
                if quiet[candidate] < quiet[answer[person]]:
                    answer[person] = candidate

            return answer[person]

        for i in range(n):
            dfs(i)

        return answer