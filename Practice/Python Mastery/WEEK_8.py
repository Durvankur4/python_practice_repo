# Problem 1 (Easy) — Timing Two Approaches
# Compare these:
# Using a list comprehension
# Using map
# Task:
# Generate squares of numbers 0–999999 and measure both.
# Topics Required
# timeit
# list comprehension
# simple map usage

# import timeit
# # using list comprehensions
# def squares():
#     return [n**2  for n in range(0,1000000)]
# # print(squares())

# #using mapping comprehensions
# def squares2():
#     return {x : x **2 for x in range(0,1000000)}
# # print(squares2())

# #timing code 
# results = timeit.timeit(stmt="squares2()",setup="from __main__ import squares2",number=5)
# print(results)
# results = timeit.timeit(stmt="squares()",setup="from __main__ import squares",number=5)
# print(results)

# Problem 2 (Medium) — Optimize an O(n²) operation
# Given a list of numbers, return all pairs (a, b) where a + b == target.
# A naive version:
# def pairs(nums, target):
#     result = []
#     for i in nums:
#         for j in nums:
#             if i + j == target:
#                 result.append((i, j))
#     return result
# Tasks
# Explain the complexity.
# Rewrite it in O(n).
# Compare timing using timeit.
# Topics Required
# Hash sets
# Time complexity
# Eliminating repeated work
# Optimized solution
import timeit 

def pairs(nums, target):
    result = []
    for i in nums:
        for j in nums:
            if i + j == target:
                result.append((i, j))
    return result

print(timeit.timeit(stmt="pairs([x for x in range(1000)],50)",setup="from __main__ import pairs",number=1))


def opt_pairs(nums,target):
    seen =set()
    out = []
    for n in nums:
        comp = target - n 
        if comp in seen:
            out.append((n,comp))
        seen.add(n)
    return out

print(timeit.timeit(stmt="opt_pairs([x for x in range(1000)],50)",number=100,setup="from __main__ import opt_pairs"))


