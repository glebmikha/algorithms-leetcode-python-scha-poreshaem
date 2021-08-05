from typing import List
from collections import OrderedDict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = sorted(list(set(groupSizes)))

        group_dict = OrderedDict()
        for group in groups:
            if group in group_dict:
                pass
            else:
                group_dict[group] = []

        for i, gs in enumerate(groupSizes):
            group_dict[gs].append(i)

        list_of_groups = []
        for gs, elements in group_dict.items():
            n = len(elements)
            l = []
            i = 0
            while i < n:
                if len(l) < gs:
                    l.append(elements[i])
                else:
                    list_of_groups.append(l)
                    i = i - 1
                    l = []
                i = i + 1

            list_of_groups.append(l)

        return list_of_groups


if __name__ == '__main__':
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(Solution().groupThePeople(groupSizes))
