#For loop#

# Print number 1 to 10
for i in range(1,10):
    print(i)

#Sum of Numbers from 1 to N
a=int(input("Enter numbers"))
total=0
for i in range(1,a+1):
    total +=i
print("Sum of numbers from 1 to",a,"is",total)

#Multiplication table
num=int(input("Enter a numbers"))
for i in range(1,11):
    print(f"{num} * {i} = {num *i}")

#Factorial of a Number
x=int(input("Enter a number"))
factorial=1
for i in range(1,n+1):
    factorial * =i
print(f"the Factorial of {n} is {factorial}")

#Intermediate: Fibonacci Series
y=int(input("Enter a numprer of terms:"))
a,b=0,1
for_in range(n):
    print(a, end=" ")
    a,b=b, a + b

#Prime Numbers in a Range

n=int(input("Enter a number :"))
print("Prime number between 1 and " ,n,"are:")
for num in range(2,n+1):
    is_prime=True
    for i in range(2, int(num/2)+1):
        if num % i==0:

#Palindrome Check
string=input("Enter a string :").lower()
is_palindrome=True
for i in range(len(string)//2):
    if string[i]=string[len(string)-i-1]:
        is_palindrome=False
        break

if is_palindrome:
    print(f"the string '{string}' is a palindrome.")
else:
     print(f"the string '{string}' is not a palindrome.")

#Iterating by Index of Sequences
li=["Aaliya Fatma","Faisal Sheikh","Shadmani Noor","Ummehani Noor"]
for index i in range(len(li)):
    print(li[index])
