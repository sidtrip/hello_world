def main():
    print("Enter a sequence of non-decreasing numbers.")
    last_num= float(input("Enter num: "))
    curr_num = float(input("Enter num: "))
    count = 1
    while curr_num >= last_num:
        count += 1
        last_num = curr_num
        curr_num = float(input("Enter num: "))
    print("Thanks for playing!")
    print("Sequence length: ", count)



if __name__ == "__main__":
    main()
