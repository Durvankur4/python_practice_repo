# ---

# ### **1️⃣ Two Sum**

# **Problem:**
# Given an array of integers `nums` and an integer `target`, return *indices* of the two numbers such that they add up to the target.
# Assume each input has exactly one solution, and you may not use the same element twice.

# **Example:**

# ```
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# ```

# ---


# def funtion(list1,target):
#     result=[]
#     for i in range(len(list1)):
#         for j in range(i+1,len(list1)):
#             if list1[i]+list1[j] == target :
#                 result.append(char)
#                 result.append(j)
#     return result

# print(funtion([2,7,11,15],13))


# ### **2️⃣ Palindrome Number**

# **Problem:**
# Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.
# (A palindrome reads the same backward as forward.)

# **Example:**

# ```
# Input: x = 121
# Output: True
# ```

# ---

# user_inp = 121
# def check_palindrome(inp):
#     inpS = str(inp)
#     if inpS == inpS[::-1]:
#         return True
#     else:
#         return False
# print(check_palindrome(user_inp))


# ### **3️⃣ Valid Parentheses**

# **Problem:**
# Given a string `s` containing just the characters `'(', ')', '{', '}', '[' , ']'`, determine if the input string is valid.
# A string is valid if:

# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.

# **Example:**

# ```
# Input: s = "()[]{}"
# Output: True
# ```

# ---
# def paranthesis_check(string):

#         stack = []
#         for char in string :
#             if char in '({[':
#                 stack.append(char)


#             elif char in '}])':
#                 if not stack :
#                      print('not in order')
#                 elif stack[-1]== '(' and char == ')':
#                     stack.pop()
#                 elif stack[-1]== '[' and char == ']':
#                     stack.pop()
#                 elif stack[-1]== '{' and char == '}':
#                     stack.pop()
#                 else :
#                     print('this does not follow order')
#                     return

#             else:
#                  print('inorder')

#         if stack != 0 :
#              print('more opening brackets')
#         else :
#              print('done')

# paranthesis_check('{}[](){')
# paranthesis_check('{}[](})')
# paranthesis_check('{}[]()')


# ### **4️⃣ Remove Duplicates from Sorted Array**

# **Problem:**
# Given a sorted array `nums`, remove the duplicates **in-place** such that each unique element appears only once.
# Return the number of unique elements.

# **Example:**

# ```
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# ```


# nums = [1,2,3,4,4,5,6,7,7,7,8,9]

# def rem_duplicates(arr):
#     if not arr:
#         return False

#     i = 0
#     for j in range(len(arr)):
#         if arr[j] != arr[i]:
#             i+=1
#             arr[i]=arr[j]

#     return i

# print(rem_duplicates(nums))


# ---

# ### **5️⃣ Plus One**

# **Problem:**
# You are given a large integer represented as an integer array `digits`, where each `digits[i]` is a single digit.
# Add one to the integer and return the resulting array.

# **Example:**

# ```
# Input: digits = [1,2,3]
# Output: [2,3,4]
# ```

# ---

# Would you like me to include the **Python solutions** for these 5 next?

# nums = [1,2,3,4,4,5,6,7,7,7,8,9]
# lsitaddOne = list(map(lambda x : x+1 ,nums))
# print(lsitaddOne)


# bonus
# count vowels in a string

str1 = input("enter a string")
count = 0
for i in str1.lower():
    if i in "aeiou":
        count += 1
print(count)
