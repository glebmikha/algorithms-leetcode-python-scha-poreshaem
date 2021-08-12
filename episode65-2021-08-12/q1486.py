class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(1, n):
            xor = xor ^ (start + i * 2)
        return xor


if __name__ == '__main__':
    n = 1
    start = 7
    print(Solution().xorOperation(n, start))
