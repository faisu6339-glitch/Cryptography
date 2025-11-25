s1="crush"
s2="Hania Amair"
print(s1.capitalize())
print(s2.capitalize())

# Accessing characters in a string
s="programming"
print(s[0])  # First character
print(s[1])  # Second character
print(s[2])  # Third character

print(s[-1]) # Last character
print(s[-2]) # Second last character

# Slicing strings
s="programming"
print(s[0:3])   # First three characters
print(s[3:6])   # Characters from index 3 to 5
print(s[:4])    # First four characters
print(s[4:])    # From index 4 to the end
print(s[:])     # Entire string

#reverse a string
s="programming"
print(s[::-1])  # Reversed string

#palindrome check
s="madam"
if s.lower() == s[::-1].lower():
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

#count occurrences of a character
sentence="Python is a programming language. Python is popular."
words=sentence.lower().split()
count=words.count("python")
print(f"Occurrences of 'python': {count}")
count={w:words.count(w) for w in set(words)}
print("Word occurrences:", count)

#find substring
s="programming in python"
index=s.find("python")
print(f"Index of 'python': {index}")
index=s.find("java")
print(f"Index of 'java': {index}")  # -1 if not found

#replace substring
s="I love programming. Programming is fun."
new_s=s.replace("programming","coding").replace("Programming","Coding")
print(new_s)

#split string
s="apple,banana,cherry"
fruits=s.split(",")
print(fruits)

#join strings
words=["Hello","world","from","Python"]
sentence=" ".join(words)
print(sentence)

#strip whitespace
s="   Hello, World!   "
print(s.strip())  # Remove leading and trailing whitespace
print(s.lstrip()) # Remove leading whitespace
print(s.rstrip())# Remove trailing whitespace

#string length
s="Hello, World!"
print(len(s))  # Length of the string

#string formatting
name="Alice"
age=30
formatted_string=f"My name is {name} and I am {age} years old."
print(formatted_string)


# Convert cases
s="Hello, World!"
print(s.upper())  # Convert to uppercase
print(s.lower())  # Convert to lowercase
print(s.title())  # Convert to title case


# Check string start and end
s="Hello, World!"
print(s.startswith("Hello"))  # Check if string starts with "Hello"
print(s.endswith("World!"))   # Check if string ends with "World!"

# Count occurrences of a substring
s="banana"
print(s.count("a"))  # Count occurrences of 'a'
print(s.count("na")) # Count occurrences of 'na'

# Find substring index
s="Hello, World!"
print(s.index("World"))  # Find index of 'World'

# Note: index() raises ValueError if substring not found

# Check if string is alphanumeric
s="Hello123"
print(s.isalnum())  # Check if string is alphanumeric

#reverse each words in a sentence
sentence="Hello World from Python"
reversed_sentence=' '.join(word[::-1] for word in sentence.split())
print(reversed_sentence)

# Count vowels and consonants in a string
s="Hello World"
vowels="aeiouAEIOU"
vowel_count=sum(1 for char in s if char in vowels)
consonant_count=sum(1 for char in s if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
