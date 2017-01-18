# -*- coding: utf-8 -*-
"""
Project 02 structure
prompt user to input an interger
establish the value of certian variables for later use
establish the starting length of the user's input interger
while loop to sum the value of all the digits in an interger 
\ until that sum is a single interger in length
    determine the value of the final digit in the interger
    print the final digit
    If this is not the final digit in the interger, print a '+'
    Add the value of the digit to the total sum
    set the value of the interger equal to the value of the interger 
    \ without the rightmost digit
    Add 1 to the loop counter
    If this is the final iteration of the while loop under 
    \ the current conditions and the value of the sum is only a single digit:
        print an = sign and the total to finish the printed equation
        exit the while loop
    f this is the final iteration of the while loop under 
    \ the current conditions and the value of the sum is 2 or more digits:
        print an = sign and the total to finish the printed equation
        reset the loop counter
        set the value of the sum equal to the input interger
        reestablish the length of the input interger
        reset the value of the sum  
"""

input_str = input("Input a postive interger: ")
input_int = int(input_str)
"""User's input interger"""

while_escape = 0
"""While loop counter that serves in the while loop escape contitions"""
total = 0
"""sum of all the digits in the input interger"""
digit_in_place = 0
"""The value of the final digit in an interger"""

"""This while loop counts the number of digits in the number.
digit_count = 0
Ex: 1000 will have a digit_count of 3"""

"""while while_escape != 1: 
    if 10**digit_count <= input_int:
        digit_count += 1
        
    elif 10**digit_count > input_int:
        whileEscape = 1"""

"""Hey! It looks like I reinvented the function len(). 
I dont want to erase my beautiful work, so I'll leave it in"""     
length = len(str(input_int))


while while_escape <= length:
    digit_in_place = input_int%10
    print(digit_in_place, end="")
    if while_escape < length-1:
        print(" + ", end="")
    total += digit_in_place
    input_int = input_int//10
    while_escape += 1
    if (while_escape == length and total < 10):
        """This condition is met if the sum is 1 digit and the while loop is about to end"""
        print(" =", total)
        while_escape = length + 1
    elif(while_escape == length and total>=10): 
        """This condition is met if the sum is greater than 2 digits and the while loop is about to end"""
        print(" =", total)
        while_escape = 0
        length = len(str(total))
        input_int = total
        total = 0
