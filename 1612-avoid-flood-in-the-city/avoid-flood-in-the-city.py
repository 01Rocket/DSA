class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        ans = [1] * n

        # Last day when each lake got rain
        last = {}

        # Days on which we can dry a lake
        dry_days = []

        for day, lake in enumerate(rains):

            if lake == 0:
                dry_days.append(day)
                continue

            ans[day] = -1

            # Lake is already full, so we must dry it first
            if lake in last:
                pos = bisect_right(dry_days, last[lake])

                if pos == len(dry_days):
                    return []

                dry_day = dry_days.pop(pos)
                ans[dry_day] = lake

            last[lake] = day

        return ans