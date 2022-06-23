from datetime import date
"""print('today is a good day to learn python')
print('Python is fun!')
print('Python\'s strings are easy to use.')
print('We can even include "quotes" in strings.')"""
greeting = "Hello"
Welcome= "Welcome to my Age Calculator"
print("%s, %s" % (greeting, Welcome))
name = input("Please enter your name: ")
# print(greeting + name)
print("%s %s" %(greeting,name))
dateofbirth = int(input("Please enter your date of birth: "))
age= date.today().year - dateofbirth
print("%s %s, you are %d years old." % (greeting, name, age))
print(type(age))