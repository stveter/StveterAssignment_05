#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Desc: Updated starter script to complete assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# STveter, 2022-Nov-13, Edited File
# STveter, 2022-Nov-13, Completed File
#------------------------------------------#

# Declare variabls

Song = {"Shelter": "1, Porter Robinson & Madeon.","Rom": "2, Helios.","Midnight Kids": "3, Run it.","Hymm for the weekend": "4, Coldplay."}
# Created Dict

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
# Created dictionary to add, delete, and load inventory from
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        # runFlag = False
        print('Program has been closed')
    
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        print(Song)
        print('\n')
        
        pass
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        # Added the functionality to add a Dict to the list
        if strChoice == "a":
            term = input("What song do you want me to add?: ")
            if term not in Song:
                definition = input("\nWhats the  ID number, and the Album name?: ")
                Song[term] = definition
                print("\n", term, "has been added")
                print('\n')
            else:
                print("\nThat Term already exists! Try Redefining it")
        
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        # Added the functionality to view the current data, even after the user uploads more information
        print('CD Title, ID, Artist')
        print('\n')
        print(Song)
        print('\n')
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        # Added the ability to delete an entry from the dictionary
    
        if strChoice == "d":
            term = input("What song do you want me to delete?: ")
            if term in Song:
                del Song[term]
                print("\nOkay, this song has been deleted:", term)
                print('\n')
            else:
                print("\nI can't delete that!", term, "doesn't exist in the dictionary.")
        

    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        # Added the functionality to save the new data to a text file if the user wants too
        objFile = open('UpToDateCDInventory.txt', 'w')
        
        print('Saving your information')
        print('\n')
        
        objFile.write(str(Song))
            
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x!')

