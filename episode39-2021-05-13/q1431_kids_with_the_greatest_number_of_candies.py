from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_true = []

        for i in range(len(candies)):
            candies_copy = candies.copy()
            candies_copy[i] = candies_copy[i] + extraCandies

            cur_max = candies_copy[0]
            for kid in candies_copy[1:]:
                if kid > cur_max:
                    cur_max = kid

            max_indexes = []
            for k in range(len(candies_copy)):
                if candies_copy[k] == cur_max:
                    max_indexes.append(k)

            if i in max_indexes:
                max_true.append(True)
            else:
                max_true.append(False)

        return max_true

    def kids_with_candies(self, candies, extraCandies):
        max_el = max(candies)

        for i in range(len(candies)):
            candies[i] = (candies[i] - max_el + extraCandies) >= 0

        return candies

    def kids_with_candies_one_on2(self, candies, extraCandies):
        return [el + extraCandies >= max(candies) for el in candies]

    def kids_with_candies_one_on(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_el = max(candies)
        return [el + extraCandies >= max_el for el in candies]


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    delta = [-3, -2, 0, -4, -2]
    extraCandies = 3

    print(Solution().kids_with_candies_one(candies, extraCandies))
