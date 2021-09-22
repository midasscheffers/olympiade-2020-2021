

wrd = input()

letters = []
for letter in wrd:
    if letter not in letters:
        letters.append(letter)

print(len(letters))