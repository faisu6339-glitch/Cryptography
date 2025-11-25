# Function Arguments

def func(name):
    print("Hello, " + name + "!")
func("Aaliya")

#2. Multiple Arguments
def func(fname, lname):
    print("Hello, " + fname + " " + lname + "!")
func("Aaliya", "Aaliya")

# add
def add(a, b):
    return a + b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The sum is:", add(a, b))

#3. Calculator
def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return "Invalid operation"
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")
result = calculator(num1, num2, operation)
print("The result is:", result)

#4. factorial
def factorial(n):
    fact=1
    for i in range(1, n + 1):
        fact *= i
    return fact
n = int(input("Enter a number: "))
print("The factorial is:", factorial(n))

#5.Even or Odd
def evenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
print("The number is:", evenOdd(num))

#6. Prime Number
def isPrime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                return "Not Prime"
        return "Prime"
    else:
        return "Not Prime"
num = int(input("Enter a number: "))
print("The number is:", isPrime(num))

#7. Fibonacci Series
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a, end=' ')
        a,b=b,a+b
n = int(input("Enter the number of terms: "))
fibonacci(n)

#8. Palindrome Check
def is_palindrome(word):
    word = word.lower()
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is Palindrome")
else:
    print(f"{word} is not Palindrome")

#9. Armstrong Number
def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return sum == num
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

#10. Perfect Number
def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num
num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")

#11. Square Root
def square_root(num):
    return num ** 0.5
num = int(input("Enter a number: "))
print("The square root is:", square_root(num))




#12.Roots of Quadratic Equation
import cmath   # cmath handles complex numbers

def find_roots(a, b, c):
    # calculate the discriminant
    D = (b**2) - (4*a*c)

    # find two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(D)) / (2*a)
    root2 = (-b - cmath.sqrt(D)) / (2*a)

    return root1, root2


# --- Main Program ---
print("Quadratic Equation: ax² + bx + c = 0")

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

r1, r2 = find_roots(a, b, c)

print(f"The roots of {a}x² + {b}x + {c} = 0 are:")
print(f"Root 1 = {r1}")
print(f"Root 2 = {r2}")


#LCM
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The LCM is:", lcm(num1, num2))

#GCD
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The GCD is:", gcd(num1, num2))

#Function with Default Argument
def greet(name="Guest"):
    print("Hello, " + name + "!")
greet()
greet("Aaliya")
