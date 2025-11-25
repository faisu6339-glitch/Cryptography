a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)  # Output: [1, 2, 3, 4, 5, 6]

a1=[1,2,3]
b1=['a','b','c']
c1=[1,'a',2,'b',3,'c']
print(c1)  # Output: [1, 'a', 2, 'b', 3, 'c']
print(a1) # Output: [1, 2, 3]
print(b1) # Output: ['a', 'b', 'c']

#using list constructor
list1=list((1,2,3,4))
print(list1)  # Output: [1, 2, 3, 4]

a2=list(('python','java','c++'))
print(a2)  # Output: ['python', 'java', 'c++']
b=list("Aaliya")
print(b)  # Output: ['A', 'a', 'l', 'i', 'y', 'a']

# Accessing elements in a list
fruits=['apple','banana','cherry','date']
print(fruits[0])  # Output: 'apple'
print(fruits[1])  # Output: 'banana'
print(fruits[2])  # Output: 'cherry'
print(fruits[3])  # Output: 'date'
print(fruits[-1]) # Output: 'date'
print(fruits[-2]) # Output: 'cherry'

#creating list with repeated elements
zeros=[0]*5
print(zeros)  # Output: [0, 0, 0, 0, 0]
nines=[9]*3
print(nines)  # Output: [9, 9, 9]
chars=['a']*4
print(chars)  # Output: ['a', 'a', 'a', 'a']

# Slicing lists
numbers=[10,20,30,40,50,60,70]
print(numbers[0:3])   # Output: [10, 20, 30]
print(numbers[3:6])   # Output: [40, 50, 60]
print(numbers[:4])    # Output: [10, 20, 30, 40]
print(numbers[4:])    # Output: [50, 60, 70]
print(numbers[:])     # Output: [10, 20, 30, 40, 50, 60, 70]

#reverse a list
print(numbers[::-1])  # Output: [70, 60, 50, 40, 30, 20, 10]

#check if list is palindrome
lst=[1,2,3,2,1]
if lst == lst[::-1]:
    print(f"{lst} is a palindrome")
else:
    print(f"{lst} is not a palindrome")

#count occurrences of an element
colors=['red','blue','green','blue','yellow','blue']
count_blue=colors.count('blue')
print(f"Occurrences of 'blue': {count_blue}")

#find index of an element
index_green=colors.index('green')
print(f"Index of 'green': {index_green}")  # Output: 2


# update and modify list elements
elements=[10,20,30,40,50]
elements[2]=35
print(elements)  # Output: [10, 20, 35, 40, 50]
elements[0:2]=[15,25]
print(elements)  # Output: [15, 25, 35, 40, 50]

# append and extend lists
num=[1,2,'apple',3.5,True,None]
num.append('banana')
print(num)  # Output: [1, 2, 'apple', 3.5, True, None, 'banana']
num.extend([4,5,'cherry'])
print(num)  # Output: [1, 2, 'apple', 3.5, True, None, 'banana', 4, 5, 'cherry']

# insert elements at specific positions
letters=['a','b','d','e']
letters.insert(2,'c')
print(letters)  # Output: ['a', 'b', 'c', 'd', 'e']

# remove elements from list
fruits=['apple','banana','cherry','date','banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'date', 'banana']
fruits.pop(2)
print(fruits)  # Output: ['apple', 'cherry', 'banana']
fruits.pop()
print(fruits)  # Output: ['apple', 'cherry']

# clear the entire list
fruits.clear()
print(fruits)  # Output: []

# sort and reverse lists
numbers=[50,20,40,10,30]
numbers.sort()
print(numbers)  # Output: [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)  # Output: [50, 40, 30, 20, 10]


# copy a list
original=[1,2,3,4,5]
copy_list=original.copy()
print(copy_list)  # Output: [1, 2, 3, 4, 5]

# nested lists
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])      # Output: [1, 2, 3]
print(matrix[1][2])   # Output: 6
print(matrix[2][0])   # Output: 7
print(matrix)        # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


#🔁 7️⃣ Loop Through Lists
numbers=[10,20,30,40,50]
for num in numbers:
    print(num)
# Output:
#10
#20
#30
#40
#50
# Using range() to loop through list indices
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")
# Output:
#Index 0: 10
#Index 1: 20

# Using enumerate() to get index and value
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")
# Output:
#Index 0: 10

# List comprehensions
squared=[x**2 for x in numbers]
print(squared)  # Output: [100, 400, 900, 1600, 2500]
# Filtering with list comprehensions
even_numbers=[x for x in numbers if x%2==0]
print(even_numbers)  # Output: [10, 20, 30, 40, 50]
# Nested loops with list comprehensions


#even odd
nums=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for n in nums:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
print("Even numbers:", even)  # Output: Even numbers: [2, 4, 6, 8, 10]
print("Odd numbers:", odd)    # Output: Odd numbers: [1, 3, 5, 7, 9]

# Finding maximum and minimum in a list
numbers = [12, 45, 67, 23, 90, 11, 56]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
# Output:
#Largest: 90
#Smallest: 11

#Count positive and negative numbers in a list
nums = [10, -5, 3, -1, 0, 7, -8, 2]
pos=neg=zero=0

for n in nums:
    if n>0:
        pos+=1
    elif n<0:
        neg+=1
    else:
        zero+=1
print("Positive numbers:", pos)
print("Negative numbers:", neg)
print("Zeroes:", zero)

#remove all negative numbers from a list
numbers = [10, -5, 3, -1, 0, 7, -8, 2]
positive=[]

for n in numbers:
    if n>=0:
        positive.append(n)
print("List after removing negative numbers:", positive)  # Output: [10, 3, 0, 7, 2]

# Generate a list of squares of even numbers from another list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for num in numbers:
    if num % 2 == 0:
        squares.append(num ** 2)

print("Squares of even numbers:", squares)


#⚙️ 1. Find sum, average, and length of list
numbers = [12, 45, 67, 23, 90, 11, 56]

total = sum(numbers)
avg = total / len(numbers)

print("Sum:", total)
print("Average:", avg)
print("Total elements:", len(numbers))


#. Merge two lists and remove duplicates
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged = list1 + list2
unique = list(set(merged))

print("Merged list:", merged)
print("Unique list:", unique)

#6. Check if an element exists in list

colors = ["red", "green", "blue", "yellow"]
check = input("Enter a color: ")

if check in colors:
    print(check, "is present in the list.")
else:
    print(check, "is not in the list.")
