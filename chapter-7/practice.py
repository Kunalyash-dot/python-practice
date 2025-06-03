# Write a program to print multiplication table of a given number using for loop

# num = int(input("enter the number "))

# for i in range (1,11):
#    print(f'{num} x {i} = {i*num}')

#Q2 Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if (i[0] == 'S'):
#         print(i)

#Q3 Attempt problem 1 using while loop.

# num=int(input("Enter the number : "))

# i=1
# while (i<11):
#     print(f'{num} x {i} = {num*i}')
#     i +=1

# Write a program to find the sum of first n natural numbers using while loop.

# num =int(input("Enter the number : "))

# i=1
# result=0

# while(i<=num):
#     result += i
#     i += 1

# else:
#     print(result)    

# Write a program to calculate the factorial of a given number using for loop.

# num = int(input("Enter the number : "))
# result = 1

# for i in range(1,num+1):
#     print(f'{result} x {i} = {result*i}')
#     result *= i

# else:
#     print(result)    

# . Write a program to print multiplication table of n using for loops in reversed order.

# num = int(input("Enter the number : "))

# for i in range (1,11):
#     print(f'{num} x {11-i} = {num*(11-i)}')
#     i -+ 1



#  Write a program to find whether a given number is prime or not.

# num  = int(input("Enter the number : "))

# for i in range (2,num):
#     if(num%i == 0):
#         print(f'Entered number {num} is not a prime number')
#         break
# else:
#     print(f"Entered number {num} is prime number")


# Write a program to print the following star pattern.
#  *
# ***
#***** for n = 3

# num= int(input("Enter a number : "))

# for i in range (1,num+1):
#     print(" " * (num-i), end="")
#     print("*" * ((2*i)-1),end="")
#     print("")

# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# num=int(input("Enter the number : "))

# for i in range (1,num+1):
#     print("*"*i)

# Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *

# num = int(input("Enter the number : "))

# for i in range (1,num+1):
#     if(i==1 or i==(num)):
#         print("*" * (num))
#         # print("")
#     else:
#         print("*",end="")
#         print(" " * ((num)-2),end="")
#         print("*",end="")
#         print("")
