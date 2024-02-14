###########################################
# Author: Keidy Lopez
# Filename: problem #4.py
# Description: give average age and gpa of the ppl in friends.txt
###########################################

def main():
    # reads file, strips commas and carriage returns, turns number strings into integers or floats, and adds the result
    # to a list
    name_list = []
    with open('friends.txt', 'r') as name_file:
        for line in name_file:
            name_data = line.strip().split(',')
            name_list.append(int(name_data[2]))
            name_list.append(float(name_data[3]))

    #average age
    age_sum=0
    counter1=0
    for i in range(0,len(name_list),2):
        age_sum+=name_list[i]
        counter1+=1
    age_average = age_sum//counter1

    #average gpa
    gpa_sum = 0
    counter2 = 0
    for i in range(1, len(name_list), 2):
        gpa_sum += name_list[i]
        counter2 += 1
    gpa_average = round((gpa_sum / counter2), 2)



    print('the average age of your friends is: '+str(age_average))
    print('the average gpa of your friends is: ' + str(gpa_average))



if __name__ == "__main__":
    main()
