# Level 1: Basics (1-10)

# 1. Print "Hello, World!"
# 2. Take user input for name and print a greeting.
# 3. Take two numbers as input and print their sum.
# 4. Check if a number is odd or even.
# 5. Print the largest of three numbers.
# 6. Print the multiplication table of a number.
# 7. Calculate the factorial of a number.
# 8. Reverse a string entered by the user.
# 9. Count vowels in a string.
# 10. Create a list of 5 numbers and print sum, max, min.


# 1 ---------------------------------------------------------------------#

# print('hello world')


# 2 ---------------------------------------------------------------------#

# name = input()
# print(f'Hi {name}')


# 3 ---------------------------------------------------------------------#

# a = int(input())
# b = int(input())
# print(f"addition is {a+b}")


# 4 ---------------------------------------------------------------------#

# a = int(input())
# if a % 2 == 0 :
#     print("even")
# elif a % 2 == 1 :
#     print("odd")
# else :
#     print('enter a valid number')

# 5 ---------------------------------------------------------------------#

# a = int(input())
# b = int(input())
# c = int(input())

# def largest_number(a,b,c):
#     if a > b and a > c :
#         return a
#     elif b > a and b > c :
#         return b
#     elif c > a and c > b :
#         return c

# print(f"the largest number is {largest_number(a,b,c)}")


# 6 ---------------------------------------------------------------------#

# num = input(f"enter the numeber for its table : ")

# for i in range(11):
#     print(f'{i} * {num} = {i * int(num)}')


# 7 ---------------------------------------------------------------------#

# num = input('enter the number to get its factorial : ')

# def factorial(a):
#     if a < 0 :
#         print('enter a positive number')
#     elif a == 0 or a==1 :
#         return(1)
#     else :
#         return a * factorial(a-1)

# print(f'the factorial of the number {num} is : {factorial(int(num))}' )


# 8 ---------------------------------------------------------------------#

# str1 = input("enter a stirng : ")
# print(str1[::-1])


# 9 ---------------------------------------------------------------------#

# str1 = input("enter a stirng : ")
# count = 0
# for i in str1:
#     if i in 'aeiouAEIOU':
#         count +=1

# print(f'there are {count} vowels in this string')


# 10 ---------------------------------------------------------------------#

# num = []
# for i in range(5) :
#     num.append(input())

# while True :
#     print('Menu \n 1.Sum \n 2.Max \n 3.Min \n 4.Exit')
#     choice = int(input('enter the choie : '))

#     if choice == 1 :
#         print(f'Sum is : {sum(map(lambda x : int(x), num))}')
#     elif choice == 2 :
#         print(f'Max is : {max(num)}')
#     elif choice == 3 :
#         print(f'Min is : {min(num)}')
#     elif choice == 4:
#         break
#     else:
#         print('enter a valid number')


