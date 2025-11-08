# Write a function fizz_buzz(n) that returns a list of strings for numbers 1..n:
# multiples of 3 → "Fizz"
# multiples of 5 → "Buzz"
# multiples of both → "FizzBuzz"
# otherwise → string of the number

def fizz_buzz(n):
    if n <=0 :
        return []
    out = []
    for i in range(1,n+1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 5 == 0 :
            out.append("Buzz")
        elif i % 3 == 0 :
            out.append("Fizz")
        else :
            out.append(str(i))
    return out

print(fizz_buzz(20))