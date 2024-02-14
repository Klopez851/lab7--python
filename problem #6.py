###########################################
# Author: Keidy Lopez
# Filename: problem #6.py
# Description: program that gives the max, min, sum, and average of numbers in random.txt
###########################################

def main():
    # main lists
    random_list=[]    # takes letter and numbers with no carriage return
    random_list2 =[] # takes numbers from first list as integers

    # opens random.txt and removes carriage return
    with open('random.txt', 'r') as infile:
        for line in infile:  #
            ranData = line.strip()
            random_list.append(ranData)

    # turns numbers with no carriage return and turns them into integer class
    for i in range(0,len(random_list),2):
        random_list2.append(int(random_list[i]))

    # prints out min, max, sum, average
    print('The lowest number in random.txt: ', getLowest(random_list2))
    print('The highest number in random.txt: ', getHighest(random_list2))
    print('The total sum of all the numbers in random.txt: ', getSum(random_list2))
    print('The average number of the numbers in random.txt: ', getAveraget(random_list2))

# takes list and returns min
def getLowest(myList:list)->int:
    lowest = min(myList)
    return lowest

# takes list and returns max
def getHighest(myList:list)->int:
    highest = max(myList)
    return highest

# takes list and returns sum of all nums
def getSum(myList:list)->int:
    sum_total = sum(myList)
    return sum_total

# takes list and returns average of all nums
def getAveraget(myList:list)->int:
    average = getSum(myList)/len(myList)
    average_2 = round(average,2)
    return average_2


if __name__ == "__main__":
    main()
