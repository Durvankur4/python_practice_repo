# Problem 1 (Easy) — FizzBuzz variant
# Write a function fizz_buzz(n) that returns a list of strings for numbers 1..n:
# multiples of 3 → "Fizz"
# multiples of 5 → "Buzz"
# multiples of both → "FizzBuzz"
# otherwise → string of the number

# Solution (step-by-step)
# Validate n is positive integer (simple guard).
# Iterate for i in range(1, n+1).
# Use condition order: check multiples of both first (or use concatenation).
# Append result to list and return.

# def fizz_buzz(n):
#     if n <=0 :
#         return []
#     out = []
#     for i in range(1,n+1):
#         if i % 15 == 0:
#             out.append("FizzBuzz")
#         elif i % 5 == 0 :
#             out.append("Buzz")
#         elif i % 3 == 0 :
#             out.append("Fizz")
#         else :
#             out.append(str(i))
#     return out

# print(fizz_buzz(20))



# Problem 2 (Medium) — Count words with filter
# Given a list of strings, return a dict mapping words → count, but:
# normalize to lowercase
# skip empty strings and words shorter than 3 chars
# treat punctuation .,!?;: as separators (strip them)
# Example: ["Hi!", "hello", "Hello", "ok", "well-done."] → {'hello': 2, 'well-done':1}

# def count_string(words : list[str]) -> dict[str,int]:
#     PUNCT = ".,!?;:"
#     count_dict = {}
#     for i in words :
#         if not i:
#             continue
#         if len(i) <= 3:
#             continue
#         i = i.strip(PUNCT).lower()
    
#         if i in count_dict:
#             count_dict[i]+=1 
#         else:
#             count_dict[i] =1
        
#     return count_dict

# print(count_string(["HEllo","hi","hello","WTF.",'wtf?']))


# Problem 3 (Hard) — Sliding window max (control-flow + algorithm)
# Given a list of integers and a window size k, return a list of maximums for each contiguous window of length k.
# Example: [1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7].
# Step-by-step approach
# We want O(n). Use a deque storing indices of elements in decreasing value order:
# Iterate indices i from 0 to n-1.
# Pop left elements if they are out of window (i - deque[0] >= k).
# Pop right elements while current element >= element at deque[-1] to keep deque decreasing.
# Append current index.
# Starting at i >= k-1, record nums[deque[0]] as window max.

def find_max(window : list[int]) -> int:
    max_num = max(list)
    return max_num

def find_max_window(list : list[int], k : int) -> list[int] :
    result = []
    window_stack = list[:k]
    result.append(window_stack)
    for i in range(k,len(list)):
        print(i)
        window_stack = list[i] - list[i-k]
        
        max = find_max(window_stack)
        result.append(max)

    print(result)
    return

find_max_window([1,3,-1,-3,5,3,6,7])


# Example
# Find the maximum sum of any 3 consecutive numbers in a list.
# nums = [2, 1, 5, 1, 3, 2]
# k = 3






















# def some_function(nums : list[int], k : int)-> int :
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k,len(nums)):
#         window_sum += nums[i] - nums[i-k]
#         max_sum = max(window_sum,max_sum)

#     return max_sum

# print(some_function([2, 1, 5, 1, 3, 2],3))