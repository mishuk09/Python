 
#Assignment-03

 

## Mahadi Hasan Mishuk
#21SOECE11649
#CE-D  ROLL 54

"""1- Write a program to check whether a number entered by user is even or odd.
"""

num=int(input("Enter any positive number=")) 

if num %2 ==0:
  print("Number is even")
else:
  print("Number is odd")




"""2- Write a program to check whether a number is divisible by 2 and 5 or not."""



num=int(input("Enter any positive number="))

if num%2==0 or num%5==0:
  print("Number is divisible by 2 and 5")
else:
  print("Number is not divisible by 2 or 5")



"""3- Write a program to accept a number from 1 to 7 and display the name of the day like 1 for
Sunday, 2 for Monday and so on.
"""

num=int (input("Enter number="))

if num==1:
  print("Satarday")
elif num==2:
  print("Sunday")
elif num==3:
  print("Monday")
elif num==4:
  print("Tuesday")
elif num==5:
  print("Wednesday")
elif num==6:
  print("Thusday")
elif num==7:
  print("Friday")
else:
  print("Invalid input")


"""4- Write a program that tells the form of Water whether it is Ice, Water or Steam. Display the
menu also as under
Temperature Less than 0 = Ice
Temperature Greater than 0 and less than 100 = Water
Temperature Greater than 100 = Steam

"""


temp=int (input ("Enter temperature="))

if 0>temp:
  print("ICE")
elif 0<temp<100:
  print("Water")
else :
  print("Steam")




""" Swimming pool is a dangerous place for children, therefore write a program to check the age
of people who will enter the swimming pool considering that:
If the age is less than 12, check if the child with one of his parents, then print “you are most
welcome”, if no one of his parents with him check his gender if male print “Please wait,
Ahmed is coming to help”, if she is a female print “Please wait, Sara is coming to help”.
If the age is more than 12 print “you are most welcome”.
"""

age=int(input("Enter your age="))
if age<12:
   ask=input("Enter your parents presents=")
   if ask=='yes':
     print("You are most welcome")
   elif  ask=='no':
     ask2=input("Enter your Gender=")
     if ask2 == 'male':
       print("Please wait, Ahmed is coming to help")
     else:
       print("Please wait, Sara is coming to help")


       

"""6- There are errors in the following code, remove those errors and write output:


year = int(input("Enter a year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else (year % 4 !=0) and (year % 100 != 0)
    print("{0} is not a leap year".format(year))


"""

year = int(input("Enter a year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
else :
    print("{0} is not a leap year".format(year))