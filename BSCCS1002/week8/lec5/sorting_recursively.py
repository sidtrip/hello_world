def mini(l):
#this function finds the minimum element in a list and returns it.
    small = l[0]

    for item in l:
        if item < small:
            small = item
    return small

def sort(l):
    
    if len(l) == 0 or len(l) == 1:
        return l

    m = mini(l)
    l.remove(m)
    sorted_list = [m] + sort(l)
    return sorted_list

l = [5,3, 74, 2, 37, 94, 21,9, 4, 36]

print(sort(l))




