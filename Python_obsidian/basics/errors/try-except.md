single error handling
```
try:
    num = int("abc")   # this will cause ValueError
except ValueError:
    print("Conversion failed! Not a number.")

---

Conversion failed! Not a number.

```

multiple error handling 
```
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid value")

---

You cannot divide by zero!
```
