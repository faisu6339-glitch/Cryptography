a=int(input("Enter any constant value for a: "))
n=int(input("Enter the number of terms: "))
s=1
f=1
i=1

while i<=n:
    j=i
    while j>0:
        f*=j
        j-=1
    
    s=s+((i+1)*a)/f
    f=1
    i+=1
print("The sum of the series is:",s)