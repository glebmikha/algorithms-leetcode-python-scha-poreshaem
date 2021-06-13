class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = {}
        for stone in stones:
            if stone in stone_dict:
                stone_dict[stone] += 1
            else:
                stone_dict[stone] = 1

        jewel_number = 0
        jewels = set(jewels)

        for stone, count in stone_dict.items():
            if stone in jewels:  # O(1)
                jewel_number = jewel_number + count

        return jewel_number


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))
