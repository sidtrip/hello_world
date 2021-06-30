def binary_search(L, k):
    """ This function is an alternative for the obvious search. It does exactly what is expected form the obvious_search, but in an efficient way. This method is popularly called the binary search."""
    begin = 0 # first element in L. L[0]
    end = len(L)-1

    #Using a while loop to look at the list and keep halving it
    while(end-begin > 1):
        #we will handle the case when number of elements is less than or equal to 1         
        mid = (begin+end)//2
        
        if (L[mid] == k):
            return 1
        # if the middle element is greater than k, then cut the right side and retain the left side
        if (L[mid] > k):
            end = mid -1 
        
        if (L[mid] < k):
            begin = mid+1

    #This is outside the while loop
    #if it is equal to 1, then we have 2 elements
    if (L[begin] == k) or (L[end] == k):
        return 1
    else:
        return 0

 
