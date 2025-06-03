#Q1 Write a program using functions to find greatest of three numbers.

# def greaternum(num1,num2,num3):
#     if(num1>num2 and num1>num3):
#         # print(f'{num1} is greater')
#         return(f'{num1} is greater')
#     elif (num2>num1 and num2>num3):
#         # print(f'{num2} is greater')
#         return(f'{num2} is greater')
#     else:
#         # print(f'{num3} is greater')
#         return(f'{num3} is greater')



# num1=int(input("Enter the number 1 "))
# num2=int(input("Enter the number 2 "))
# num3=int(input("Enter the number 3 "))

# print(greaternum(num1,num2,num3))




#Q2 Write a python program using function to convert Celsius to Fahrenheit.

# def fahrenheit (n):
#     return f'for {n} deg celsius is equal to {round ((n * (9/5))+32)} deg Fahrenheit'

# print(fahrenheit(15))





#Q3 Write a recursive function to calculate the sum of first n natural numbers.

# def sumNaturalNumber(n):
#     if(n==0 or n==1):
#         print(f'this prints in if {n}')
#         return 1
#     else:
#         print(f'This print in else {n}')
#         return n + sumNaturalNumber(n-1)
    
# print(sumNaturalNumber(3))




#Q4  Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *


# def partten(n):
#     for i in range (1,n+1):
#         print("*" * ((n+1)-i))


# print(partten(3))



#Q5 Write a python function which converts inches to cms

# def inchToCms (n):
#     return (f'{n} inches is equal to {n*2.54} cms')

# print(inchToCms(5))


#Q6 Write a python function to print multiplication table of a given number.

# def tables (n):
#     resultTable=[]
#     for i in range (1,11):
#         print(f'{n} X {i} = {n*i}')
#         resultTable.append(f'{n} X {i} = {n*i}')
#     return resultTable 

# print(tables(2))