class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rec = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rec[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]


if __name__ == '__main__':
    rec = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
    sq = SubrectangleQueries(rec)
    print(sq.rec)
    print(sq.getValue(0, 1))
    sq.updateSubrectangle(0, 0, 3, 2, 5)
    print(sq.rec)
