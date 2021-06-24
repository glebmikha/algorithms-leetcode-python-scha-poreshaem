class Solution:  # O(n**2)
    def minOperations(self, boxes: str) -> list[int]:
        answers = []
        n = len(boxes)
        for i in range(n):
            op = 0
            for j in range(n):
                if boxes[j] == '1':
                    op = op + abs(i - j)
            answers.append(op)
        return answers


class Solution:  # O(n)
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n
        curr, steps = 0, 0
        for i in range(n):
            answer[i] += steps
            curr += int(boxes[i])
            steps += curr
        curr, steps = 0, 0
        for i in reversed(range(n)):
            answer[i] += steps
            curr += int(boxes[i])
            steps += curr
        return answer


if __name__ == '__main__':
    boxes = "110"
    print(Solution().minOperations(boxes))
