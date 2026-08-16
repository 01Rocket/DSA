class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def days_from_start(date):
            year, month, day = map(int, date.split('-'))

            # Days in previous years
            days = (year - 1971) * 365

            # Add leap years
            for y in range(1971, year):
                if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
                    days += 1

            # Days in previous months
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            for m in range(month - 1):
                days += month_days[m]

            # Add leap day if needed
            if month > 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
                days += 1

            days += day

            return days

        return abs(days_from_start(date1) - days_from_start(date2))