from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        increase = 0
        n = len(grid)

        max_for_rows = []
        for i in range(n):
            max_for_rows.append(max(grid[i]))

        max_for_cols = []
        for i in range(n):
            max_for_cols.append(max([row[i] for row in grid]))

        for i in range(n):
            for j in range(n):
                increase += min(max_for_rows[i], max_for_cols[j]) - grid[i][j]

        return increase


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(Solution().maxIncreaseKeepingSkyline(grid))
