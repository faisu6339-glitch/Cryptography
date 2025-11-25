# Question 1
n=int(input("Enter n number"))
s=0
for x in range(1,n+1):
    if x %2 !=0:
        s=s+x
print("Sum oF n odd=",s)

# question 2
a=int(input("Enter a no."))
b=0
for i in range(1,a//2+1):
    if a%i==0:
        b=b+i
if a==b:
    print(a,"is a perfect No.")
else:
    print(a,"is not a perfect No.")

# Question 3
