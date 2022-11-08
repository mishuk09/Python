 #Daily lab practice


x="4"
y="2"
z=int(x)+int (y)
print(z)



str =input("Input Here!!!:")
num = len(str)
x = num
print (((x))*x)



x="4"
y="2"
z=x+y
print(z)



print('My name is Md Mahadi Hasan Mishuk')
print('I am from Bangladesh')
print('I am a student of RKU')
print("I am good in   football")
print("'Md Sheikh Mahiuddin'")
print("Father\'s name:Md Sheikh Mahiuddin")



print(5+3)
type('rku')




"""# Type **casting**"""

num1 = input("enter any number=")
num2= input("Enter any number=")
sum= int(num1)+int(num2)
print("Sum is",sum)

div = int (num1)-int (num2)
print("DIv iss",div)




"""# Area of any ***shape***"""

base= float (input("ENter base="))
height= float (input("Enter height="))

area= 0.5*base*height
print("Area is ",area)5

from math  import *

print(max(10,20))
print(min(10,20))
print(abs(-8))
print(pow(2,3))
print(sqrt(25))
print(round(25))

type(20)

type("Mahadi Hasan Mishuk")

type( True)






num1=20
num2=30
print("The sum is",num1+num2)
print(f"{num1}+{num2} = {num1+num2}")

print("Mahadi Hasan Mishuk",end="     ")
print("1740106176")

print("Mahadi",end=" ")
print("Hasan Mishuk",end=" ")
print("10/03/2000")

print("Mahadi Hasan Mishuk")
print("I am from Bangladesh")
print("I am a student of RKU")
print("My hobby is traveling")

x = input("Enter write=")
y = input("Enter digit=")
print( x * y)

spam = "eggs"
print(spam * 3)



type(3)






name=    input("enter your name:")
print("please enter the marks as below:")
maths=int(input('maths:'))
while(maths>100 or maths<0):
  print("Invalid input,please enter valid marks between 0 to 100")
  maths=int(input("maths:"))
science=int(input('science:'))

while(science>100 or science<0):
  print("Invalid input,please enter valid marks between 0 to 100")
  science=int(input("science:"))
biology=int(input('biology:'))

while(biology>100 or biology<0):
  print("Invalid input,please enter valid marks between 0 to 100")
  boilogy=int(input("biology:"))
chemistry=int(input('chemistry:'))

while(chemistry>100 or chemistry<0):
  print("Invalid input,please enter valid marks between 0 to 100")
  chemistry=int(input("chemistry:"))
physics=int(input('physics:'))

while(physics>100 or physics<0):
  print("Invalid input,please enter valid marks between 0 to 100")
  physics=int(input("physics:"))

sum=maths+science+biology+chemistry+physics
print(sum,"/500",sep="")
percentage=(sum/500)*100
print(percentage,"%",sep="")

if(percentage>80) and (percentage<101):
  print("Grade:A")
  print("Congratulation,u have secured grade A")
elif(percentage>60) and (percentage<81):
  print("Grade:B")
  print("Congratulations,u have secured grade B")
elif(percentage>=40) and (percentage<61):
  print("Grade:C") 
  print("Congratulations,u have secured grade C") 
else:
  print("fail")
  print("Oops,you failed...")

firstnumber=2
secondnumber=7
sum=firstnumber+secondnumber
print(firstnumber)
print(secondnumber)
print(sum)






n=2
n1=int("%s" %n)
n2=int("%s%s" %(n,n))
n3=int("%s%s%s" %(n,n,n))

print(n1+n2+n3)

num=10
if num%2==0:
  print(num,'This is even number')
else:
  print(num,'This is odd number')

num=10
if num%2==0 or num%5==0:
  print(num,'This is divisible')
else:
  print(num,'This is not divisible')





"""3- Write a program to accept a number from 1 to 7 and display the name of the day like 1 for
Sunday, 2 for Monday and so on.
"""

a=input("Enter num=")
b=input("Enter num=")
c=input("Enter num=")
d=input("Enter num=")
e=input("Enter num=")
f=input("Enter num=")
g=input("Enter num=")

s1=input("Enter Day=")
s2=input("Enter Day=")
s3=input("Enter Day=")
s4=input("Enter Day=")
s5=input("Enter Day=")
s6=input("Enter Day=")
s72=input("Enter Daymonday=")

day=int(input("Enter any value in 1-7 ="))

if day==1:
   print("Satrday")
elif day==2:
  print("Sunday")
elif day==3:
  print("Monday")
elif day==4:
  print("Tueday")
elif day==5:
  print("Wednesday")
elif day==6:
  print("Thusday")
elif day==7:
  print("Fryday")
else:
  print("Invalid input")

temp=int(input("Enter temperature="))

if temp<0:
  print("ICE")
elif 0<temp and temp<100:
  print("Water")
else:
  print("Steam")

age=int(input("Enter your age="))

if age>12:
  print("You are allow")
else :
 
    prnt=str(input("Enter that parents with him="))
    if prnt=='yes':
      print("You are most welcome")
    elif prnt=='no':
      print("Please wait, Sara is coming to help")

x=1
while x>10:
  x=x+1
  if x==7:
     print(x)

x=1
while x >11:
  x=x+1
   if x==7:
     break
   print(x,end=" ")

n = 0
while n <10:
     n=n+ 1
     if n == 7:
        continue
     print(n)



     

"""Enter how many person :5
person1 age is :1
person1 age is :2
person1 age is :3
1person1 age is :4
person1 age is :5

 total expence is 300



 age<5=0
 5-10=100
 11-20=200
 21+=300
 then make the total 
 total cost and and you have to aske the vauscer code then get 50% discount
"""

def num():
  print('A')
  print('B')
  print('C')
  print('D')
num()

def num(x,y):
  z=x*y
  print(z)
num(4,5)

def num(x,y):
  return x*y
num(4,5)

def meter(x):
  cm=x*100
  print(cm)
  ince=x*37.39
  print(ince)
  feet=x*3.28
  print(feet)
meter(5)

class CED:
    pass
  student2=CED()
  student2.name='Mahadi'
  student2.city='Rajkot'
  student2.mobile=7069089662

  print(student2.name)
  print(student2.city)
  print(student2.mobile)

x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("No")

try:
   num1=7
   num2=0
   print(num1/num2)
   print("Calculation is done")
except ZeroDivisionError:
  print("An erron occured")
  print("Due to zero divitin by mahadi")

try:
  variable="rku"
  print(variable +  "helllo")
  print(variable / 2)

except ZeroDivisionError:
  print("Divider by zero")
except( ValueError,TypeError):
  print("Error occure")

def sum(x,y):
  return x+y
print(sum(10,20))


def detils(a,b):
  print(a)
  print(b)

  return a+b
print(detils(b=20,a=10))

#Default arguments

def sum(x,y=10):
  print(x)
  print(y)
  return
print(sum(x=20))

fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
num = int(input())
#your code goes here
if (num<0 or num>7):
    print("Wrong number")
if (num>=0 or num<=7):
    print(fruits[num])

sum=lambda a,b:a+b

print(sum(10,20))

