sentence = input("enter a string")
freq = {}
for char in sentence:
    if char in freq:
        freq[char]+=1
    else:
        freq[char] = 1
print("character frequnecies" )
for key, value in freq.items():
    print(f"{key} : {value}")
