If you have a [[list and tuples]], `*` will unpack it into separate positional arguments.

```
def add(a, b, c):
    return a + b + c

numbers = [2, 4, 6]

print(add(*numbers))   # same as add(2, 4, 6)

```

If you have a [[dict()]], `**` will unpack it into keyword arguments.

```
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, from {city}.")

person = {"name": "Alice", "age": 21, "city": "Pune"}

introduce(**person)  # same as introduce(name="Alice", age=21, city="Pune")

-----

My name is Alice, I am 21 years old, from Pune.

```

Combining both (order matters)

```
def demo(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, 4, 5, x=10, y=20)

-----

a: 1
b: 2
args: (3, 4, 5)
kwargs: {'x': 10, 'y': 20}

```

