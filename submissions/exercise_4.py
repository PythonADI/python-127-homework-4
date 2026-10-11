word = str(input("Enter word: ").strip().lower())
vowels = 0
for letter in word:
   if letter in "aeiou":
      vowels += 1
print(f"Vowels: {vowels}")
