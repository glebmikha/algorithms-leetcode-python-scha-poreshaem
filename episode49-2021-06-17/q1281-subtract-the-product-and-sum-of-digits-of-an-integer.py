class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)

        product = 1
        summ = 0
        for num in n_str:
            product = product * int(num)
            summ = summ + int(num)

        return product - summ


class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        product = 1
        summ = 0
        mult = 0
        while n // 10**mult:
            digit = (n % 10**(mult+1)) // 10**mult
            product = product * digit
            summ = summ + digit
            mult = mult + 1

        return product - summ



if __name__ == '__main__':
    n = 234
    print(Solution().subtractProductAndSum(n))