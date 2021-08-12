from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # O(nlog(n))
        points.sort(key=lambda x: x[0])
        gaps = []
        n = len(points)
        # O(n)
        for i in range(1, n):
            gaps.append(points[i][0] - points[i - 1][0])
        # O(n)
        return max(gaps)


if __name__ == '__main__':
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print(Solution().maxWidthOfVerticalArea(points))
