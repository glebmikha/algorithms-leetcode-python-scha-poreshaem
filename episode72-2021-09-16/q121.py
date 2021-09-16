from typing import List


# brute force O(n**2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        deals = []
        for i in range(n):
            for j in range(i + 1, n):
                deals.append(prices[j] - prices[i])
        return max(max(deals), 0)


# O(n**2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        while len(prices) > 1:
            # O(n)
            min_el = min(prices)
            max_el = max(prices)

            # O(n)
            min_el_ind = prices.index(min_el)
            max_el_ind = prices.index(max_el)

            if max_el_ind > min_el_ind:
                return max_el - min_el
            else:
                # O(n)
                del prices[max_el_ind]

        return 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        i = 0
        j = 1
        cur_max = prices[j] - prices[i]
        while i < j < n and i < n:
            if prices[j] <= prices[i]:
                j = j + 1
                i = i + 1
            else:
                cur = prices[j] - prices[i]
                if cur > cur_max:
                    cur_max = cur
                j = j + 1
        return cur_max


class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
