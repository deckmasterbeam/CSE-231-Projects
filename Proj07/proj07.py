###############################################################################
#Variables are declared 
#Open_file() is called. This function returns a list of file pointers.
#Iterating through the list of file pointers, temporary dictionaries are 
#   created of the valueable information from each file by the read_file() 
#   function
#Each dictionary is merged into a master dictionary called mileage_dict
#Mileage_average() is called to determine the average mileage at each year in 
#   the master dictionary, mileage_dict. These averages are stored in 
#   averages_dict
#Averages_dict is input into the function dict_splitter() which splits the
#   dictionary into its respective parts: year_list, city_dict, highway_dict
#These parts are input into the provided plot_mileage() which creates two 
#   plots, one of the city mileage averages and one of the highway mileage
#   averages
#Total_averages() is called to determine the average mileage across all the 
#   years in the plot for each man. These averages are then desplayed
#   in the desired format 
###############################################################################

import csv
import pylab
import matplotlib.patches as patches

def plot_mileage(years,city,highway):
    """
    Plot the city and highway mileage data.
    Input: years, a list of years;
    city, a dictionary with man as key and list of annual mileage as 
    value;
    highway, a similar dictionary with a list of highway mileage as values.
    Requirement: all lists must be the same length.
    """
    pylab.figure(1)
    pylab.plot(years, city['Ford'], 'r-', years, city['GM'], 'b-', years,
             city['Honda'], 'g-', years, city['Toyota'], 'y-')
    red_patch = patches.Patch(color='red', label='Ford')
    blue_patch = patches.Patch(color='blue', label='GM')
    green_patch = patches.Patch(color='green', label='Honda')
    yellow_patch = patches.Patch(color='yellow', label='Toyota')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('City Fuel Economy (MPG)')
    pylab.show()
    
    # Plot the highway mileage data.
    pylab.figure(2)
    pylab.plot(years, highway['Ford'], 'r-', years, highway['GM'], 'b-', years,
             highway['Honda'], 'g-', years, highway['Toyota'], 'y-')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('Highway Fuel Economy (MPG)')
    pylab.show()
    
def open_file():
    """
    Function prompts the user for a string of files to open. Provided the user
    specified files are acceptable and exist, those files are opened and put
    into a list of file pointers. Otherwise, all files are closed and user is
    prompted again
    fp: a list of file pointers that will assign the contents of the file to a
    variable
    """
    acceptable_decades, fp, exit_bool = ("1980","1990","2000","2010"),[], False
    
    while exit_bool != True:
        try:
            error_bool, user_input, user_input_list = False,"",[]
            
            user_input = input("Input multiple decades separated by commas," +
            "e.g. 1980, 1990, 2000: ")
            user_input_list = user_input.split(",")
            for element in user_input_list:
                if element.strip() not in acceptable_decades:
                    print("Error in decade.", end="")
                    error_bool = True
            if error_bool == True:
                continue
            for element in user_input_list:
                temp_file = open(element.strip()+"s.csv", "r")
                fp.append(temp_file)
        except FileNotFoundError:
            print("file not found", end="")
            for file in fp:
                file.close()
            fp = []
            continue
        exit_bool = True
    return fp

def read_file(input_file):
    """
    Function processes the relevant info (mileage) from the input file into a 
    dictionary with a structure of {man: {year: {city: [mileage, 
    mileage], hwy: [mileage, mileage]}}}. Function does this by matching car 
    brand on a specific line with their man then putting the mileage 
    values from that line into into their appropriate space based on 
    man, year, and type (either city or hwy)
    Input_file: the file input into the function
    Mileage_dict: the dictionary file containing all the mileage values
    """
    mileage_dict = {}
    
    for line_number, line in enumerate(input_file):
        if line_number != 0:
            man = ""
            brand = line[46].lower()
            year = int(line[63])
            m1 = int(line[4])
            m2 = int(line[34])
            if year == 2017:
                continue
            if brand == "ford" or brand == "mercury" or brand == "lincoln":
                man = "Ford"
            if brand == "chevrolet" or brand == "pontiac" or brand == "buick" \
            or brand == "gmc" or brand == "cadillac" or brand == "oldsmobile" \
            or brand == "saturn":
                man = "GM"
            if brand == "honda" or brand == "acura":
                man = "Honda"
            if brand == "toyota" or brand == "lexus" or brand == "scion":
                man = "Toyota"
            
            if man != "Ford" and man != "GM" and \
            man != "Honda" and man != "Toyota":
                continue
            
            if man not in mileage_dict:
                mileage_dict[man] = {year:{"city": [m1], "hwy": \
                [m2]}}
                continue
            if year not in mileage_dict[man]:
                mileage_dict[man][year] = {"city": [m1], "hwy": \
                [m2]}
                continue
            mileage_dict[man][year]["city"].append(m1)
            mileage_dict[man][year]["hwy"].append(m2)
    return mileage_dict
    
def merge_dict(target, source):
    """
    function merges two dictionaries together
    target: the dictionary being added to
    source: the dictionary that has the data that needs to be added to the 
    target
    target: the updated dictionary to be returned
    """
    for key in source:
        if key not in target:
            target[key] = source[key]
        target[key].update(source[key])
    return target

def dict_splitter(input_dict):
    """
    Function takes a dictionary as input and splits it up into multiple lists
    and dictionaries to be used as input into the plot_mileage() function.
    Input_dict: the input dictionary
    year_list: the list of years present in the input_dict
    city_dict: the list of city mileage values in the input_dict organized 
    according to man
    highway_dict: the list of highway mileage values in the input_dict 
    organized according to man
    """
    previous_year = 0
    resort = False
    year_list, city_dict, highway_dict, city_list = [],{},{},[]
    
    for key in input_dict:
        city_list, highway_list = [],[]
        for year in input_dict[key]:
            city_list.append(input_dict[key][year]["city"])
            highway_list.append(input_dict[key][year]["hwy"])
            if year not in year_list:
                year_list.append(year)
            if year < previous_year:
                resort = True
            if resort != True:
                previous_year = year
        
        #This whole resort if statement block is designed to handle a specific 
        #bug where 2016 comes before all other years in whatever set its 
        #involved in
        if resort == True:
            year_list.remove(previous_year)
            year_list.append(previous_year)
            city_list.remove(input_dict[key][previous_year]["city"])
            city_list.append(input_dict[key][previous_year]["city"])
            highway_list.remove(input_dict[key][previous_year]["hwy"])
            highway_list.append(input_dict[key][previous_year]["hwy"])
            resort = False
        city_dict[key] = city_list
        highway_dict[key] = highway_list
    return year_list, city_dict, highway_dict

def mileage_average(input_dict):
    """
    Function calculates the average from each year for each man and
    returns the averages in the form of a dictionary
    Input_dict: the input dictionary
    Averages_dict: the dictionary of all the averages
    """
    averages_dict = {}
    
    for key in input_dict:
        for year in input_dict[key]:
            average_city, average_hwy,sum_value = 0,0,0
            for value in input_dict[key][year]["city"]:
                sum_value += value
            average_city = sum_value/len(input_dict[key][year]["city"])
            sum_value = 0
            
            for value in input_dict[key][year]["hwy"]:
                sum_value += value
            average_hwy = sum_value/len(input_dict[key][year]["city"])
            sum_value = 0
            
            if key not in averages_dict:
                averages_dict[key] = {year:{"hwy": average_hwy, "city": \
                average_city}}
            elif year not in averages_dict[key]:
                averages_dict[key][year] = {"hwy": average_hwy, "city": \
                average_city}
            else:
                averages_dict[key][year]["hwy"] = average_hwy
                averages_dict[key][year]["city"] = average_city
    return averages_dict
    
def total_averages(year_list, city_dict, highway_dict):
    """
    This function is largely a display function that does some calculations to
    find the averages of each man over the entire span of time the
    data represents
    year_list: the list of all the years
    city_dict: the dictionary of all the city mileage averages from each year
    highway_dict: the dictionary of all the highway mileage averages from each 
    year
    """
    sum_value, average = 0,0
    
    for year in year_list:
        if year >= 1980 and year <= 1989:
            if 1980 not in decade_list:
                decade_list.append(1980)
        if year >= 1990 and year <= 1999:
            if 1990 not in decade_list:
                decade_list.append(1990)
        if year >= 2000 and year <= 2009:
            if 2000 not in decade_list:
                decade_list.append(2000)
        if year >= 2010 and year <= 2019:
            if 2010 not in decade_list:
                decade_list.append(2010)
    for decade in decade_list:
        if decade == decade_list[0]:
            print("Manufactures' average for ", end="")
        if decade != decade_list[len(decade_list)-1]:
            print(decade, end=", ")
        else:
            print(decade, end="")
            
    print(" ")
    print("City")
    print("{:>10}: {}".format("Company", "Mileage"))
    for key in city_dict:
        for value in city_dict[key]:
            sum_value += value
        average = sum_value/len(city_dict[key])
        print("{:>10}: {:<0.2f}".format(key, average))
        sum_value, average = 0,0
    
    print("Highway")
    print("{:>10}: {}".format("Company", "Mileage"))    
    for key in highway_dict:
        for value in highway_dict[key]:
            sum_value += value
        average = sum_value/len(city_dict[key])
        print("{:>10}: {:<0.2f}".format(key, average))
        sum_value, average = 0,0
    
    
file_list, temp_dict, averages_dict, mileage_dict = [],{},{},{}
year_list, city_dict, highway_dict = [],{},{}
decade_list = []

file_list = open_file()

for file in file_list:
    temp = csv.reader(file)
    temp_dict = read_file(temp)
    mileage_dict = merge_dict(mileage_dict, temp_dict)
    temp_dict = {}
    file.close()

averages_dict = mileage_average(mileage_dict)
year_list, city_dict, highway_dict = dict_splitter(averages_dict)

plot_mileage(year_list, city_dict, highway_dict)
total_averages(year_list, city_dict, highway_dict)


# Questions
# Q1: 7
# Q2: 3
# Q3: 2
# Q4: 7