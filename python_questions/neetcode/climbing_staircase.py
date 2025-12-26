# Quesiton:
# Climbing Stairs
# Solved
# You are given an integer n representing the number of steps to reach the top of a
# staircase. You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase

# Solution:
class Solution:
    def climb_stairs(self, n: int) -> int:
        one = 1
        two = 1
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


# time complexity = O(n)
# space complexity = O(n)
