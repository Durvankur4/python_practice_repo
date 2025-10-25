A dictionary is a collection of key-value pairs.
Each key is unique.
Values can be any data type.
Dictionaries are unordered in Python

creating 
```
# Using curly braces
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)
# {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Using dict() function
student2 = dict(name="Bob", age=22, grade="B")
print(student2)
# {'name': 'Bob', 'age': 22, 'grade': 'B'}

# Empty dictionary
empty = {}
print(empty)  # {}

```

looping in a dict()
```
student = {"name": "Alice", "age": 20, "grade": "A"}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Both key and value
for key, value in student.items():
    print(key, ":", value)

```

![[Pasted image 20251025210451.png]]