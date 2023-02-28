#Print Hello world!

"""print("Hello world!")"""

#Python Program to add two numbers

"""num_1=10
num_2=20
print(num_1+num_2/2)
"""

#Python program to find the square root

"""num_1=6

num_2=num_1**0.5

print(num_2)
"""


#Python Program to Calculate the Area of a triangle
"""a=10
b=20
c=30

s=(a+b+c)/2

area=(s*(s-a)-(s-b)*(s-c))**0.5
print(area)
"""

#Python Program to solve Quadratic Equation

"""a=10
b=20
c=10
x=(b**2)-4*(a*c)
x_one=(-b+(x**0.5))/2*a
x_two=(-b-(x**0.5))/2*a
print(x_one)
print(x_two)
"""

#Python Program to Swap Two Variables

"""x=5
y=10
temp=x
x=y
y=temp
print(x,y)
"""

#Python program to generate a Random Number

"""import random
x=random.randint(1,100)
print(x)
"""

#Python Program to Convert Kilometres to Miles

"""kilometres=1000
miles=0.621371*kilometres
print(kilometres)
"""

#Python Program to Convert Celcius to Fahrenheit

"""Celcius=31
Fahrenheit=Celcius*1.8+32
print(Fahrenheit)
"""

#Python program to check if a number is positive,negative or 0

"""number_1=10
if number_1>0:
    print("Positive")
elif number_1%2<0:
    print("Negative")
elif number_1==0:
    print("0")
else:
    print("Something that wrong! Please try again")
"""

#Python program to check if a number is odd or even

"""number_1=10
if number_1%2==0:
    print("odd")
elif number_1%2%2==1:
    print("even")
elif number_1==0:
    print("0")
else:
    print("Something that wrong! Please try again")

"""

#Python Program to check leap year
"""These extra days occur in each year that is an integer multiple of 4 (except for
 years evenly divisible by 100, but not by 400). The leap year of 366 days has 
 52 weeks and two days,hence the year following a leap year will start later by
  two days of the week."""

"""year=1992

if (year%4==0 and year%100!=0) or (year%400==0):
    print("This is leap  year")
else:
    print("No")
"""

#Python Program to find the Largest Among Three Numbers

"""list_1=[1,2,3]
print(max(list_1))
"""

#Python Program Check Prime Number

"""x=2
for i in range(1,x):
    if i%x==0:
        print("Not Prime Number")
        break
else:
    print("Prime Number")
"""

#Python Program to Print all Prime Numbers in an Interval

"""liste_1=list()

for i in range(1,101):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            liste_1.append(i)
print(liste_1)
"""        

#Python Program to find the factorial of a Number

"""5!=5*4*3*2*1"""

"""x=5
carpim=1 #çarpma  kullandığımız için 1 yazdım
for i in range(1,x+1):
    carpim*=i
print(carpim)
"""

#Python program to display the multiplication table

"""for i in range(1,11):
    for j in range(1,11):
        print(f"\n {i} * {j} ={i*j}")
"""

#Python Fibonacci sequence

"""def func(x):
    if x<=1:
        return x
    else:
        return (func(x-1)+func(x-2))
print(func(9))"""
   

#Python program to check Armstong Number

"""N haneli bir sayının basamaklarının n’inci üstlerinin toplamı, 
sayının kendisine eşitse, böyle sayılara Armstrong sayı denir.
Örneğin 407 sayısını ele alalım. (4^3)+ (0^3)+(7^3) = 64+0+343 = 407 
sonucunu verir. Bu da 407 sayısının armstrong bir sayı olduğunu gösterir."""

"""number=407
number_1=0
for i in str(number):
    number_1+=(int(i)**3)
if number_1==number:
    print("This is armstong number!")    
"""

#Python Program tı find the sum of natural numbers

"""num=16
sum_of_natural_numbers=num*(num+1)
if num>0:
    print(sum_of_natural_numbers)
elif num<0:
    print("Please give me positive number")
else:
    print("SOmeething is wrong please try again")
"""

#Python program to display powers of 2 using Anonymus Function
"""terms=10
result=list(map(lambda x:2**x,range(terms)))
for i in range(terms):
    print(result[i])
"""

#Python program to find numbers divisible by another number

"""list_1=[1,2,3,45,6,78,65,26,90,78,91,104]

result=list(filter(lambda x:(x%13==0),list_1))
print(result)
"""


#Python Program to Convert to Decimal to Binary,Octal and HexaDecimal
"""dec=300
print("is binary:",bin(dec))
print("is octal:",oct(dec))
print("is hexadecimal:",hex(dec))
"""

#EKOK 
"""import math
x=6
y=8
print(f"EBOB:{math.gcd(x,y)}")
print(f"EKOK:{x*y/math.gcd(x,y)}")
"""

#Bir sayının bölenleri

#Örnek olarak 8=1,2,4,8

"""sayi_1=320
for i in range(1,sayi_1+1):
    if sayi_1%i==0:
        print(i)
"""
"""import random,itertools

kart_desteleri=list(itertools.product(range(1,14),["maça", "kupa", "karo","sinek"]))
random.shuffle(kart_desteleri)

print("Elde edilen:")
for i in range(5):
    print(kart_desteleri[i][0], "de", kart_desteleri[i],)
"""

"""import calendar
yy=2023
mm=1
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

#display the calendar
print(calendar.month(yy, mm))
"""

#To find sum of  Natural Numbers Using Recursion
"""def func(n):
    if n<=1:
        return 1
    else:
        return n+func(n-1)
sum=22
if sum<0:
    print("Please enter a positive number")
else:
    print(f"The sum of Natural number is:{func(sum)}")"""

#Python program to add Two Matrices

"""X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j]=X[i][j]+Y[i][j]
print(result)
"""


#Python Multiply Two Matrices


"""X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[1,1,1],
         [1,1,1],
         [1,1,1]]
for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j]=X[i][j]*Y[i][j]
print(result)
"""



#Matrices Transpose


"""X = [[12,7],
    [4 ,5],
    [7 ,8]]

result = [[0,0,0],
[0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i]=X[i][j]
for r in result:
    print(r)
"""

#Python Program to check Whether a String is Palindrome or Not

"""value_1=input("Say something whether palindrome or not:")
value_2=value_1[::-1]
if value_1==value_2:
    print("This is palindrome")
else:
    print("This is not palindrome")
"""

#Python Program to remove Punctuations From a String 

"""number_1="1234567890"
value_1="Hello1 My2 name3 is4 Salih6"
no_number=""
for i in value_1:
    if i not in number_1:
        no_number+=i
print(no_number)
"""


#kelimeleri alfabetik sıraya dizme ve sayıları kelimeye yazdırmama


"""number_1="0123456789"
value_1="Merhaba1 Benim2 İsmi4m Sali7h Birdal9"
clear_value=""

def kelimeler_temize_cikar(clear_value):
    for i in value_1:
        if i   not in number_1:
            clear_value=clear_value+i
    print(clear_value)

def alfabetik_siraya_koy(clear_value):
    kelimeler=[kelime.lower() for kelime in clear_value.split()]
    kelimeler.sort()
    for kelime in kelimeler:
        print(kelime)

kelimeler_temize_cikar(clear_value)
print(clear_value)
alfabetik_siraya_koy()
"""



"""number_1="0123456789"
value_1="Merhaba1 Benim2 İsmi4m Sali7h Birdal9"
clear_value=""

def kelimeler_temize_cikar(clear_value):
    for i in value_1:
        if i   not in number_1:
            clear_value=clear_value+i
    return clear_value

def alfabetik_siraya_koy(clear_value):
    kelimeler=[kelime.lower() for kelime in clear_value.split()]
    kelimeler.sort()
    for kelime in kelimeler:
        print(kelime)


print(alfabetik_siraya_koy(clear_value))
"""  

"""import math
 
sayi_gir = abs(int(input("Lütfen basamak sayısını merak ettiğiniz sayıyı giriniz:")))
 
if sayi_gir == 0:
  print ("0 girdiniz...")
else:
  basamak = math.log10(sayi_gir)
  virgulsuz_basamak = round(basamak)
  print ("Girdiğiniz sayının basamak sayısı:", virgulsuz_basamak+1)
"""

