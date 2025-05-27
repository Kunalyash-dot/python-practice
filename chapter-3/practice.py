# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input('Enter your name :')

print("Good Afternoon", name)


# Q2 - Write a program to fill in a letter template given below with name and date.

date = input("Enter DOJ")
print(f'''
    Dear  {name}
    You are selected!
    {date}
 ''')

# Write a program to format the following letter using escape sequence characters.

letter = 'Dear Kunal , \n this python course is nice. \n Thanks!'
print(letter)

print(name.find("  "))
print(name.replace("  "," "))