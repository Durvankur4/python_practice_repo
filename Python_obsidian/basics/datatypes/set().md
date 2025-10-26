useful datatype allows faster search and delete operation since no indexing is present
unordered and unique elements
```
# From a list
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}

# Using curly braces (set literal {} )
fruits = {"apple", "banana", "cherry"}
print(fruits)  # {'apple', 'banana', 'cherry'}

# Empty set
empty = set() # correct
empty2 = {}  # wrong
print(empty)  # type set() 
print(empty2)  # type dict()

```

![[Pasted image 20251026221802.png]]