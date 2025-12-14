usually program stops completely when error occurs so these are used so your program doesn’t crash when an exception occurs.

```
BASIC STRUCTURE

try:
    # code that may cause an error
except SomeError:
    # code to run if that error happens
finally:
    # code that always runs (cleanup)


```


[[try-except]]
[[try-except-finally]]