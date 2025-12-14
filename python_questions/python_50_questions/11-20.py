# Level 2: Loops & Conditionals (11–20)
# 11. Print numbers from 1 to 50 using a loop.
# 12. Print all even numbers between 1 and 100.
# 13. Sum of all numbers from 1 to N.
# 14. Check if a number is prime.
# 15. Print Fibonacci series up to N terms.
# 16. Print a pattern of stars (triangle shape).
# 17. Count digits in a number.
# 18. Sum of digits of a number.
# 19. Find the reverse of a number.
# 20. Print multiplication tables for numbers 1 to 10.



# 1 ---------------------------------------------------------------------#

# arr1=[]
# for i in range(1,51):
#     arr1.append(i)
# print(*arr1, sep=', ')



# 2 ---------------------------------------------------------------------#

# arr1=[]
# for i in range(1,101):
#     if i%2 == 0 :
#         arr1.append(i)
# print(*arr1, sep=', ')



# 3 ---------------------------------------------------------------------#

# num = input('Enter the number N for the sum of numbers 1 to N : ')
# arr1 = []
# for i in range(0,int(num)+1):
#     arr1.append(i)
# total_sum = sum(arr1)
# print(f'the total sum upto N is : {total_sum}')
    


# 4 ---------------------------------------------------------------------#

#we will divide the num in range(2,num) and check its remainder
#if the remainder is == 0 (means it was divisible by a number, thus not a prime)

# num = int(input('enter a number to check if its prime : '))
# if num > 1 :
#     for i in range(2,num) :
#         if (num %2) == 0 :
#             print("number is not a prime")
#             break
#     else:
#                 print("number is prime ")
# else:
#     print("number is not a prime")



# 5 ---------------------------------------------------------------------#

#fibonacii series is created by adding previous two numebrs and creating a new number 
#1,1,2,3,5,8,13,.....
# num = int(input("enter fibonacii seires number of elements : "))
# arr1 = [1,1]
# next_num = 1
# for i in range(1,num-1) :
#     next_num = arr1[i] + arr1[i-1]
#     arr1.append(next_num)
# print(arr1)



# 6 ---------------------------------------------------------------------#

# n = int(input('enter the no of rows in the star : '))

# for i in range(1,n+1):
#     print('*' * i)



# 7 ---------------------------------------------------------------------#

# num = input("enter the number : ")
# print(f'the length of the number is {len(num)}.')



# 8 ---------------------------------------------------------------------#

# num = list(input("enter the number : "))
# int_list = list(map(int,num))
# total_sum = 0 
# for i in range(len(int_list)+1):
#     total_sum += i 
# print(f'the total sum of the digits in the number is {total_sum}')



# 9 ---------------------------------------------------------------------#

# num = input("enter the number : ")
# print(f'reversed number is {num[::-1]}')



# 10 ---------------------------------------------------------------------#

# for i in range(1,11):
#     print("----------------------------------")
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
    
