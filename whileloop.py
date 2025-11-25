#basic
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

#break
n = 1
while True:
    print(n)
    if n == 3:
        break
    n += 1
#continue to Skip Iteration
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
    
#Loop with else
    x = 1
while x <= 3:
    print(x)
    x += 1
else:
    print("Loop completed.")

#Password Retry System
correct_password = "secret"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Wrong password.")
    attempts += 1
else:
    print("Too many failed attempts.")
