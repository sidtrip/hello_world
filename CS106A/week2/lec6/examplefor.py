"""
File: examplefor.py
------------------
Print the first 100 even numbers
"""

def main():
    for i in range(2, 201, 2):
        print(i)

    """
    for i in range(101):
        print(i*2)
    """
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
