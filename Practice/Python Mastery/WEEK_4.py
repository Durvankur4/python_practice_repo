# Problem 1 (Easy) — Custom sum function with *args
# Write a function my_sum(*args) that takes unlimited numbers and returns their sum.
# Ignore non-numeric values.
# Topics required
# *args usage
# isinstance(x, (int, float))
# Simple iteration

# def my_sum(*numbers):
#     sum = 0
#     for num in numbers:
#         if isinstance(num , (int,float)): 
#             sum += num
#     # print(numbers) 
#     return sum

# print(my_sum(1,2,3,"abc"))



# Problem 2 (Medium) — Function factory using closures
# Write make_counter(start=0) that returns a function.
# Each time you call the returned function, it increases the counter by 1 and returns it.
# Example:
# c = make_counter(10)
# c() → 11  
# c() → 12
# Topics required
# Closures
# Nonlocal variables
# Function returning a function
# Step-by-step
# Define outer function accepting start.
# Inside, define inner function that modifies start.
# Use nonlocal so inner function updates outer variable.
# Return inner function.


# def make_counter(start=0) :
#     count = start
#     def inner():
#         nonlocal count
#         count += 1 
#         return count
#     return inner

# c = make_counter(10)

# assert c() == 11
# assert c() == 12