class Solution:
    def get_num_repr(self, word):
        codes = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
        s = ''
        for l in word:
            s = s + codes[l]
        return int(s)

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.get_num_repr(firstWord) + self.get_num_repr(secondWord) == self.get_num_repr(targetWord)


if __name__ == '__main__':
    test_cases = [['acb', 'cba', 'cdb', True]]
    for test_case in test_cases:
        assert Solution().isSumEqual(*test_case[:3]) == test_case[3]

