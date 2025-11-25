print("Area of triangle")
base=int(input("Enter base"))
height=int(input("Enter height"))
if base >0 and height >0 :
    global area
    area = ((base*height)*1/2)
else:
     print("Enter proper data")
print("Area of triangle",area)