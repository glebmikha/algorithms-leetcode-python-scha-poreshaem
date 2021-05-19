from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for account in accounts:
            s = 0
            for bank in account:
                s = s + bank
            wealth.append(s)

        cur_max = wealth[0]
        for w in wealth[1:]:
            if w > cur_max:
                cur_max = w

        return cur_max

    def maximum_wealth(self, accounts):
        return max([sum(acc) for acc in accounts])

    def maximum_wealth_ef(self, accounts):
        cur_max = float('-inf')
        for account in accounts:
            s = 0
            for bank in account:
                s = s + bank

            if s > cur_max:
                cur_max = s

        return cur_max


if __name__ == '__main__':
    accounts = [[1, 5], [7, 3], [3, 5]]

    print(Solution().maximum_wealth_ef(accounts))
