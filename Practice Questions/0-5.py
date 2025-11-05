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

list_inp = list(input('enter a lsiit of numbers :'))

def funtion(list1,target):
    result=[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j] == target :
                result.append(i)
                result.append(j)
    return result

print(funtion(list_inp))






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












# ### **4️⃣ Remove Duplicates from Sorted Array**

# **Problem:**
# Given a sorted array `nums`, remove the duplicates **in-place** such that each unique element appears only once.
# Return the number of unique elements.

# **Example:**

# ```
# Input: nums = [1,1,2]  
# Output: 2, nums = [1,2,_]
# ```












# ---

# ### **5️⃣ Plus One**

# **Problem:**
# You are given a large integer represented as an integer array `digits`, where each `digits[i]` is a single digit.
# Add one to the integer and return the resulting array.

# **Example:**

# ```
# Input: digits = [1,2,3]  
# Output: [1,2,4]
# ```

# ---

# Would you like me to include the **Python solutions** for these 5 next?
