#  write a program to print twinkle twinkle little star....

print('''Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are! ''')
# Note 
#  Using triple single quotes (''') & triple double quotes we can print multi line string. 


# Q2 Install an external module and use it to perform an operation of your interest

# for this question i'm using pyttsx3 - ( text to voice module)

import pyttsx3;

engine = pyttsx3.init()
engine.say("Hi kunal! how are you! all good!")
engine.runAndWait()


# Q3 - Write a python program to print the contents of a directory using the os module.Search online for the function which does that.

import os

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in the current directory
entries = os.listdir(current_directory)
# print(entries)
print(f"Contents of '{current_directory}':")
for entry in entries:
    print(entry)
