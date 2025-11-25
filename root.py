"""WAP to compute roots of quadratic equation using parameterised function, parameter as a,b,c of quadratic function. """
import math as m
def quadratic(a=1,b=0,c= -4):
    D = m.sqrt((b**2) - (4*a*c))
    #return (((b+D)/(2*a)), ((b-D)/(2*a)))
    if D < 0:
        print("No Solution")
    elif D>0:
        print("Roots are Unique and Real")
        print((((-b+D)/(2*a)), ((-b-D)/(2*a))))
    elif D==0:
        print('Roots are equal.')
        print((((-b+D)/(2*a)), ((-b-D)/(2*a))))
