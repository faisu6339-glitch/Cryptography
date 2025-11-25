'''
num=int(input("Enter number"))

#Check whether the number is less than 2 if yes then it is not prime
flag = False
if num <2:
    print("This is not prime")
else:
    for i in range(2,num):
        if(num% i)==0:
            flag = True
            break
if flag:
    print('Number is not prime.')
else:
    print("Number is prime.")
'''

# prime number between 2 numbers
lower = int(input('Enter first number'))
upper = int(input("Enter upper number"))

for num in range(lower, upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)