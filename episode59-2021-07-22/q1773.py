from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        if ruleKey == 'type':
            index = 0
        elif ruleKey == 'color':
            index = 1
        else:
            index = 2

        counter = 0
        for item in items:
            if item[index] == ruleValue:
                counter += 1
        return counter


if __name__ == '__main__':
    items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"
    print(Solution().countMatches(items, ruleKey, ruleValue))
