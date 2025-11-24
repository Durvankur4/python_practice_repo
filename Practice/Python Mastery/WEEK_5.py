# Problem 1 (Easy) — Count lines in a file
# Write a function count_lines(path) that returns how many lines are in a file.
# Topics required
# with open(...) as f:
# Iteration over file objects
# File modes (“r”)

# def count_lines(path:str):
#     count = 0
#     with open(path , "r") as f :
#         for _ in f :
#             count += 1
#     return count

# print(count_lines('Practice\Python Mastery\WEEK_4.py'))


# Problem 2 (Medium) — Build a tiny module
# Create two files:
# mathutils.py
# def square(n):
#     return n*n
# def cube(n):
#     return n*n*n
# main.py
# import mathutils
# print(mathutils.square(5))
# print(mathutils.cube(3))
# Your task:
# Write a function run_math(path) that automatically imports the module from the given path and runs both functions.
# Topics required
# Modules
# importlib
# Attribute access via getattr

import mathutils
print(mathutils.square(5))
print(mathutils.cube(3))

### too complex for my understanding currently redo

