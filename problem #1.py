###########################################
# Author: Keidy Lopez
# Filename: problem #1.py
# Description: Adds five numbers to a text file
###########################################

def main():
    # welcome statement
    print('please enter 5 numbers and ill save them in a text file')

    # list variable
    number_list = []

    # for loop that takes input from the user, adds a carriage return to the end of the input, and adds it to a list
    for i in range(1,6):
        num1 = input('number('+ str(i)+ '): ')
        num2 = num1 + '\n'
        number_list.append(num2)

    # adds list of numbers + carriage return to number.txt
    with open('numbers.txt', 'w') as number_file:
        number_file.writelines(number_list)



if __name__=="__main__":
    main()
