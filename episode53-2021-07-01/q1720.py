class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        decoded = [first]
        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[i])
        return decoded


if __name__ == '__main__':
    encoded = [6, 2, 7, 3]
    first = 4
    print(Solution().decode(encoded, first))
