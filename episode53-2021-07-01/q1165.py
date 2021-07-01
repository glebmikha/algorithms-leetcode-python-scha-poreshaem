class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cur = 0
        time = 0
        layout = {}
        for i, c in enumerate(keyboard):
            layout[c] = i

        for c in word:
            new = layout[c]
            time = time + abs(cur - new)
            cur = new

        return time


if __name__ == '__main__':
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
    print(Solution().calculateTime(keyboard, word))
