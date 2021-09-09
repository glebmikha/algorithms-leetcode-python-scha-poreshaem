from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # O(n)
        nums_ind = [(nums[i], i) for i in range(n)]

        # O(nlog(n))
        nums_sorted = sorted(nums_ind, key=lambda tup: tup[0])

        # O(nlog(n))
        for i in range(n):
            compliment = target - nums_sorted[i][0]
            compliment_index = self.bs(nums_sorted, 0, n - 1, compliment)

            if compliment_index is not None and compliment_index != i:
                return [nums_sorted[i][1],
                        nums_sorted[compliment_index][1]]

    def bs(self, arr, start, end, target):
        # base case
        if end <= start:
            if arr[start][0] == target:
                return start
            return

        # recursive case
        mid = start + ((end - start) // 2)
        if target == arr[mid][0]:
            return mid
        elif target < arr[mid][0]:
            return self.bs(arr, start, mid - 1, target)
        elif target > arr[mid][0]:
            return self.bs(arr, mid + 1, end, target)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            compliment = target - nums[i]
            if nums[i] in d:
                return [i, d[nums[i]]]
            else:
                d[compliment] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
