class Solution:
    def minProductSum(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        n = len(nums1)
        s = 0
        for i in range(n):
            s = s + nums1[i] * nums2[i]
        return s


if __name__ == '__main__':
    n1 = [1, 2]
    n2 = [4, 6]
    print(Solution().minProductSum(n1, n2))
