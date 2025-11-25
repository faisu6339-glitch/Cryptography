Salary=int(input("Enter Your Salary: "))
age = int(input("Enter Your Age: "))
CreditScore = int(input("Enter Your CreditScore: "))

print(f"Your Salary is {Salary}")
print(f"Your Age is {age}")
print(f"Your Credit Score is {CreditScore}")




if Salary > 110000 & age >= 26 & CreditScore <= 720 :
  print(f"You Have to increase your credit Score (Credit Score should be >= 800)")
elif Salary <= 80000 & age <= 17 & CreditScore <=600 :
  print(f"Increase your age munna")
elif Salary == 100000 & age >= 18 & CreditScore >=800 :
  print(f"You are eligible for loan")
else:
  print(f"Time kharba mt karo!")
