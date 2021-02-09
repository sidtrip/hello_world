n = 0
bow = ['a', 'e', 'i', 'o', 'u']
for i in s:
    if i in bow:
        n += 1
print("number of vowels: " + str(n))
