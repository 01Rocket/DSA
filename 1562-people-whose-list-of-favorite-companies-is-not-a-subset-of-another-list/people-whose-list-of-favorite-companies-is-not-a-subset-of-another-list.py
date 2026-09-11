class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        result = []

        companies = [set(x) for x in favoriteCompanies]

        for i in range(len(companies)):
            is_subset = False

            for j in range(len(companies)):
                if i != j and companies[i].issubset(companies[j]):
                    is_subset = True
                    break

            if not is_subset:
                result.append(i)

        return result