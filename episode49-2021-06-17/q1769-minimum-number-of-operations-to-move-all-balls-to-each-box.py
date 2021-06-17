class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        answers = []
        n = len(boxes)
        for i in range(n):
            op = 0
            for j in range(n):
                if boxes[j] == '1':
                    op = op + abs(i-j)
            answers.append(op)
        return answers

if __name__ == '__main__':
    boxes = "110"
    print(Solution().minOperations(boxes))