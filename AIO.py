#1
items=int(input("Please enter the number of items you want to purchase: "))
if items<10:
  cost=120*items
elif 10<items and items<99:
    cost = 100*items
elif items>=100:
  cost =70*items
print("the cost is", cost)
#2
n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum=sum+j
print(sum)
#3
x=int(input("enter x: "))
n=int(input("enter n: "))
sum=1
for i in range(1,n+1):
      if x%2==0:
       sum +=(x**i)
      else:
       sum -=(x**i)
sum=sum+(x**i)
print(sum)
#4
sum=1
for sum in range(1,10):
    print('*'*sum)
    sum=sum+1
print('if you are good at something never do it for free')
#5 prime
a=int(input("Enter number: "))
num=0
for i in range(2,a//2+1):
 if( a%i ==0):
  num=num+1
if(num<=0):
  print("Number is prime")
else:
 print("Number isn't prime")
 #6 factorial
n=int(input("enter a number: "))
sum=1
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact *=j
    sum=sum+(1/fact)
print(sum)
# +-factorail
x=int(input('enter a number: '))
n=int(input('enter a number: '))
sum=1
for i in range(1,n+1):
    fact=1
    for j in range(1,n+1):
        fact *=j
if x%2==0:
       sum +=(x**i)
else:
       sum -=(x**i)
sum=sum+(i*j/fact)
print(sum)
#sum of factorial
num = int(input("enter a number: "))
fac = 1
sum=0
for i in range(1, num+1):
    fac = fac * i
sum=sum+fac
print(sum)
#sum of 1/fact
num = int(input("enter a number: "))
fac = 1
sum=0
for i in range(1, num+1):
    fac = fac * i
sum=sum+(i/fac)
print(sum)
#maxmin
n=int(input("enter the number: "))
max = n
min = n
for i in range(1,10):
        n=int(input("enter the number: "))
        if n>max:
           max=n
        elif n<min:
           min=n
        else :
            print("we have two same values")
print("the greatest number is",max,"the minimum number is",min)
#perfectt number
num=int(input(" Please Enter any num: "))
i= 1
s=0
while(i<num):
    if(num%i==0):
        s=s+i
    i=i+1
if (s==num):
    print("yes it is-",num)
else:
    print(num,"nope")
#Python programming code to check whether the character is Alphabet or not
c=(input("enter a number: "))
if((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')): 
    print("The Given character ", c, "is an Alphabet") 
elif(c >= '0' and c <= '9'):
    print("The Given character ", c, "is a Digit")
else:
    print("The Given character ", c, "is a Special character")
#Sum to n terms
n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum=sum+j
print(sum)
#break fn
for i in range(1,6):
    if i==5:
        print("hello")
        break
    else:
        print(i)
print('done')
#continuousfn
for i in range(1,6):
    if i==5:
        print('hello')
        continue
    else:
        print('i')
        print("done")
#number of days in a month
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name == "february":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("april", "june", "september", "november"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
elif month_name in ("january", "march", "may", "july", "august", "october", "december"):
	print("No. of days: 31 day")
else:
    print("wrong month name")
#### workshet
####
#
##
##
#
#1a
import math
x=int(8)
y=int(43)
print(math.sqrt(x+y),"the square root of 8+43")
#1b
x=int(100)
y=int(32)
integral=x/y
print(integral)
#2
string = input("Enter any string: ")
if string == 'x':
    exit()
else:
    newstr = string
    print("\nRemoving vowels from the given string")
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")
    print("New string after successfully removed all the vowels:")
    print(newstr)
#3
list1=[-2,1,-3,-15,16,-17,5,-3,-6]
list2=[0]*9
a=len(list1)
a=a-1
j=0
for i in range(9):
  if list1[i]>0:
      list2[j]=list1[i]
      j+=1
  else:
      list2[a]=list1[i]
      a-=1
print(list2)
#4
name = input("Enter Name : ")
basic = float(input("Enter Basic Salary : "))
if basic <= 10000:
 da = basic *0.8
 hra = basic * 0.2

elif basic <= 20000:
 da = basic *0.85
 hra = basic * 0.25
else:
 da = basic *0.9
 hra = basic * 0.3
gross = basic + hra + da
pf = 0.12 * basic
net = gross - pf
print (" Name : ",name)
print (" Basic Salary : ",basic)
print (" Gross Salary : ",gross)
print (" Net Salary : ",net)
#sum of GP
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/i)
    
print("The sum of series is",(sum1))
#factorial
num=int(input("enter just a number: "))
fac=1
for i in range(1,num+1):
 fac=fac*i
print("factorial of",num,"is",fac)
#range function
n=5
product=1
for i in range(1,11):
    product=i*n
    print(product,"x",i)
#rangefn2
N = int(input("enter the number"))
sum=0
for i in range(1,N+1):
    sum=sum+1
    print(sum)
#whether a triangle is one of the three types
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
#entered number is 4 or 8
a = input("Enter a number : ")
if a[-1] == "4":
 print("ends with 4")
elif a[-1] == 8:
 print("ends with 8")
else:
 print("ends with neither")   
#entered value wull form a triangle or not
a=int(input("Enter 1st side of triangle:"))
b=int(input("Enter 2nd side of triangle:"))
c=int(input("Enter 3rd side of triangle:"))
if a+b>c:
     if b+c>a:
            if a+c>b:
                  print("The given measurements:",a,b,c,"forms a triangle")
else:
    print("The given measurements:",a,b,c,"does not form a triangle")
#factorial of n number
num=int(input("enter just a number: "))
fac=1
for i in range(1,num+1):
 fac=fac*i
print("factorial of",num,"is",fac)
#division by factorail time n
n = int(input("Enter the end number : ")) 
sum = 0 
for i in range(n+1):
    fact=1
    for j in range(1,i):
        fact *= j
        term = 1/fact
        sum += term
    print(sum)
#leap year
year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print(year," is a leap year")  
       else:  
           print("{0} is not a leap year",year)  
   else:  
       print("{0} is a leap year",year)  
else:  
   print("{0} is not a leap year",year)  
print(year,"this is shit")
#maths quadratic equation
import math     
a = int(input("enter 'a' numeric value such that a≠0: "))
b = int(input("enter 'b' numeric value: "))
c = int(input("enter 'c' numeric value: "))
#cal d
D=(b**2-4*a*c)
if D>0:
    print(D)
elif D==0:
    print(D)
    print("tHis Has equal roots")
elif D<0:
    print("tHis Does not Have any roots")
else:
    print("sorry")
#sol
sol1 = (-b-math.sqrt(D))/(2*a)
sol2 = (-b+math.sqrt(D))/(2*a)

print('THe solution are {0} and {1}'.format(sol1,sol2))
