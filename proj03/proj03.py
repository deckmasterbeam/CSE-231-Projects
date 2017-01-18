###############################################################################
#Computer project #5
#
#Establish while loop and relivant variables
#   Prompt user for residency status
#       check if this input is valid
#           assign the relivant value to resident_bool
#   Prompt user for grade level
#       check if this input is valid
#           assign the relivant value to level_int
#   Prompt user for college
#       check if this input is valid
#           assign the relivant value to college_str
#   Prompt user for credits taken
#       check if this input is valid
#           assign the relivant value to credits_int
#   Determine the price per credit based on residency and grade level
#       set tuition equal to the multiple of price per credit and credits taken
#   Determine college specific bills
#   Determine applicable student-voted taxes
#   Print the formatted value of tuition
#   Prompt the user to restart the while loop or terminate
###############################################################################
exit_condition_int = 0
while exit_condition_int == 0:
    #variable resets
    tuition = 0 #total tuition based on all relivant factors
    level_int = 0 #grade level
    resident_bool = True #residency status
    college_str = "" #name of college
    credits_int = 0 #number of credits taken this semester
    
    #Residency input
    input_str = str(input("Resident (Yes/No): "))
    if input_str.lower() == "yes":
        resident_bool = True
    elif input_str.lower() == "no":
        resident_bool = False
    else:
        print("invalid input")

    #Grade level input
    input_str=str(input("Input level — freshman, sophomore, \
junior, senior, graduate: "))
    if input_str.lower() == "freshman":
        level_int = 1
    elif input_str.lower() == "sophmore":
        level_int = 2
    elif input_str.lower() == "junior":
        level_int = 3
    elif input_str.lower() == "senior":
        level_int = 4
    elif input_str.lower() == "graduate":
        level_int = 5
    else:
        print("invalid input")
    
    #College input
    valid_colleges = ["business", "engineering", "health", "sciences", "none"]
    input_str=str(input("College — business, engineering, \
health, sciences, None: "))
    if input_str.lower() not in valid_colleges:
        print("invalid input")
    else:
        college_str = input_str
    
    #Cedits input
    input_str = input("Input credits this semester: ")
    if int(input_str) >= 0:
        credits_int = int(input_str)
    else:
        print("invalid input")

    #Resident status and grade level determine how youre charged per credit
    if resident_bool == True and (level_int == 1 or level_int == 2):
        tuition += 468.75*credits_int
    elif resident_bool == True and (level_int == 3 or level_int == 4):
        tuition += 523.25*credits_int
    elif resident_bool == True and level_int == 5:
        tuition += 698.50*credits_int
    if resident_bool == False and (level_int == 1 or level_int == 2):
        tuition += 1263.00*credits_int
    elif resident_bool == False and (level_int == 3 or level_int == 4):
        tuition += 1302.75*credits_int
    elif resident_bool == False and level_int == 5:
        tuition += 1372.00*credits_int
        
    #College-specific bills
    if college_str == "business" and (level_int == 3 or level_int == 4):
        tuition += 109.00
        if (credits_int >= 4):
            tuition += 109.00
    elif college_str == "engineering" and (level_int == 3 or level_int == 4, \
    level_int == 5):
        tuition += 387.00
        if (credits_int > 4):
            tuition += 258.00
    elif (college_str == "health" or college_str == "sciences") \
        and (level_int == 3 or level_int == 4):
        tuition += 50.00
        if (credits_int >= 4):
            tuition += 50.00
    if level_int == 5:
        tuition += 37.50
        if (credits_int >= 4):
            tuition += 37.50
       
    # Student-Voted Taxes
    tuition += 3.00 #FM radio tax
    if level_int < 5: #ASMSU Tax
        tuition += 18.00
    elif level_int == 5: #COGS Tax
        tuition += 11.00
    if credits_int >= 6:
        tuition += 5.00
    
    #print the final value of the bill
    print("Total bill: ${:,.2f}".format(tuition))
    
    #repeat while loop input
    input_str = input("Do you want to calculate again (Yes/No): ")
    if input_str.lower() == "no":
        exit_condition_int = 1
    elif input_str.lower() != "yes" and input_str.lower() != "no":
        print("invalid input")
        
# Questions 
# Q1: 7
# Q2: 3
# Q3: 2
# Q4: 7