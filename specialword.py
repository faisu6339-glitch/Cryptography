word=input("Enter any word:").lower()
l=len(word)
fl=word[0]
ll=word[l-1]
if fl==ll:
    print(word,'is special word')
else:
    print(word,'is not special word')