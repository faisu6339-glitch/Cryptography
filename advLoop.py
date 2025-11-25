#. Detect Prime Numbers in Range (with loop and flags)
def find_primes(n):
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')

find_primes(100)

#def find_primes(n):
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')

find_primes(100)

#Multiplication Table
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i*j:4}", end='')
        print()

multiplication_table(10)

#Fibonacci Series up to N Terms (with Loop)
def fibonacci(n):
    a, b = 0, 1
    print(a, b, end=' ')
    for _ in range(2, n):
        a, b = b, a + b
        print(b, end=' ')

fibonacci(10)
