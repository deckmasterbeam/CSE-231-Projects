###############################################################################
#read_file() is called to create a master list of all the relevant data in a
#file pointer, this pointer having been created by calling open_file()
#The racial breakdown of those exicuted is then calculated by race_counter()
#The gender breakdown of those exicuted is then calculated by gender_couter()
#The gender and racial breakdown of the victims of those exicuted is calculated
#by victim_counter()
#All breakdowns and derived values are input into display() where they can be
#output in the desired format
###############################################################################

#Answers to project questions:
#1: Yes, there were 273 executions of minorities while there were 225 
#executions of whites
#2: Yes, there were 28 executions of a minority who killed a white while there 
#were 7 executions of a white who killed a minority
#3: Yes, there were 65 executions of a man who killed a woman while there were 
#no execution of a woman who killed a man
#4: Yes, there were 118 executions of  men while there was 1 execution of a 
#woman

import csv

def open_file():
    """
    Function opens the file specified by the user while checking to make sure 
    the input is an existing file.
    fp: a file pointer that will assign the contents of the file to a variable
    """
    exit_bool = False
    
    while exit_bool != True:
        try:
            file_name = ""
            file_name = input("Enter a file name: ")
            fp = open(file_name)
        except FileNotFoundError:
            while exit_bool != True:
                try:
                    file_name = ""
                    file_name = input("Error: Input a file name: ")
                    fp = open(file_name)
                except FileNotFoundError:
                    continue
                exit_bool = True
            continue
        exit_bool = True
    return fp

def read_file():
    """
    Function calls open_file() and procedes to process useful information from
    the file pointer into a master list that can be used in other functions
    list_local: a master list of the race, gender, and victims of every 
    execution
    """
    list_local = []
    line_list = []
    
    fp = open_file()
    csv_fp = csv.reader(fp)
    
    for line in csv_fp:    
        line_list = [line[15],line[16],line[27]]
        list_local.append(line_list)
    fp.close()
    return list_local

def race_counter(list_local):
    """
    Function processes through the master list looking for instances of each
    race through the catagory of race of the person executed
    list_local: a master list of the race, gender, and victims of every 
    execution
    white_count: a count of the number of white people executed
    black_count: a count of the number of black people executed
    hispanic_count: a count of the number of hispanic people executed
    """
    white_count, black_count, hispanic_count = 0,0,0
    for line in list_local:
        if line[0].lower() == "white":
            white_count += 1
            continue
        elif line[0].lower() == "black":
            black_count += 1
            continue
        elif line[0].lower() == "hispanic":
            hispanic_count += 1
            continue
    return white_count, black_count, hispanic_count
    
def gender_counter(list_local):
    """
    Function processes through the master list looking for instances of male/
    female in the gender catagory
    list_local: a master list of the race, gender, and victims of every 
    execution
    male_count: a count of the number of male people executed
    female_count: a count of the number of female people executed
    """
    male_count, female_count = 0,0
    for line in list_local:
        if line[1].lower() == "male":
            male_count += 1
        if line[1].lower() == "female":
            female_count += 1
    return male_count, female_count

def victim_counter(list_local):
    """
    Function processes through the master list in order to find 1. the total
    number of people exicuted that didnt have relivant data missing, 2. the 
    number of minorities exicuted who killed a white person, 3. the number of
    whites exicuted who killed a minority person, 4. the number of men exicuted
    who killed women, and 5. the number of women exicuted who killed men
    list_local: a master list of the race, gender, and victims of every 
    execution    
    race_diff_count: a count of the number of lines where there is no missing
    relivant information (missing relicant infromation would be a "Not 
    Avalible" or blank space) in the race, gender, or victims catagory
    minority_white_count: the number of minorities exicuted who killed a white 
    person
    white_minority_count: the number of whites exicuted who killed a minority 
    person
    male_female_count: the number of men exicuted who killed women
    female_male_count: the number of women exicuted who killed men
    """
    minority_white_count, male_female_count = 0,0
    female_male_count, white_minority_count = 0,0
    race_diff_count = 0
    line_number = 0
    
    for line_number, line in enumerate(list_local):
        line[0] = line[0].lower()
        line[1] = line[1].lower()
        line[2] = line[2].lower()
        
        if line_number != 0 and line[0] != "not available" and line[0] != "" \
        and line[2] != "not available" and line[2] != "": #only count lines 
        #that do not include "Not Available", blanks, or the very first line
            race_diff_count += 1

        if line[0] == "black" or line[0] == "hispanic":
            if line[2].count("white") >= 1:
                minority_white_count += 1
        elif line[0].lower() == "white":
            if line[2].count("hispanic") >= 1 or line[2].count("black") >= 1:
                white_minority_count += 1
        if line[1] == "male":
            if line[2].count("female") >= 1:
                male_female_count += 1
        elif line[1] == "female":
            if line[2].count("male") >= 1 and line[2].count("female") == 0:
                female_male_count += 1

    return minority_white_count, male_female_count, female_male_count, \
    white_minority_count, race_diff_count

def display(white_count, black_count, hispanic_count, male_count, \
female_count, minority_white_count, male_female_count, female_male_count, \
white_minority_count, race_diff_count):
    """
    Function takes all derived information in and displays it in the desired
    format
    white_count: a count of the number of white people executed
    black_count: a count of the number of black people executed
    hispanic_count: a count of the number of hispanic people executed
    male_count: a count of the number of male people executed
    female_count: a count of the number of female people executed
    minority_white_count: the number of minorities exicuted who killed a white 
    person
    white_minority_count: the number of whites exicuted who killed a minority 
    person
    male_female_count: the number of men exicuted who killed women
    female_male_count: the total number of people exicuted that didnt have 
    relivant data missing
    """
    seperator = "========================================"    
    print(seperator)
    print("White vs. Minority")
    print("N =",white_count+black_count+hispanic_count)
    print("White:",white_count)
    print("Black:",black_count)
    print("Hispanic:",hispanic_count)
    print("Minority = Black + Hispanic:",black_count+hispanic_count)
    print(seperator)
    print("Male vs. Female")
    print("N =",male_count+female_count)
    print("Male =",male_count)
    print("Female:",female_count)
    print(seperator)
    print("Race difference between perpetrator and victim.")
    print("N =", race_diff_count)
    print("Minority-on-white:", minority_white_count)
    print("Male-on-female:", male_female_count)
    print("Female-on-male:", female_male_count)
    print("White-on-minority:", white_minority_count)
    print(seperator)
    
#set all variables
race_white, race_black, race_hispanic = 0,0,0
gender_male, gender_female = 0,0
minority_on_white, male_on_female, female_on_male, white_on_minority = 0,0,0,0
race_diff = 0

#open the user-input file
master_list = read_file()

race_white, race_black, race_hispanic = race_counter(master_list)
gender_male, gender_female = gender_counter(master_list)
minority_on_white, male_on_female, female_on_male, white_on_minority, \
race_diff = victim_counter(master_list)

display(race_white, race_black, race_hispanic, gender_male, gender_female, \
minority_on_white, male_on_female, female_on_male, white_on_minority, \
race_diff)

#Questions
#Q1: 7
#Q2: 3
#Q3: 1
#Q4: 6