def collatz_repeat(n, op_count = 0):
    operand = n
    if operand == 1:
        return(op_count)
    elif operand % 2 == 0:
        n = collatz_repeat(n/2, op_count+1)
        return n
    else:
        n = collatz_repeat(3*n +1, op_count+1)
        return n
