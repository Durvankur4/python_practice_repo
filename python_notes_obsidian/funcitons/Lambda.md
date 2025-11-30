small, anonymous [[Functions]] defined without a name. It is often used when you need a simple function for a short period of time.
Lambda functions can only have **one expression**, no statements

```
lambda arguments: expression

square = lambda x: x ** 2
print(square(4))  # Output: 16
```

often use with [[map()]] and [[filter()]]