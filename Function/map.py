# Map Function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

# Using lambda with map
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print(cubed_numbers)
# Output: [1, 8, 27, 64, 125]

# Using map with multiple iterables
numbers2 = [10, 20, 30, 40, 50]
summed_numbers = list(map(lambda x, y: x + y, numbers, numbers2))
print(summed_numbers)
# Output: [11, 22, 33, 44, 55]

# Using map with strings
words = ["hello", "world", "python"]
uppercased_words = list(map(str.upper, words))
print(uppercased_words)

# Output: ['HELLO', 'WORLD', 'PYTHON']

# Using map to convert strings to integers
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)
# Output: [1, 2, 3, 4, 5]

#Multple iterables with map
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, list1, list2))
print(summed)

# Output: [5, 7, 9]

# Using map with a custom function
def to_uppercase(s):
    return s.upper()
strings = ["apple", "banana", "cherry"]
uppercased = list(map(to_uppercase, strings))
print(uppercased)

# Output: ['APPLE', 'BANANA', 'CHERRY']

# Using map with nested functions
def add_prefix(s):
    def prefixer(s):
        return "Prefix_" + s
    return prefixer(s)
strings = ["one", "two", "three"]
prefixed = list(map(add_prefix, strings))
print(prefixed)
# Output: ['Prefix_one', 'Prefix_two', 'Prefix_three']

# Using map with conditionals
def conditional_map(x):
    return x * 2 if x > 2 else x + 2
numbers = [1, 2, 3, 4, 5]
result = list(map(conditional_map, numbers))
print(result)
# Output: [3, 4, 6, 8, 10]

# Using map with filter-like behavior
def filter_map(x):
    return x if x % 2 == 0 else None
numbers = [1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x is not None, map(filter_map, numbers)))
print(filtered)
# Output: [2, 4]

# Using map with multiple functions
def add_one(x):
    return x + 1
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
functions = [add_one, square]
for func in functions:
    numbers = list(map(func, numbers))
print(numbers)
# Output: [4, 9, 16, 25, 36]

# Using map for unit conversion
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
print(fahrenheit)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# Using map with dictionaries
dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
names = list(map(lambda d: d['name'], dicts))
print(names)
# Output: ['Alice', 'Bob']


# Using map with sets
num_set = {1, 2, 3, 4, 5}
squared_set = set(map(lambda x: x * x, num_set))
print(squared_set)
# Output: {1, 4, 9, 16, 25}

# Using map with tuples
num_tuple = (1, 2, 3, 4, 5)
doubled_tuple = tuple(map(lambda x: x * 2, num_tuple))
print(doubled_tuple)
# Output: (2, 4, 6, 8, 10)

