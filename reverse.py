sen=input("Enter a sentence:").lower()
sen+=' '
l=len(sen)
w=''
i=0
listword=[]
while i < l:
    if sen[i]!=' ':
        w+=sen[i]
    else:
        listword.append(w)
        w=''
    i=i+1
print(listword)
l1=len(listword)
j=(l1-1)
while j>=0:
    print(listword[j],end=' ')
    j-=1
