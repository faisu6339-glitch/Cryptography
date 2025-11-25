import math as m
def solution_quadratic(a=1,b=0,c=-4):
    result = ''
    d = b**2 - 4*a*c
    if d>0:
        x1 = (-b+m.sqrt(d))/(2*a)
        x2 = (-b-m.sqrt(d))/(2*a)
        result = 'Differnt roots ' + str(x1) + ','+ str(x2)
    elif d==0:
        x1 = (-b+m.sqrt(d))/(2*a)
        result = 'Roots are equal ' + str(x1)
    else:
        result = 'Imaginary Roots'
    return(a,b,c,result)

a = int(input('enter coefficient of x**2:'))
b = int(input('enter coefficient of x :'))
c = int(input('enter constant'))

a,b,c,result = solution_quadratic(a,b,c)
print(result)
#a,b,c,result = solution_quadratic()
#print(result)