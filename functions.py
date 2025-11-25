#Defining a Function
def fun():
    print("Welcome to GFG")

#Calling a Function
    def fun():
     print("Welcome to GFG")
    
fun()

#Function Arguments
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

# Default Arguments
def myfunc(x,y=90):
    print(f"X :{x}")
    print("y:",y)
myfunc(20)

# Keyword Arguments
def myfun(fname,lname):
    print(fname,lname)

studnet(fname='Aaliya', lname='Fatma')
student(lname
