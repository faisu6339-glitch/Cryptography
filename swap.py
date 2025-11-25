def swap(a,b):
  a,b=b,a
  print(a={a},b={b})

  return a,b
a=int(input("Enter the value"))
b=int(input("Enter the value"))
a,b=swap(a,b)
print(a={a},b={b})
