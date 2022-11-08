 
"""Assignment-05

 
 Assignment-05 
 Mahadi Hasan Mishuk    

 CE-D   54

 21SOECE11649

1. endswith()
Demonstrate the use of the following functions of String Data Structure: Strip(), split(), splitlines(), join(), replace(), isnumeric(), textwrap.wrap(), lower(), upper(), capitalized(), title(), lstrip(), rstrip(). <sting> in <string>, <string>.startswith(<string>), <string>.endswith(<string>), <string>.find (<string>), <string>.index (<string>).
"""

strip()=           its remove space in beginign and ending.
split() =          The split() method splits a string into a list.
splitines()=       Split the string keep the line breaks.
Join()=            The join() method takes all items in an iterable and joins them into one string.
replace()=         The replace() method replaces a specified phrase with another specified phrase.
isnumeric()=       The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
lower()=           The lower() method returns a string where all characters are lower case.
upper()=           The Upper() method returns a string where all characters are Upper case.
Capitalize()=      The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
title()=           The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
rstrip()=          The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
startswith()=      The startswith() method returns True if the string starts with the specified value, otherwise False.
endswith() =       The endswith() method returns True if the string ends with the specified value, otherwise False.
Find()=            The find() method returns -1 if the value is not found.
Index()==          The index() method returns the position at the first occurrence of the specified value.

str="Mahadi Hasan Mishuk"
print(str.strip())

str="Mahadi Hasan Mishuk"
print(str.split())

str="Mahadi Hasan \n Mishuk"
print(str.splitlines())

str="Mahadi Hasan"
str2="Mishuk"
print(str.join(str2))

str="Mahadi Hasan Mishuk"
 
print(str.replace("Hasan","Mishuk"))

str="12345"
print(str.isnumeric())

str="Mahadi Hasan Mishuk"
print(str.lower())

str="Mahadi Hasan Mishuk"
print(str.upper())

str="Mahadi Hasan Mishuk"
print(str.capitalize())

str="Mahadi Hasan Mishuk"
print(str.title())

str="Mahadi Hasan Mishuki"
print(str.lstrip())

str="Mahadi Hasan Mishuk"
print(str.rstrip())

str="Mahadi Hasan Misuk"
print(str.startswith("H",7,20))

str="Mahadi Hasan Mishuk"
print(str.find("Hasan"))

str="Mahadi Hasan Mishuk"
 str2=str.split(" ")
 for i in str2:
   if len(i)%2==0:
     print(i)

str="python"
 a=str.replace("t","")
 print(a)




""" 5. Write a Python program which matches the following output:

Input: Python

Output: P

y

t

h

o

n


"""


a=input()
for i in a:
  print(i)



"""7. Rewrite the following code after removing all errors.

while = "Enter a number to check if it is divisible by 2: "

x= input(while)

if x %2 = 0:

    print("divisible")

else:

    print("not divisible")
"""

a = int(input("Enter any number"))

if a %2 == 0:
 print("divisible")
else:
  print("not divisible")
