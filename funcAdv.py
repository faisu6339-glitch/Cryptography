l1=[]
ch='Y'
while True:
    if ch=='Y':
        x=int(input("Enter any no:"))
        l1.append(x)
        ch=input('Do you want to next(Y/N?').upper()
    else:
        break
print("List of taken numbbers",l1)
sqrt_list=list(map(lambda x:x**2,l1))
print("list of square of taken Numbers:",sqrt_list)

l1=[]
ch='Y'
while True:
    if ch=='Y':
        x=int(input("Enter any no:"))
        l1.append(x)
        ch=input('Do you want to next(Y/N?').upper()
    else:
        break
print("List of taken numbbers",l1)
evenodd_list=list(map(lambda x:x%2==0,l1))
print("list of square of taken Numbers:",evenodd_list)

l1=[]
ch='Y'
while True:
    if ch=='Y':
        x=int(input("Enter any no:"))
        l1.append(x)
        ch=input('Do you want to next(Y/N?').upper()
    else:
        break
print("List of taken numbbers",l1)
evenodd_list=list(filter(lambda x:x%2==0,l1))
print("list of square of taken Numbers:",evenodd_list)

l1 = []
ch = 'Y'

while True:
    if ch == 'Y':
        x = int(input("Enter any number: "))
        l1.append(x)
        ch = input("Do you want to continue (Y/N)? ").upper()
    else:
        break

print("List of taken numbers:", l1)

# Use filter() to get even and odd numbers
even_list = list(filter(lambda x: x % 2 == 0, l1))
odd_list = list(filter(lambda x: x % 2 != 0, l1))

print("List of even numbers:", even_list)
print("List of odd numbers:", odd_list)


a=int(input("Enter first number"))
b=int(input("Enter Second number"))
c=int(input("Enter third number"))

max3=lambda a,b,c:a if a>b and a>c else b if b>c else c
print("Maximum No=",max3)