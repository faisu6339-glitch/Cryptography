x = int(input('Enter a number'))
y = int(input("Enter another number."))
z = int(input("Enter thired number."))
if x > y and x > z:
    print(f"{x} is greatest.")
elif y>x and y > z:
    print(f"{y} is greatest.")
else:
    print(f"{z} is greatest.")
    
