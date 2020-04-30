import random

N_RANDS = 4

def random_average():
    """
    Generate 4 random numbers, printing them as we go, and then print their avgerage
    """

    total = 0
    for i in range(N_RANDS):
        r = random.randint(0, 10)
        total += r
        print(r)
    print("Average: " + str(total/N_RANDS))


def main():
    random_average()



if __name__ == '__main__':
    main()