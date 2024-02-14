###########################################
# Author: Keidy Lopez
# Filename: problem #3.py
# Description: writes name, lastname, age, and gpa into a friends.txt
###########################################
import random

def main():
    # main list and condition for while loop
    myCondition = True
    names_list = []

    # while loop that takes name and last name as input and ads then to a list along with the age and gpa all separates
    # by commas, and a carriage return at the end
    while myCondition:
        name = input('please enter your friends first name(0 to quit): ')
        last_name = input('please enter your friends last name(0 to quit): ')
        if name != '0' or last_name != '0':
            name_line = name + ',' + last_name + ',' + str(age(name, last_name)) + ','+ str(gpa(name,last_name)) + '\n'
            names_list.append(name_line)
        else:
            myCondition = False

    # open friends.txt and writes names in list in it
    with open('friends.txt', 'w') as outfile:
        outfile.writelines(names_list)

# generates a random age number
def age(name,lastname):
    num= str(random.randint(18,23))
    return num

# generates a random gpa number
def gpa(name,lastname):
    num = random.uniform(3.00, 4.00)
    num2 = round(num,2)
    return num2


if __name__ == "__main__":
    main()
