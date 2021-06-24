class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2:
                num = num - 1
            else:
                num = num / 2
            steps = steps + 1
        return steps

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return num // 2 - 1 if (num // 2) % 2 else num // 2


if __name__ == '__main__':
    num = 8
    print(Solution().numberOfSteps(num))