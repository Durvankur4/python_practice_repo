# Level 3: Functions & Strings (21–30)
# 21. Write a function to check if a number is prime.
# 22. Write a function to calculate factorial.
# 23. Write a function to find GCD of two numbers.
# 24. Write a function to convert Celsius to Fahrenheit.
# 25. Check if a string is a palindrome.
# 26. Count words in a string.
# 27. Remove vowels from a string.
# 28. Capitalize the first letter of each word in a string.
# 29. Replace spaces in a string with underscores.
# 30. Find the most frequent character in a string.



# 21 ---------------------------------------------------------------------#

# def is_prime(num):
#     if num > 1 :
#         for i in range(2,num):
#             if (num % i)==0:
#                 print('the number is not prime.')
#                 break
#         else :
#             print('number is prime.')
#     else:
#         print('the number is not prime.')

# number = int(input("enter the numebr to check for prime : "))
# is_prime(number)



# 22 ---------------------------------------------------------------------#

# def clac_fact(num):
#         if num < 0 :
#               print('enter a valoid number.')
#         elif num == 0 or num == 1: 
#             return(1)
#         else :
#             return num * clac_fact(num-1)
    
# number = int(input("enter the numebr to check factorial : "))
# print(clac_fact(number))



# 23 ---------------------------------------------------------------------#

#solved using euclidian algorithm
# num1 = int(input("enter 1st numebr : "))
# num2 = int(input("enter 2nd numebr : "))

# def calc_gcd(a,b):
#     if b == 0 :
#         return a 
#     else :
#         return calc_gcd(b,a%b)

# print(f"GCD is : {calc_gcd(num1,num2)}")



# 24 ---------------------------------------------------------------------#

# def convert_temperatures(value,degree):
#     ans = 0 
#     if degree in ("C","c") :
#         ans = (value * 9/5) + 32 
#         print(f"the converted value is {ans} degree Farenheit")
    
#     elif degree in ("f","F") :
#         ans = (value - 32) * 5/9
#         print(f"the converted value is {ans} degree Celsius")
#     else:
#         print("enter valid input.") 

# temperature_value = int(input("enter value : "))
# temperature_degree = input("enter Celsius or Farenheit (C/F) : ")


# convert_temperatures(temperature_value,temperature_degree)



# 25 ---------------------------------------------------------------------#

# word = input('enter a word to check for palindrome : ')
# word = word.lower()

# if word == word[::-1]:
#     print('its a palindorme')
# else:
#     print('not a palindrome')



# 26 ---------------------------------------------------------------------#

# sentence = input('enter a sentence to count no of letters : ')
# word_array = sentence.split()
# # count = 0
# print(len(word_array))

# # for i in word_array :
# #     count += len(i)
# # print(f'there are {count} letters')



# 27 ---------------------------------------------------------------------#

# sentence = input('enter a sentence to count no of letters : ')
# collector = [] 
# for i in sentence:
#    if i not in ["a","A","e","E","i","I","o","O","u","U"] :
#       collector.append(i)

# print(collector)
# ---------------------------
# sentence = input("enter a sentence to remove vowels : ")
# vowels = 'aeiouAEIOU'
# result_sentence = ''

# for char in sentence :
#     if char not in vowels :
#         result_sentence += char

# print(result_sentence)



# 28 ---------------------------------------------------------------------#

# sentence = input("enter a sentence : ")
# print(sentence.lower().title())

