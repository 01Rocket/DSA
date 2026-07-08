class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + "*****" + name[-1] + "@" + domain

        digits = []

        for ch in s:
            if ch.isdigit():
                digits.append(ch)

        digits = "".join(digits)
        country = len(digits) - 10

        local = "***-***-" + digits[-4:]

        if country == 0:
            return local

        return "+" + "*" * country + "-" + local