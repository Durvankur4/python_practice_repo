# Problem 1 (Easy) — Count lines in a file
# Write a function count_lines(path) that returns how many lines are in a file.
# Topics required
# with open(...) as f:
# Iteration over file objects
# File modes (“r”)

def count_lines(path:str):
    count = 0
    with open(path , "r") as f :
        for _ in f :
            count += 1
    return count

print(count_lines('Practice\Python Mastery\WEEK_4.py'))