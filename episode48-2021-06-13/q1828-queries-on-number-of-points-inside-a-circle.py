class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:

        points_inside = []

        for querie in queries:
            num_points_inside = 0
            for point in points:
                if (querie[0] - point[0]) ** 2 + (querie[1] - point[1]) ** 2 <= querie[2] ** 2:
                    num_points_inside = num_points_inside + 1
            points_inside.append(num_points_inside)

        return points_inside


if __name__ == '__main__':
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    print(Solution().countPoints(points, queries))
