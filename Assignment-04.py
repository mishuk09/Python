 
"""Assignment-04

 
Mahadi Hasan Mishuk

21SOECE11649

CE-D   Roll 54

"""

""" Write a program to print all the even numbers between [0-100] using for loop, and print all the odd numbers between [100-200] using while loop.
"""

#while loop
i=2
while  i<=100:
  print(i)
  i=i+2
 
#For loop

for x in range(100,200,2):
  print(x)
  x=x+2



"""Write a program to print all the numbers between [100-0] except for numbers that are divisible by 5 using for loop, and print all the numbers between [512-256] except for the numbers that are divisible by 7 using while loop."""

for x in range(100,0,-1):
  if x%5 !=0:
   print(x)  


x=512
while x >=256:
 if x%7 ==0:
      print(x)
      x=x-1



"""Write a program to take a sentence from the user and re-print it without any spaces, stop printing if you meet a number.Write a program to take a sentence from the user and re-print it without any spaces, stop printing if you meet a number."""



num=input("Enter your name",end='')
print(num)



"""Write a program to calculate the nth number of Fibonacci series"""

num=int(input("How many number you want=")) 
num1= 0  
num2 = 1  
count = 0  
  
 
if num <= 0:  
    print ("Please enter valid number")  
 
elif num == 1:  
    print ("The Fibonacci sequence of the numbers up to", n)  
    print(num1)  
 
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < num:  
        print(num1)  
        temp = num1+num2
        
        num1=num2 
        num2=temp
        count += 1

list= input("Input a string")
d=l=0
for c in list:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

n=5
for i in range(n+1):
   print(i * '*')
n=5
for i in range(n- 1):
  print(i*'*')

n=5
for i in range(n+1):
  print(i*1)