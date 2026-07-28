class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        data = []
        n = len(transactions)

        # Parse transactions
        for t in transactions:
            name, time, amount, city = t.split(",")
            data.append([name, int(time), int(amount), city])

        invalid = [False] * n

        # Check each transaction
        for i in range(n):
            if data[i][2] > 1000:
                invalid[i] = True

            for j in range(i + 1, n):
                if (
                    data[i][0] == data[j][0]
                    and data[i][3] != data[j][3]
                    and abs(data[i][1] - data[j][1]) <= 60
                ):
                    invalid[i] = True
                    invalid[j] = True

        result = []
        for i in range(n):
            if invalid[i]:
                result.append(transactions[i])

        return result