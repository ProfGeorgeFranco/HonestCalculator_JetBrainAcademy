vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

word = input()

for char in word:
    if not char.isalpha():
        break

    elif char in vowels:
        print("vowel")

    else:
        print("consonant")
