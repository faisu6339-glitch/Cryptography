'''
def fact():
    num = int(input("Eneter the value:"))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    
    return fact

#Without function

num = int(input("Eneter the value:"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(fact)
    
# palindrome checker

def pal():
    word = input("Enter your word")
    j=len(word)-1
    flag=True
    for i in word:
        if i!=word[j]:
            flag=False
            break
        j-=1
    if flag == True:
        print("Palindrome")
    else:
        print("Not Palindrome")
        

#Using Function
def pac():
    a=input("Enter the value")
    if a == a[::-1]:
        print('Palindrome')
    else:
        print('not palindrome')

# reverse
def rev():
    word = input("enter value")
    print(word[::-1])

#swapping
def swap(x,y ):
   print("Before Swapping a:",x)
   print("Before Swapping b:",y)

x,y=y,x
return x,y
a=int(input("Enter the value"))
b=int(input("Enter the value"))
a,b=swap(a,b)

# reverse a number
def revnum(num):
    # num = int(input('ENter your number'))
    rem = 0
    quo = None
    l = []
    for i in range(len(num)):
        quo = num/10
        l.append(quo)
        rem = num//10
        num = rem
        print(l)
'''
# 16/10/2025
'''
friends = list()
print("Enter 5 friends name")
for i in range(5):
    name = input("Enter name")
    friends.append(name)
print(list(filter(lambda x: len(x)> 5, friends)))
'''

# Program 2 16102025
'''
a=[]
b=[]
l=int(input("Enter length for list"))
print("Enter first list number")

for i in range(l):
    x=int(input("Enter a number"))
    a.append(x)
print("Enter second number")
for i in range(l):
    y=int(input("Enter a number"))
    b.append(y)
print('First list',a)
print('Second list',b)
c=list(map(lambda x,y:x+y,a,b))
print('Sum of two list')
print (c)
'''

'''
 #Program 3   
sentence=input("Enter a senctence::")
print(sentence.upper().split())
'''
# Program 4
def prime(num):
    factor = 0
    for i in range(1,num+1):
        if num%i == 0:
            factor += 1
    if factor==2:
        print("Number is prime.")
    else:
        print("Number is not prime.")