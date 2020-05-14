from math import sqrt

"""
This program is supposed to prompt users for 3 coefficients
of a quadratic equation, and then calculate for it's solution
"""
def main():
    print("Welcome to Quadratic equation solver!")
    print("This program solves equations of the form Axˆ2 + Bx + C = 0")
    a = float(input("Enter the coefficient of A: "))
    b = float(input("Enter the coefficient of B: "))
    c = float(input("Enter the coefficient of C: "))
    print("The roots of " + str(a) + " xˆ2 + " + str(b) + " x + " + str(c) + " = 0" + " are: ")

    d = b * b - 4 * a * c
    is_d_neg = False
    if d < 0:
        d = -1 * d
        is_d_neg = True


    first_half = -b / (2 * a)
    second_half = sqrt(d) / (2 * a)

    if is_d_neg:
        print('x1 = ' + str(first_half) + ' + i' + str(second_half))
        print('x2 = ' + str(first_half) + ' - i' + str(second_half))

    else:
        print('x1 = ' + str(first_half + second_half))
        print('x2 = ' + str(first_half - second_half))


if __name__ == '__main__':
    main()