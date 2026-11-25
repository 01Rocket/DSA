class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        records = defaultdict(list)

        # Convert HH:MM into minutes
        for name, time in zip(keyName, keyTime):
            h, m = map(int, time.split(":"))
            records[name].append(h * 60 + m)

        ans = []

        for name, times in records.items():
            times.sort()

            # Check every consecutive group of 3
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    ans.append(name)
                    break

        return sorted(ans)