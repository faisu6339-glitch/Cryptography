sen=input('Enter a sentence').lower()
l=len(sen)
sen=sen+' '
i=0
ccl=0

while i <l:
       if sen[i]==sen[i+1]:
              ccl+=1
       i+=1
       
print('Your sentence',sen)
print('Total No. Consecutive letters in sentence:',ccl)