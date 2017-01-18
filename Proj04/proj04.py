###############################################################################
#open_file() is called, prompting the user for a file name
#line_isolate() is called to isolate the contents of line 9
#Line contents are fed into find_min_percent() where every value in the line is 
#   compared to find the smallest. This value is returned to min_percent and
#   its index is returned to min_index
#Line contents are fed into find_max_percent() where every value in the line is 
#   compared to find the largest. This value is returned to max_percent and
#   its index is returned to max_index
#line_isolate() is called to isolate the contents of line 44
#Line contents are fed into find_gdp() to determine the GDP at the min_index
#Line contents are fed into find_gdp() to determine the GDP at the max_index
#line_isolate() is called to isolate the contents of line 8
#Line contents are fed into find_year() to find the year associated with the
#   min_index
#Line contents are fed into find_year() to find the year associated with the
#   max_index
#All derived values are fed into display(). This function prints all the values
#   in the desired format
###############################################################################


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
            print("Error. Please try again")
            continue
        exit_bool = True
    return fp

def line_isolate(file_input, line_number):
    """
    Function isolates the desired line based on the file opened above and the 
        line number
    file_input: the multi-line file that will be sifted through
    line_number: The line at which the for loop should stop changing the value 
        of line_contents_local
    line_contents_local: the local variable that contains the line-by-line 
        contents. When the desired line is reached, its value stops changing
        and gets returned
    """
    line_number_local = 0
    line_contents_local = ""
    for line_number_local,line_contents_local in enumerate(file_input):
        if line_number_local == line_number-1:
            break
    return line_contents_local
    
def find_min_percent(line):
    """
    Function finds the smallest percentage change in the line provided
    line: the entire line that will be sifted through for the desired info
    min_value: the smallest percentage on the line
    min_value_index: the index value associated with the point in the line at
        which min_value came from. This value is important for finding other
        values on other lines within the same year as the min_value
    """
    index, index_counter, min_value = 76,0,100000000
    line_chunk = ""
    
    while index+index_counter < len(line):
        line_chunk = line[index+index_counter:index+index_counter+12]
        line_chunk = line_chunk.strip(" ")
        line_chunk = float(line_chunk)        
        if line_chunk < min_value:
            min_value = line_chunk
            min_value_index = index+index_counter
        index_counter += 12
    return min_value, min_value_index

def find_max_percent(line):
    """
    Function finds the largest percentage change in the line provided
    line: the entire line that will be sifted through for the desired info
    max_value: the largest percentage on the line
    max_value_index: the index value associated with the point in the line at
        which max_value came from. This value is important for finding other
        values on other lines within the same year as the max_value
    """
    index, index_counter, max_value = 76,0,-100000000
    line_chunk = ""
    
    while index+index_counter < len(line):
        line_chunk = line[index+index_counter:index+index_counter+12]
        line_chunk = line_chunk.strip(" ")
        line_chunk = float(line_chunk)        
        if line_chunk > max_value:
            max_value = line_chunk
            max_value_index = index+index_counter
        index_counter += 12
    return max_value, max_value_index

def find_gdp(line, index):
    """
    Function isolates the float value of the GDP from the line at the index 
        point
    line: the entire line that will be sifted through for the desired info
    index: the index value associated with the max or min percentage found 
        above. This index value is important for finding the GDP value in the 
        same year as the percentage value
    gdp: The GDP value in the trillions
    """
    gdp = float(line[index:index+12].strip())
    gdp = gdp/1000
    return gdp

def find_year(line, index):
    """
    Function isolates the int value of the year from the line at the index 
        point
    line: the entire line that will be sifted through for the desired info
    index: the index value associated with the max or min percentage found 
        above. This index value is important for finding the year that the
        percentage value occured in
    year: the value of the year
    """
    year = line[index:index+12].strip()
    return year


def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    """
    Function takes all the values derived from the input file and displays them
        in the desired format
    min_val: the minimum percentage value
    min_year: the year that the minimum percentage value occured
    min_val_gdp: the gdp value from the same year as the minimum percentage 
        value
    max_val: the maximum percentage value
    max_year: the year that the maximum percentage value occured
    max_val_gdp: the gdp value from the same year as the maximum percentage 
        value
    """
    print("")    
    print("Gross Domestic Product")    
    print("The minimum change in GDP was",min_val,"percent in", min_year, \
    "when the GDP was {:.2f} trillion dollars.".format(min_val_gdp))
    print("The maximum change in GDP was",max_val,"percent in", max_year, \
    "when the GDP was {:.2f} trillion dollars.".format(max_val_gdp)) 
    
min_percent, min_year, min_GDP, max_percent, max_year, max_GDP = 0,0,0,0,0,0
min_index, max_index = 0,0
line_contents = ""

#The file is opened
GDP_input = open_file()

#This block calls the functions that derive the maximum and minimum percentage 
#changes as well as the index points of those percentage values
GDP_input.seek(0)
line_contents = line_isolate(GDP_input, 9)
min_percent, min_index = find_min_percent(line_contents)
max_percent, max_index = find_max_percent(line_contents)

#This block calls the functions that derive the maximum and minimum GDP values
#based on the index points created above
GDP_input.seek(0)
line_contents = line_isolate(GDP_input, 44)
min_GDP = find_gdp(line_contents, min_index)
max_GDP = find_gdp(line_contents, max_index)

#This block calls the functions that derive the year respective to the index
#values created above
GDP_input.seek(0)
line_contents = line_isolate(GDP_input, 8)
min_year = find_year(line_contents, min_index)
max_year = find_year(line_contents, max_index)

#All derived information is input into the final function to be output in the
#desired format
display(min_percent, min_year, min_GDP, max_percent, max_year, max_GDP)

GDP_input.close()

#Q1: 7
#Q2: 3
#Q3: 1
#Q4: 6