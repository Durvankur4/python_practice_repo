# Problem 1 (Easy) — Custom sum function with *args
# Write a function my_sum(*args) that takes unlimited numbers and returns their sum.
# Ignore non-numeric values.
# Topics required
# *args usage
# isinstance(x, (int, float))
# Simple iteration

def my_sum(*numbers):
    sum = 0
    for num in numbers:
        if isinstance(num , (int,float)):
            sum += num
    # print(numbers)
    return sum

print(my_sum(1,2,3,"abc"))