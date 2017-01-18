###############################################################################
#import pylab for later use in draw_plot()
#variables are declared
#read_file() is called. This function calls on open_file() to open the file the
#   user inputs. The function processes the file into a usable list
#The average of all the values in a year is determined by the function annual_
#   average(). The function determines the average of with every year and 
#   returns them all in a list.
#tuple_splitter() splits the points into a list of x coordinates and a list of 
#   y coordinates. 
#These lists are then fead into the draw_plot() function which draws a 
#   graphical representation of the average flow rate vs. the year.
#The plot is followed by a table of all the values in the plot, constructed by
#   the function display_tuples().
#The function input_month() prompts the user to input the integer value of a 
#   month.
#The function month_averages() extracts the flow rate associated with the 
#   user's month from each year in the list of the file contents
#tuple_splitter() splits the points into a list of x coordinates and a list of 
#   y coordinates. 
#These lists are then fead into the draw_plot() function which draws a 
#   graphical representation of the average flow rate vs. the year.
###############################################################################
import pylab

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
            file_name = input("Input a file name: ")
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
    Function calls open_file() to get a file pointer, then processes it to 
    extract the relivant data into a list.
    file_contents: the contents of the file stripped down to just the flow 
    rates. These rates are grouped together based on the year they were 
    recorded in.
    """
    file_contents, file, year_count = [[]],"",0
    
    file = open_file()
    for line in file:
        temp = line[33:].strip()
        file_contents[year_count].append(temp)
        if int(line[30:33].strip()) == 12:
            file_contents.append([])
            year_count += 1
    return file_contents
    
def draw_plot(x, y, plt_title, x_label, y_label):
    """ 
    Draw x vs. y (lists should have the same length)
    Sets the title of plot and the labels of x and y axis
    """
    pylab.title(plt_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    
    pylab.plot( x, y )
    pylab.show()

def display_tuples(tuples_list):
    """
    Function takes the list of points created by the functions annual_average()
    and monthly average() and displays them in a table format following the
    graph.
    tuples_list: a list of tuples that act as point coordinates in a graph
    """
    while_counter = 0
    
    print("Year{:>14}".format("Flow"))
    while while_counter < len(tuples_list):
        print(tuples_list[while_counter][0], "{:>13.2f}".format(float(\
        tuples_list[while_counter][1])))
        while_counter += 1 

def annual_average(L):
    """
    Function takes the list that contains the contents of the file opened by
    read_file and averages the data by year. These averages are then put in
    their own list.
    L: the list of values representing the entirety of the relivant information
    from the file.
    annual_averages: the list of average values from each year. 
    """
    while_counter, annual_averages = 0,[]
    
    #larger while is responcible for assigning the average of each year to the 
    #list
    while while_counter+1 < len(L):
        sum_of_flow, term, average, temp = 0,0,0,[]
        #smaller while is repsoncible for determining the sum of all the values
        #in a perticular year
        while term <= 11:
            sum_of_flow += float(L[while_counter][term])
            term += 1 
        average = sum_of_flow/12        
        temp = (while_counter+1932, average) #in form (year, average_flow)
        annual_averages.append(temp)
        while_counter += 1
    return annual_averages

def month_average(L,M):
    """
    Function takes the list that contains the contents of the file opened by 
    read_file and extracts only the values from a specific month out of each
    year. These values are then put in their own list.
    L: the list of values representing the entirety of the relivant information
    from the file.
    M: the user input integer of the month they wish to view. 
    monthly_averages: the list of the values from the specific month out of the
    year that the user wanted to see
    """
    while_counter, monthly_averages = 0,[]
    
    while while_counter+1 < len(L):
        #in form (year, month_flow)
        temp = (while_counter+1932, L[while_counter][M-1]) 
        monthly_averages.append(temp)
        while_counter += 1
    return monthly_averages

def input_month():
    """
    Function prompted the user for a valid month (represented by an interger).
    Function error checks that the user input is both a valid interger and
    exists within the range of 1-12
    month_int: the interger value the user input
    """
    exit_bool = False
    while exit_bool != True:
        try:
            month_int = 0
            month_int = int(input("Enter a month (1-12): "))
        except ValueError:
            print("Error. Not an interger.", end ="")
            continue
        if month_int > 12 or month_int < 1:
            print("Error. Interger out of range.", end="")
            continue
        exit_bool = True
    return month_int            

def tuple_splitter(averages_list):
    """
    Function splits apart the tuples into seperate lists
    x_list: the list of years from each tuple. This list will be input into 
    display_plot() as the list of x coordinates.
    x_list: the list of averages from each tuple. This list will be input into 
    display_plot() as the list of y coordinates.
    """
    x_list, y_list, while_counter = [],[],0

    while while_counter < len(averages_list):
        x_list.append(averages_list[while_counter][0])
        y_list.append(averages_list[while_counter][1])
        while_counter += 1
    return x_list, y_list 

#Variable declarations
month_int = 0
list_of_months = ["January","February","March","April","May","June","July",\
"August","September","October","November","December"]
file_list, annual_averages_list, years_list, averages_list = "","","",""

#open the file and process it into a usable format. file_list reads as a list
#each year
file_list = read_file()
annual_averages_list = annual_average(file_list)

#annual_averages_list needs to be split into years_list and averages_list.
#These lists are then fead into the function draw_plot as the values of points
#along the x axis and y axis
years_list, averages_list = tuple_splitter(annual_averages_list)
draw_plot(years_list, averages_list, "Annual Average Flow 1932-2015", "Year",\
"Flow")
#following draw_plot, the next two lines create the table of points represented
#in the graph
print("Annual Average Flow")
display_tuples(annual_averages_list)

#by prompting the user for the interger value of a specific month, the values
#of that month can be presented in graph and table
month_int = input_month()
month_averages_list = month_average(file_list, month_int)
years_list, averages_list = tuple_splitter(month_averages_list)

#this for loop gives the interger value of the month chosen by the user a name
for month_number, month_name in enumerate(list_of_months):
    if month_int-1 == month_number:
        month_title =  list_of_months[month_number]
draw_plot(years_list, averages_list, "Average Flow for "+month_title, "Year", \
"Flow")
#following draw_plot, the next two lines create the table of points represented
#in the graph
print("Average Flow for", month_title)
display_tuples(month_averages_list)


#Questions
#Q1: 6
#Q2: 3
#Q3: 1
#Q4: 7