 
#Assignment-02
#Mahadi Hasan Mishuk

#21SOEC11649

#CE-D ROLL 54

'''1- Write a program to demonstrate all the basic data types in Python.'''


''' Neumeric int  float complex  bool string  list tuple'''

int=10
float=10.5
complex=5+2j
bool=10>20
str="Mishuk"
list=[10,20,30,40]
tuple=('G','h','i')


print(int)

print(float)

print(complex)

print(bool)

print(str)

print(list)

print(tuple)





"""2- Design a simple calculator using Python.
"""


num1=int(input("Enter any positive number="))
num2=int(input("Enter any positive nnumber="))

opt=input("Enter any operator=")

if opt == '+':
    print(num1+num2)
elif opt == '-':
    print(num1-num2)
elif opt == '*':
    print(num1*num2)
elif opt == '/':
    print(num1/num2)
else:
    print("Invalid operator")




"""3- Write a program to print the largest and smallest number of two numbers input from user
with and without using library functions.
"""



num1=int(input("Enter any positive number="))
num2=int(input("Enter any positive nnumber="))

if num1 > num2:
  print("Num1 is maximum",num1)
  print("Num2 is minimum",num2)



"""4- Using Python ask the user to enter his details and print the details again on the screen."""



name=str(input("Enter your name="))
age=int(input("Enter your age="))
city=str(input("Enter your city="))
profession=str(input("Enter your profession="))
contact_num=int (input("Enter your contact number="))

print("Bio-Data")
print("Name:", name)
print("Age:", age)
print("City:",city)
print("Profession",profession)
print("Contact Num:",contact_num)



"""5- Write a Python program to accept a filename from the user and print the extension of that.

Input: test.py
Output: py


#blank




6- Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.


Input: 5
Output: 615
"""

n=5
num1= int ("%s" % n )
num2= int ("%s%s" %(n,n))
num3= int ("%s%s%s" %(n,n,n))
 
print(num1+num2+num3)



"""7- There are errors in the following code, remove those errors and write Output

1stnumber ==2
2ndnumber==7
sum == 1stnumber + 2ndnumber
print (1stnumber)
print(2ndnumber)
print (Sum)
"""

number1=2
number2=7
sum =  number1  +  number2
print(number2)
print(sum)