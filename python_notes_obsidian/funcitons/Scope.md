the region of the code where a variable is recognized.

Python has LEGB rules [[Functions]]

L – Local → inside the current function.
E – Enclosing → in outer functions (if functions are nested).
G – Global → variables defined at the top level of a script/module.
B – Built-in → Python’s built-in names (len, range, etc.).

```
x = 10  # Global

def outer():
    y = 20  # Enclosing
    
    def inner():
        z = 30  # Local
        print(x, y, z)  # Access all
    inner()

outer()

```
