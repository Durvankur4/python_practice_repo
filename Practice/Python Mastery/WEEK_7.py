# Problem 1 (Easy) — Safe integer conversion
# Write safe_int(s) that:
# Converts s to int
# Returns None if conversion fails
# Does not use s.isdigit()
# Topics Require
# try/except
# returning None as a failure signal

# def safe_int(s ):
#     try :
#         return int(s)
#     except (ValueError,TypeError):
#         return None
# print(safe_int("123"))


# Problem 2 (Medium) — Filtering + dict comprehension
# Input:
# scores = {
#     "alice": 92,
#     "bob": 75,
#     "carol": 99,
#     "dave": 61
# }
# Create a function top_scores(scores, threshold) that returns a new dict with only entries above threshold, in lowercase keys
# Expected:
# top_scores(scores, 80)
# → {"alice": 92, "carol": 99}
# Topics Required
# dict comprehensions
# predicate filtering
# type hints

# scores = {
#     "alice": 92,
#     "bob": 75,
#     "carol": 99,
#     "dave": 61
# }

# def top_scores(scores, threshold) :
#     top = {k.lower():v  for k ,v in scores.items() if scores[k]>threshold}
#     return top

# print(top_scores(scores,80))


# Write a generator primes() that yields prime numbers forever:
# g = primes()
# next(g) → 2  
# next(g) → 3  
# next(g) → 5  
# ...
# Topics Required (IMPORTANT)
# Before attempting, make sure you know:
# Generator functions (yield)
# Lazy stateful iteration
# Writing a helper function for primality
# Time complexity implications
# Infinite loops inside generators
# Clean exit (users decide when to stop)

# def isPrime(n : int ) -> bool :
#     if n <2 :
#         return False
#     if n == 2 :
#         return True
#     if n%2 == 0 :
#         return False
    
#     i = 3
#     while i * i <= n :
#         if n%i == 0:
#             return False
#         i +=2 
#     return True

# def primes():
#     n = 2 
#     while True:
#         if isPrime(n) :
#             yield n 
#         n+=1

# g = primes()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
