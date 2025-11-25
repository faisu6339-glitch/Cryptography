Unit = int(input("Enter Your Unit: "))
FreeUnit = 125 
Amount = 0
Slab1 = 4.75
Slab2 = 5.50
Slab3 = 7.50
if Unit == FreeUnit  & Unit <=125:
  print(f"You dont have to pay any amount!")
elif Unit <=225 :
  print(f"bill is : {(Unit - FreeUnit)*Slab1}")
elif Unit <=425 :
  print(f"bill is : {(Unit - FreeUnit)*Slab2}")
else :
  print(f"bill is : {(Unit - FreeUnit)*Slab3}")
if ((Unit - FreeUnit)*Slab1 >= 5000):
  print(f"Your Overlade charge is : {((Unit - FreeUnit)*Slab1)*104.5/100}")
elif ((Unit - FreeUnit)*Slab2 >= 5000):
  print(f"Your Overlade charge is : {((Unit - FreeUnit)*Slab2)*104.5/100}")
elif ((Unit - FreeUnit)*Slab3 >= 5000):
  print(f"Your Overlade charge is : {((Unit - FreeUnit)*Slab3)*104.5/100}")
else:
  print(f"Your Unit is :{Unit}")
bill=((Unit - FreeUnit)*Slab3)*104.5/100
if bill>5000:
  overload=bill*4.5/100
  print('Overload on bill :',overload)
