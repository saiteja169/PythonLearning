numbers = [1,5,7,8,9,6,3,1,4,9,6,2,5,7]
duplicates=[]
for i in numbers:
    if i not in duplicates:
        duplicates.append(i)
print(duplicates)
          