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

# def find_max(window : list[int]) -> int:
#     max_num = max(window)
#     return max_num

# #code works but is not optimal
# def find_max_window(list : list[int], k : int) -> list[int] :

#     # list which is to be passed
#     # k is the window sizze

#     result = []
#     window_stack = list[:k]
#     result.append(find_max(window_stack))

#     for i in range(k,len(list)):
#         window_stack.append(list[i])
#         window_stack.remove(list[i-k])
#         max = find_max(window_stack)
#         result.append(max)

#     print(result)
#     return


# find_max_window([1,3,-1,-3,5,3,6,7],3)


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


# Problem 3 O(n) using deque :

# from collections import deque

# def find_max_window(arr : list[int], k : int) -> list[int]:
#     if not isinstance(arr, list): #if arr is a list
#         print("enter a list!")
#     if not isinstance(k,int): # if k is a int
#         print("Enter a int window size!")

#     len_arr = len(arr)

#     if k <=0 or len_arr<=0 or k>len_arr: # null error check
#         print("enter some data!")

#     dq = deque();
#     result : list[int] = []

#     for i,val in enumerate(arr):
#         while dq and dq[0] <= i-k:
#             dq.popleft()

#         while dq and arr[dq[-1]] <= val:
#             dq.pop()

#         dq.append(i)
#         if i >= k-1 :
#             result.append(arr[dq[0]])

#     return result

# print(find_max_window([1,3,-1,-3,5,3,6,7],3))


# # resolution
# from collections import deque
# def sliding_window(array : list[int], k = int) -> list[int] :
#     array_len = len(array)
#     dq = deque()
#     result : list[int] = []

#     if isinstance(array,list):
#         print("Enter a list of int")
#     if isinstance(k , int):
#         print("Enter int in second argument")
#     if k<0 or array_len<0 or k>array_len:
#         print("Error in Values")

#     for i,val in enumerate(array):

#         while dq and dq[0] <= i-k:
#             dq.popleft()

#         while dq and array[dq[-1]]<= val :
#             dq.pop()

#         dq.append(i)
#         if i >= k-1:
#             result.append(array[dq[0]])
#     return result
# print(sliding_window([1,3,-1,-3,5,3,6,7],3))

# Clean Code Challenge (refactor)
# Refactor the messy function below to be readable, efficient, and PEP-8 compliant. Provide the refactored code and a short note on what you changed.

# def do(stuff):
#   a = {}
#   for i in range(0,len(stuff)):
#     item = stuff[i]
#     if item != None:
#       name = item.get('n')
#       if name:
#         if name in a:
#           a[name] = a[name] + 1
#         else:
#           a[name] = 1
#   return a


# items = [
#     {"n": "alice"},
#     {"n": "bob"},
#     {"n": "alice"},    # repeat
#     {"x": 123},        # missing 'n'
#     {"n": ""},         # empty name
#     None,              # ignored
#     {},                # empty mapping
#     {"n": "charlie"},
#     {"n": None},       # explicitly None
#     {"n": "bob"},      # repeat
# ]

# def count_names(dict : dict[str,str]):
#     a = {}

#     for i in range(0,len(dict)):
#         item = dict[i]
#         if item != None :
#             name = item.get('n')
#             if name in a :
#                 a[name] += 1
#             else :
#                 a[name] = 1

#     return a


