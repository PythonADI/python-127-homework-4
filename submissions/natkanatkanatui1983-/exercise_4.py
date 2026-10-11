word = input("Enter a word :\n").lower()
count = 0
for letter in word:
    if letter in "aeiou":
        count = count + 1
    print("Vowels:",count)