# Q1 Write a program to find the greatest of four numbers entered by the user.

# num1=  int(input("Enter number 1st number : "))
# num2=  int(input("Enter number 2nd number : "))
# num3=  int(input("Enter number 3rd number : "))
# num4=  int(input("Enter number 4th number : "))

# if(num1>num2):
#     if(num1>num3):
#         if(num1>num4):
#             print("Number 1 ", num1 ,"is greater")
# elif (num2>num3):
#     if(num2>num4):
#         print("Number 2", num2 ,"is greater")
# elif(num3>num4):
#     print("Number 3", num3 ,"is greater")
# else:
#     print("Number 4", num4 ,"is greater")

# # alternate 
# if((num1>num2) and (num1>num3) and (num1>num4)):
#     print("Number 1 is greater & the number is ", num1)
# elif(((num2>num1) and (num2>num3) and (num2>num4))):
#     print("Number 2 is greater & the number is ", num2) 
# elif(((num3>num1) and (num3>num2) and (num3>num4))):
#     print("Number 3 is greater & the number is ", num3) 
# elif(((num4>num1) and (num4>num3) and (num4>num2))):
#     print("Number 4 is greater & the number is ", num4) 

# Q2 Write a program to find out whether a student has passed or failed if it requires atotal of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# sub1 = int(input("Enter mark1 "))
# sub2 = int(input("Enter mark2 "))
# sub3 = int(input("Enter mark3 "))

# if(sub1>=33 and sub2>=33 and sub3>=33 ):
#     total=sub1+sub2+sub3
#     print(total)
#     avg=total/3
#     print(round(avg))
#     if(avg >= 40):
#         print("pass")
#     else:
#         print("Fail")
# else:("Fail")

# Q3 A spam comment is defined as a text containing following keywords:“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

spam_keywords = ['make a lot of money', 'buy now', 'subscribe this', 'click this']
text = input("Enter your text: ").lower()

is_spam = False
for phrase in spam_keywords:
    if phrase in text:
        is_spam = True
        break

if is_spam:
    print("Spam")
else:
    print("Not spam")



#Q4 Write a program to find whether a given username contains less than 10 characters or not.

# name= input("Enter you name")
# if(len(name)>10):
#     print("Name character is more than 10")
# else: print("Name character is less than 10")



#Q5 Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter the mark"))

# if(marks>=90 and marks<=100):
#     print("Grade is Ex")
# elif (marks>=90 and marks<=100)

if(marks<50):
    print("Grade is F")
elif(marks<=60):
    print("Grade is D")
elif(marks<=70):
    print("Grade is C")
elif(marks<=80):
    print("Grade is B")
elif(marks<=90):
    print("Grade is A")
elif(marks<=100):
    print("Grade is EX")
else: print("Marks can't be greater than 100")