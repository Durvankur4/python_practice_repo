Extract a part (subset) of a sequence like a **list, tuple, or string**.
```
sliced = sequence[start:stop:step]
```

important use cases
```
numbers = [0, 1, 2, 3, 4, 5, 6]

print(numbers[2:5])    # [2, 3, 4] -> index 2 to 4
print(numbers[:4])     # [0, 1, 2, 3] -> start to index 3
print(numbers[3:])     # [3, 4, 5, 6] -> index 3 to end
print(numbers[::2])    # [0, 2, 4, 6] -> every 2nd element
print(numbers[::-1])   # [6, 5, 4, 3, 2, 1, 0] -> reversed

```

used most in list tuples and strings [[Datatypes]]
