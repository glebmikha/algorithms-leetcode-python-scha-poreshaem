class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = []
        for i in range(0, n, 2):
            answer += nums[i] * [nums[i+1]]
        return answer



if __name__ == '__main__':
    nums = [1, 1, 2, 3]
    print(Solution().decompressRLElist(nums))
