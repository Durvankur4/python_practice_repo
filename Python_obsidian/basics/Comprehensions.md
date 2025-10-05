nothing just rules to describe a data collection [[Datatypes]]
```
# List comprehension
squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Set comprehension
unique = {x % 3 for x in range(10)}
print(unique)  # {0, 1, 2}

# Dict comprehension
mapping = {x: x**2 for x in range(5)}
print(mapping)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

```
