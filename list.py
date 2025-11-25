pn=list([])
p=list([])

for i in range(5):
   pn1=input("Enter product name")
   p1=float(input("Enter product price"))
   pn.append(pn1)
   p.append(p1)

s=0.0
print("product name ---------------------Price")
for i in range(5):
   print(pn[i],"---------------------",p[i])
   s=s+p[i]
print("Total price is",s)

# search
s = input("Enter product name to search")
if s in pn:
   print("Product found at index",pn.index(s))
else:
   print("Product not found.")