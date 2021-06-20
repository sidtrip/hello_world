"""

"""

#First input is the number of rows in the matrix,
#While the second one is the number of columns
rows = int(input())
columns = int(input())

listing = []

#Taking input for elements of the matrix
for i in range(rows):
    line = input()
    listing.append(line.split())

#Working on the asked processing    
for row in range(rows):
    line = ''
    for column in range(columns):
        if row != 0 and column != 0:
            if row != (rows-1) and column != (columns-1):
                listing[row][column] = '0'
        line += listing[row][column]
        if column != (columns -1):
            line += ' '
    print(line)
