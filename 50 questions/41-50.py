# Level 5: Slightly Advanced (41–50)
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



# 48 ---------------------------------------------------------------------#



# 49 ---------------------------------------------------------------------#



# 50 ---------------------------------------------------------------------#


# 41:
#     title: "Check if a number is an Armstrong number"
#     description: "Take an integer input, find the sum of each digit raised to the power of the number of digits, and check if that sum equals the original number."
#   42:
#     title: "Check if a number is a perfect number"
#     description: "Find all divisors of a given number (excluding the number itself), add them up, and check if the total equals the number."
#   43:
#     title: "Merge two dictionaries"
#     description: "Combine two separate dictionaries into one, so that all their key–value pairs are stored together in a single dictionary."
#   44:
#     title: "Flatten a nested list"
#     description: "Convert a list that contains other lists (like [[1,2],[3,4]]) into one single list containing all the individual numbers ([1,2,3,4])."
#   45:
#     title: "Find unique elements in a list"
#     description: "From a list that may have duplicate values, create a new list that contains each distinct element only once."
#   46:
#     title: "Sort a dictionary by value"
#     description: "Rearrange the items of a dictionary in order (ascending or descending) based on their values, not their keys."
#   47:
#     title: "Read a file and count the number of lines"
#     description: "Open a text file, read all its contents, and count how many separate lines (rows) it contains."
#   48:
#     title: "Read a file and count the frequency of each word"
#     description: "Read a text file, split the text into individual words, and count how many times each unique word appears."
#   49:
#     title: "Exception handling: divide two numbers safely"
#     description: "Write a program that asks the user for two numbers, divides them, and properly handles errors like dividing by zero or entering non-numeric input."
#   50:
#     title: "Use list comprehension to create a list of squares from 1 to 20"
#     description: "Use a one-line list comprehension to generate a list where each element is the square of numbers from 1 to 20."