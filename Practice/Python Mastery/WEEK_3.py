# <!-- Write a function dedupe(items) that returns a list with duplicates removed, but keeps the original order of first appearance.
# Example:
# [1, 2, 1, 3, 2, 4] → [1, 2, 3, 4]
# Topics required
# Sets
# List iteration
# Membership test O(1) intuition -->


# def dedupe(items : list) -> list :
#   seen = set()
#   out = []
#   for item in items:
#     if item in seen :
#       continue
#     seen.add(item)
#     out.append(item)
#   return out
  
# print(dedupe([1, 2, 1, 3, 2, 4, 5]))




# <!-- Problem 2 (Medium) — Merge list of dicts by a key
# Given a list of dicts, merge them based on a shared field "id".
# Examle input:
# [
#     {"id": 10, "name": "Alice"},
#     {"id": 10, "score": 89},
#     {"id": 12, "name": "Bob"},
#     {"id": 12, "score": 95}
# ]
# Output:
# {
#   10: {"id": 10, "name": "Alice", "score": 89},
#   12: {"id": 12, "name": "Bob", "score": 95}
# }
# Topics required
# Dicts as maps
# Understanding reference semantics (merging two dicts)
# .setdefault() or dict merging (| operator in Python 3.9+)
# Iterating a list of dicts -->



# <!-- Problem 3 (Hard) — Top-k most frequent elements
# Given a list of items, return the k most frequent ones in descending order of frequency.
# Example:
# items = [1,1,1,2,2,3], k=2 → [1,2]
# Topics required (IMPORTANT)
# These are core CS concepts you must understand before attempting:
# Hash maps (Python dict + Counter)
# Heap / priority queue (module: heapq)
# Time complexity (O(n) counting + O(n log k) heap operations)
# Tuples used for ordering (e.g., (count, value))
# This problem is foundational for interviews and high-performance Python -->