class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split("@")

            # Ignore everything after the first '+'
            if "+" in local:
                local = local[:local.index("+")]

            # Remove all dots from the local name
            local = local.replace(".", "")

            # Store the normalized email
            unique.add(local + "@" + domain)

        return len(unique)