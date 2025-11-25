word = input("Enter a word: ").lower()
is_palindrome = True

for i in range(len(word)//2):
    if word[i] != word[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{word} is Palindrome")
else:
    print(f"{word} is not Palindrome")
