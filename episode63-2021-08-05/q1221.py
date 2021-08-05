class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        split_count = 0
        for char in s:
            if char == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                split_count += 1
        return split_count


if __name__ == '__main__':
    s = "RLRRLLRLRL"
    print(Solution().balancedStringSplit(s))
