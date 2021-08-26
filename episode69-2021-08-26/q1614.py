class Solution:
    def maxDepth(self, s: str) -> int:
        depth = [0]
        for i, char in enumerate(s):
            depth.append(s[:i].count('(') - s[:i].count(')'))
        return max(depth)


if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"
    print(Solution().maxDepth(s))
