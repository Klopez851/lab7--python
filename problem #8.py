###########################################
# Author: Keidy Lopez
# Filename: problem #8.py
# Description: program that takes a zipcode, returns city and state it belongs to, and pinpoints place in a map
###########################################
import webbrowser

def main():
    # opening statements
    print('Opening the zipcode database file...')
    print('Creating a searchable data structure...')

    # opens database file
    fileOpen()

    # asks user to input a zipcode and returns city,state it belongs to
    my_condition=True
    while my_condition:
        zipcode = int(input('Enter a zipcode to search for (zero to quit): '))
        if zipcode == 0:
            my_condition=False
        elif zipcode !=0:
            zipcode_find = fileSearch(zipcode) # searches through the database and prints city,state the zipcode belongs to
            print(str(zipcode_find[0]) +', '+str(zipcode_find[1]))
            answer = input('Do you want to see this place on a map?(Y/N): ')
            if answer.upper() =='Y':
                webBrowser(zipcode_find[2], zipcode_find[3]) # opens url with places lat and log on a map

def fileOpen():
    # variable with file
    data_file = 'zipcode_database_full.txt'
    zipcode_data = []  # list that holds stripped and split data
    with open(data_file, 'r') as infile:   # opens file
        for line in infile:   # for loop that strips and slipts csv and appends the values to list
            lines = line.rstrip().split(',')
            zipcode_data.append(int(lines[0]))
            zipcode_data.append(lines[1])
            zipcode_data.append(lines[2])
            if lines[3] !='' and lines[4] !='':
                zipcode_data.append(float(lines[3]))
                zipcode_data.append(float(lines[4]))
    return zipcode_data


def fileSearch(Z:int):
    zipcode_data = fileOpen() # opens file and holds returned data
    place = [] # list that will hold city,state
    for i in range(len(zipcode_data)): #for loop that looks through zipcode data and looks for the first instance
        if Z == zipcode_data[i]:       # of a zipcode and appends it's city and state to the list
            place.append(zipcode_data[i+1])
            place.append(zipcode_data[i+2])
            place.append(zipcode_data[i+3])
            place.append(zipcode_data[i+4])
            break
    return place


def webBrowser(a,b):
    webbrowser.open("https://www.google.com/maps/place/"+str(a)+','+str(b)) # opens coordinates of a zipcode in google


if __name__ == "__main__":
    main()
