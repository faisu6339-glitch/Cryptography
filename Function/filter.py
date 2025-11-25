a=[1,2,3,4,5]
b=filter(lambda x:x%2==0,a)
print(list(b))
# Output: [2, 4]

a=['apple','banana','cherry','date']
b=filter(lambda x: len(x) > 5, a)
print(list(b))
# Output: ['banana', 'cherry']

#prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = range(1, 21)
primes = filter(is_prime, numbers)
print(list(primes))
# Output: [2, 3, 5, 7, 11, 13, 17, 19]

#strings that start with 'a'
def starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(starts_a, li)
print(list(res))
# Output: ['apple', 'avocado', 'apricot']

def funceven(n):
    return n%2==0
lst=[10,21,4,45,66,93,11,83,22]
even_nos=filter(funceven,lst)
print(list(even_nos))
# Output: [10, 4, 66, 22]

#Filtering and Transforming Data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data = filter(lambda x: x % 2 == 0, data)
squared_data = map(lambda x: x ** 2, filtered_data)
print(list(squared_data))
# Output: [4, 16, 36, 64, 100]

# filter names starting with 'a'
names=['faisal','aaliya','shadmani','ummehani','zainab']
a_names=filter(lambda name:name.startswith('a'),names)
print(list(a_names))
# Output: ['aaliya']

# filter positive numbers from a list
num=[-10,15,-20,25,-30,35]
positive=filter(lambda x:x>0,num)
print(list(positive))
# Output: [15, 25, 35]

strings=["faisal",'aaliya'," ",'shadmani','ummehani','zainab', "",""," "]
non_empty=list(filter(None,strings))
print(non_empty)
# Output: ['faisal', 'aaliya', 'shadmani', 'ummehani', 'zainab']

#filtering palimdromes
words = ["madam", "noon", "python", "level", "world"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)
# ['madam', 'noon', 'level']

#filter strings only from mixed list
input=['aaliya',True,45,'shadmani',False,78.9,'ummehani',0,'zainab',None]
strings_only=list(filter(lambda x: isinstance(x,str),input))
print(strings_only)
# Output: ['aaliya', 'shadmani', 'ummehani', 'zainab']