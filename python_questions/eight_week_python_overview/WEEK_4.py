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



# Problem 3 (Hard) — Memoization decorator
# Write a decorator @memoize that caches results of a function for each set of arguments.
# Example:
# @memoize
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# Calling fib(35) should run instantly after caching.
# Topics required (IMPORTANT)
# You must know these:
# Decorators (function wrapping another function)
# Closures
# functools.wraps to preserve metadata
# Dicts as caches (cache[(args, frozenset(kwargs))] = result)
# Tuples as hashable keys
# If any of these feel unfamiliar, pause and review before solving.
# 0 1 1 2 3 5 8 13 21 

# def memoization(func) :
#     cache = {}
#     def wrapper(*args,**kwargs):
#         key = (args, tuple(sorted(kwargs.items())))
#         if key in cache :
#             return cache[key]
#         else:
#             result = func(*args,**kwargs)
#             cache[key] = result
#         return result         

#     return wrapper

# @memoization
# def fibonacci(n):
#     if not isinstance(n, int):
#         raise TypeError("n must be an integer")

#     if n < 0:
#         raise ValueError("n must be non-negative")

#     if n < 2:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(55))
