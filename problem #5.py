###########################################
# Author: Keidy Lopez
# Filename: problem #5.py
# Description: program that writes items(number and letter) into random.txt
###########################################
import random

def main():
    # welcome statement
    print('RANDOM ITEMS')
    print('Based on your input, this program will generate a file of random items.')
    num = int(input('How many items do you wish to generate? '))  # number of items that will be generated

    # tells user file is being opened
    print('Opening file random.txt...')
    with open('random.txt', 'w') as outfile:
        print('Writing random items...')  # tells user file is being written
        for i in range(num):     # for loop that writes items in random.txt the amount of times the user requested
            outfile.write(random_num())
            outfile.write(random_let())

    print('Closing file random.txt...')  # tell user file is closing

# function that that returns random number with carriage return
def random_num():
    num = random.randint(1,1000)
    num_string = str(num)+'\n'
    return num_string

# function that that returns random letter with carriage return
def random_let():
    let = random.randint(97,122)
    let_chr = chr(let) + '\n'
    return let_chr


if __name__ == "__main__":
    main()
