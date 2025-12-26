# Quesiton:
# 1700. Number of Students Unable to Eat Lunch


# Solution:

from collections import Counter


def countstudents(students: list[int], sandwiches: list[int]) -> int:
    counter = Counter(students)
    resu = len(students)
    for s in sandwiches:
        if counter[s]:
            counter[s] -= 1
            resu -= 1
        else:
            return resu
    return resu


# time complexity = O(n)
# space complexity = O(n)
