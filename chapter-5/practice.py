# Q1 Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

hindi_words ={
    "pani":"water",
    "chawal":"rice",
    "pyar":"love"
}

# Q2 Write a program to input eight numbers from the user and display all the unique numbers (once).

# number = set()
# n1=eval(input("Enter the number : "))
# number.add(n1)
# n1=eval(input("Enter the number : "))
# number.add(n1)
# n1=eval(input("Enter the number : "))
# number.add(n1)
# n1=eval(input("Enter the number : "))
# number.add(n1)
# n1=eval(input("Enter the number : "))
# number.add(n1)
# n1=eval(input("Enter the number : "))
# number.add(n1)
# n1=eval(input("Enter the number : "))
# number.add(n1)
# n1=eval(input("Enter the number : "))
# number.add(n1)

# print(number)

# Q-3 What will be the length of following set s:

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') 
# print(len(s))


# Q-4 Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique

name_lang={}

name1= input("Enter first person name : ")
lang1 = input("Enter first person's language : ")
name_lang.update({name1:lang1})
name2= input("Enter Second person name : ")
lang2 = input("Enter Second person's language : ")
name_lang.update({name2:lang2})
name3= input("Enter Third person name : ")
lang3 = input("Enter Third person's language : ")
name_lang.update({name3:lang3})
name4= input("Enter Fourth person name : ")
lang4 = input("Enter Fourth person's language : ")
name_lang.update({name4:lang4})

print(name_lang)