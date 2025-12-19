# Level 5: Slightly Advanced (41-50)
# 41. Check if a number is an Armstrong number.
# 42. Check if a number is a perfect number.
# 43. Merge two dictionaries.
# 44. Flatten a nested list
# 45. Find unique elements in a list.
# 46. Sort a dictionary by value.
# 47. Read a file and count the number of lines.
# 48. Read a file and count the frequency of each word.
# 49. Exception handling: divide two numbers safely.
# 50. Use list comprehension to create a list of squares from 1 to 20.


# 41 ---------------------------------------------------------------------#

# num = input("enter a number : ")
# r = len(num)
# temp= 0

# for digit in num:
#     temp += int(digit)**r

# if temp == int(num) :
#     print("is armstrong")
# else:
#     print("is not armstrong")


# 42 ---------------------------------------------------------------------#

# num = int(input("enter a number to check if it is perfect : "))
# sum_of_divisors = 0

# for i in range(1,num):
#     if num % i == 0 :
#         sum_of_divisors += i

# if sum_of_divisors == num :
#     print(f"the given number {num} is perfect.")
# else:
#     print(f"the number is not perfect.")


# 43 ---------------------------------------------------------------------#

# dict1 = {x : x*x for x in range(11)}
# dict2 = {x+5 : x**3 for x in range(11)}

# merged = dict1.copy()
# merged.update(dict2)
# print(merged)


# 44 ---------------------------------------------------------------------#

# nested_list = [[1,2,3,4],['a','b','c','d']]

# def flatten_list(nested_list):
#     flat=[]
#     for i in nested_list :
#         if isinstance(i, list):
#             flat.extend(flatten_list(i))
#         else:
#             flat.append(i)
#     return flat


# print(f"flattened list is {flatten_list(nested_list)}")

# 45 ---------------------------------------------------------------------#

# list1 =  [1,2,3,3,4,4,'a','b','c','d','d']
# list2 = set(list1)
# print(list2)


# 46 ---------------------------------------------------------------------#

# dict1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 5, 'e' : 4}
# flat1 = []
# for i in dict1.values():
#     flat1.append(i)
# flat1.sort()
# print(flat1)


# 47 ---------------------------------------------------------------------#

# file1 = open("file1.txt",'r')
# read_file1 = file1.readlines()
# print(len(read_file1))
# file1.close()

# 48 ---------------------------------------------------------------------#

# file1 = open("file1.txt",'r')
# read_file1 = file1.read()
# words = read_file1.split()

# word_counts = {}

# for word in words:
#     word = word.lower()
#     word_counts[word] = word_counts.get(word,0)+1

# print(word_counts)


# 49 ---------------------------------------------------------------------#

# num1 = int(input("enter a number : "))
# num2 = int(input("enter a number : "))
# ans = 0
# try:
#     ans = num1/num2
#     print(ans)
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e :
#     print(e)


# 50 ---------------------------------------------------------------------#

# print([x**2 for x in range(1,21)])
