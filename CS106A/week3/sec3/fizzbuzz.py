def main():
    print('Fizz buzz!')
    n = int(input("Enter the number upto, count: "))
    count = fizzbuzz(n)
    print("We fizzed/buzzed/fizzbuzzed " + str(count) + " number of times.")    
def fizzbuzz(n):
    fizzbuzz_counter = 0
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            fizzbuzz_counter += 1
        elif i % 3 == 0:
            print("fizz")
            fizzbuzz_counter += 1
        elif i % 5 == 0:
            print("buzz")
            fizzbuzz_counter += 1
        else:
            print(i)

    return fizzbuzz_counter


if __name__ == '__main__':
    main()
