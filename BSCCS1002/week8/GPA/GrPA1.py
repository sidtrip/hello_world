def reverse(L):
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        nu = L.pop()
        return [nu] + reverse(L)


