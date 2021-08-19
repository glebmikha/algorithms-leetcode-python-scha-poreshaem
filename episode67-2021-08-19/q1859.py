class Solution:
    def sortSentence(self, s: str) -> str:
        shuffled = s.split(' ')
        n = len(shuffled)
        original = [''] * n

        for iword in shuffled:
            original[int(iword[-1]) - 1] += iword[:-1]

        return ' '.join(original)


if __name__ == '__main__':
    s = "is2 sentence4 This1 a3"
    print(Solution().sortSentence(s))
