class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answers = [0] * n

        steps, curr = 0, 0
        for i in range(n):
            answers[i] += steps
            curr += int(boxes[i])
            steps += curr

        steps, curr = 0, 0
        for i in range(n-1, -1, -1):
            answers[i] += steps
            curr += int(boxes[i])
            steps += curr
        return answers


if __name__ == '__main__':
    boxes = '110'
    print(Solution().minOperations(boxes))
