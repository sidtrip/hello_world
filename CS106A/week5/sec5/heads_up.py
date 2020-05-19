import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def main():
    # read the file
    words_list = load_data()
    # chosse a random word
    while True:
        #wait fo input
        input('Press enter for next word: ')
        #choose random number
        choice = random.choice(words_list)
        #display it to user
        print(choice)

def load_data():    
    file = open('cswords.txt')
    words = [] 
    for line in file:
        word = line.strip()
        words.append(line)
    return words

if __name__ == '__main__':
    main()
