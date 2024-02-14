###########################################
# Author: Keidy Lopez
# Filename: problem #7.py
# Description: program that creates carddeck.txt, reads it , and prints a random card from it
###########################################
import random

def main():
    # prints put welcome statement, creates, opens the file, and displays random card
    print('\n','This program will generate a file that contains all the members of a deck of playing cards (without jokers)'
          'on card per line.','\n')
    fileCreation()
    print('\n','Your file called cardDeck.txt has been successfully created!')
    print('Reading the card file.....................................................','\n')
    fileReading()

def fileCreation():
    # main lists
    suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    # opens/creates carddeck.txt and writes cards in it
    with open('carddeck.txt', 'w') as outfile:
        for cardClass in range(len(suits)):   # nested for loops that add card csv to carddeck.txt, and prints what its creating
            if cardClass == 0:
                print('Creating the CLUBS suit...')
            elif cardClass == 1:
                print('Creating the DIAMONDS suit...')
            elif cardClass == 2:
                print('Creating the HEARTS suit...')
            elif cardClass == 3:
                print('Creating the SPADES suit...')
            for i in range(len(values)):
                outfile.write(values[i])
                outfile.write(',')
                outfile.write(suits[cardClass])
                outfile.write('\n')

def fileReading():
    # main list
    card_list = []

    # opens, reads, and separates cvs and adds them to main list
    with open('carddeck.txt', 'r') as infile:
        for line in infile:
            lines = line.strip().split(',')
            card_list.append(lines[0])
            card_list.append(lines[1])

    # prints random card
    print('I\'ll deal you a random card')
    for i in range(1):
        num = random.randrange(0,len(card_list),2)
        print('Your card is: ', card_list[num], card_list[num+1])


if __name__ == "__main__":
    main()
