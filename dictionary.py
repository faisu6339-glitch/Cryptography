# create a Dictionary

d1={'a': 1, 'b': 2, 'c': 3}
print(d1)

d2=dict(a="faisul", b="khan", c="python")
print(d2)

#Accessing Dictionary Items
d = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))

#Adding Items to a Dictionary
d={1:'faisal',2:'Aaliya',3:'Shadmani'}
d[4]='Ummehani'
print(d)

#Removing Dictionary Items

#adding ages
d1 = {1:'faisal', 2:'Aaliya', 3:'Shadmani'}
age = {1:'21', 2:'23', 3:'25'}

data = {}

for key in d1:
    if key in age:
        data[key] = [d1[key], age[key]]

print(data)

#Adding and Updating Dictionary Items
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

#Removing Dictionary Items
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)