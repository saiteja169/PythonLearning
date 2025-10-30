sentence = input("enter a sentence")
vow = 0
cons = 0
vowels = "aeiou"
consonants ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for char in sentence.lower():
    if char in vowels:
        vow += 1
    elif char in consonants:
        cons +=1
print("number os vowels is ",vow)
print("number of consonants is",cons)
