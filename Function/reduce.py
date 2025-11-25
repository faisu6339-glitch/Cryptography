from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
# Output: 15

# Explanation:
# The reduce function takes a binary function (in this case, a lambda that adds two numbers
# together) and applies it cumulatively to the items of the iterable (the list of numbers),
# from left to right, reducing the iterable to a single value (the sum of the numbers
# in this case).

# Using reduce to find the maximum value in a list
nums=[3, 1, 4, 1, 5, 9, 2, 6, 5]
max_value = reduce(lambda x, y: x if x > y else y, nums)
print(max_value)
# Output: 9

# Using reduce to concatenate a list of strings
strings = ["Hello", " ", "World", "!"]
concatenated = reduce(lambda x, y: x + y, strings)
print(concatenated)
# Output: Hello World!

# Using reduce with an initial value
numbers = [1, 2, 3]
product = reduce(lambda x, y: x * y, numbers, 10)
print(product)
# Output: 60

# Using reduce to flatten a list of lists
list_of_lists = [[1, 2], [3, 4], [5]]
flattened = reduce(lambda x, y: x + y, list_of_lists)
print(flattened)
# Output: [1, 2, 3, 4, 5]

# Using reduce to count occurrences of elements in a list
from functools import reduce

# List of elements
elements = ['a', 'b', 'a', 'c', 'b', 'a', 'd', 'd', 'q', 'a', 'p']

# Use reduce to count occurrences
count = reduce(lambda acc, x: {**acc, x: acc.get(x, 0) + 1}, elements, {})

print(count)
# Output: {'a': 4, 'b': 2, 'c': 1, 'd': 2, 'q': 1, 'p': 1}
# Explanation:
# The reduce function takes a lambda that updates a dictionary (accumulator) with the count
# of each element (x) in the list. The initial value is an empty dictionary {}
# and for each element in the list, it increments its count in the dictionary.


# Using reduce to implement factorial
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
print(factorial(5))
# Output: 120

# Using reduce to create a string from a list of characters
chars = ['H', 'e', 'l', 'l', 'o']
word = reduce(lambda x, y: x + y, chars)
print(word)
# Output: Hello

# Using reduce to find the longest string in a list
strings = ["apple", "banana", "cherry", "date"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, strings)
print(longest)
# Output: banana

# COMBINING MAP, FILTER, REDUCE
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Step 1: Use map to square each number
squared = map(lambda x: x * x, numbers)

# Step 2: Use filter to keep only even squares
even_squares = filter(lambda x: x % 2 == 0, squared)

# Step 3: Use reduce to sum the even squares
sum_even_squares = reduce(lambda x, y: x + y, even_squares)

print(sum_even_squares)
# Output: 220


#Find Average of Positive Numbers
nums = [-10, 2, -3, 4, 5, -6, 7, 8, -9, 10]
positive_nums = list(filter(lambda x: x > 0, nums))

sum_positive = reduce(lambda x, y: x + y, positive_nums, 0)

average_positive = sum_positive / len(positive_nums) if positive_nums else 0

print(average_positive)
# Output: 6.0

#Process Student Marks
students = [
    {"name": "Faisal", "marks": 70},
    {"name": "Aliya", "marks": 85},
    {"name": "Noor", "marks": 40},
    {"name": "Sara", "marks": 90}
]

passed = list(filter(lambda s: s["marks"] >= 50, students))
names = list(map(lambda s: s["name"], passed))
avg_marks = reduce(lambda a, b: a + b["marks"], passed, 0) / len(passed)

print("Passed Students:", names)
print("Average Marks:", avg_marks)
# Output:
# Passed Students: ['Faisal', 'Aliya', 'Sara']
# Average Marks: 81.66666666666667


# Using reduce with dictionaries to merge multiple dictionaries
dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5}]
merged_dict = reduce(lambda x, y: {**x, **y}, dicts)
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# 1️⃣ MAP → “Transform Every Item”
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)
# Output: [1, 4, 9, 16, 25]

# 2️⃣ FILTER → “Select Items Based on Condition”
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4]

# 3️⃣ REDUCE → “Aggregate Items to Single Value”
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
# Output: 15

#Combine All Items into One Result”

#reduce() applies a function cumulatively to combine all elements into a single value
numbers = [1, 2, 3, 4, 5]
sum_of_squares_of_even = reduce(lambda acc, x: acc + x ** 2,numbers, 0)
print(sum_of_squares_of_even)
# Output: 220
