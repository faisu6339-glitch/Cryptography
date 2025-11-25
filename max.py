def maxthree(a,b,c=100):
    m=0
    if a > b and a>c:
        m=a
    else:
        if b>c:
            m=b
        else:
            m=c
    return(a,b,c,m)
x=int(input("Enter first Number::"))
y=int(input("Enter first Number::"))
z=int(input("Enter first Number::"))

p,q,r, max3=maxthree(x,y)
print("First No:")