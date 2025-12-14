they are used when you don’t know beforehand how many arguments you’ll pass to a function.
stored in [[list and tuples]] and [[dict()]] respectively

```
*args

Collects extra positional arguments into a tuple.

def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))        # 6
print(add_all(5, 10, 15, 20))  # 50

here args is a tupple
(1, 2, 3)
(5, 10, 15, 20)

```

```
**kwargs

Collects extra named arguments into a dictionary.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=21, city="Pune")

name: Alice
age: 21
city: Pune
 
here keywords are in dict 
{'name': 'Alice', 'age': 21, 'city': 'Pune'}
 
```