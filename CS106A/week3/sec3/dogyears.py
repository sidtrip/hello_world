def convert_to_dog_years(human_age):
    dog_age = human_age * 7
    return dog_age


def main():
    human_age = float(input('Enter human age: '))
    dog_age = convert_to_dog_years(human_age)
    print('Dog age is: ', dog_age)


if __name__ == '__main__':
    main()
