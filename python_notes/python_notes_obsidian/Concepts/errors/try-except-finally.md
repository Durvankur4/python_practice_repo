`finally` block **always runs**, whether error occurs or not.  
Useful for cleanup (closing files, releasing resources, etc.).
```
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file (if it was opened).")

---

File not found.
Closing file (if it was opened).

```

