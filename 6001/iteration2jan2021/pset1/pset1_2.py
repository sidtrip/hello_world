softc = 0
hardc = 0
for i in s:
    if i == 'b' and softc == 2:
        hardc += 1
        softc = 1
        continue
    if i == 'b':
        softc = 0
        softc += 1
        continue
    if i == 'o' and softc == 1:
        softc += 1
        continue

    
    softc = 0
    
print("Number of times bob occurs is: " + str(hardc))
