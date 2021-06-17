class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:

        new_s = [''] * len(s)

        for i, ind in enumerate(indices):
            new_s[ind] = s[i]

        return ''.join(new_s)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    print(Solution().restoreString(s, indices))
