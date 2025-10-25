# Level 4: Lists & Dictionaries (31–40)
# 31. Find the second largest number in a list.
# 32. Merge two lists and remove duplicates.
# 33. Sort a list in ascending and descending order.
# 34. Count occurrences of each element in a list.
# 35. Find common elements between two lists.
# 36. Sum all values in a dictionary.
# 37. Count number of keys in a dictionary.
# 38. Create a dictionary from two lists (keys & values).
# 39. Reverse keys and values in a dictionary.
# 40. Find the key with the maximum value in a dictionary.



# 31 ---------------------------------------------------------------------#

# list_1 = [1,2,4,5,9,7,10,7,9.5,8]
# largest = float()
# second_largest= float()
# for i in list_1:
#     if i > largest :
#         second_largest = largest 
#         largest = i 
#     elif i > second_largest and i != largest:
#         second_largest = i

# print(second_largest)



# 32 ---------------------------------------------------------------------#

# list_1 = [1,2,4,5,9,7,10,7,9.5,8]
# list_2 = [1,2,4,5,6,4,0,7,9.5,11,8]

# # list_3 = list_1 + list_2
# # print(set(list_3))

# list_3 = list(sorted(set(list_1+list_2)))
# print(list_3)



# 33 ---------------------------------------------------------------------#

# list_1 = [1,2,4,5,6,4,0,7,9.5,11,8]
# list_1.sort()
# print(list_1)



# 34 ---------------------------------------------------------------------#
# from collections import Counter
# list_1 = [123,23,4,53,2,4,2,1,456,74,2,1,1,123,8,9]

# # count_dict = {}
# # for i in list_1:
# #     if i in count_dict:
# #         count_dict[i] += 1
# #     else:
# #         count_dict[i]=1

# # print(count_dict)

# print(Counter(list_1))