###########################################
# Author: Keidy Lopez
# Filename: problem #2.py
# Description: gives the sum of the five number previously in the number.txt file
###########################################

def main():
    # open number.txt and reads its content
    with open('numbers.txt', 'r') as nums:
        Mylist = nums.readlines()

    # strips the carriage return of list of numbers read
    for i in range(len(Mylist)):
        Mylist[i] = int(Mylist[i].strip('\n'))

    # main accumulator variable and for loop that adds five numbers together
    counter = 0
    for i in range(len(Mylist)):
        counter += Mylist[i]

    # prints out sum total
    print('the sum of your five numbers is: '+str(counter))



if __name__ == "__main__":
    main()
