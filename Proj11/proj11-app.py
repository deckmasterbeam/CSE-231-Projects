###############################################################################
#Variables are declared
#Text files are opened via the open_file() function
#Provided these files can be opened, they are passed into the read_file() 
#function
#   read_file() constructs a list of grade objects and student objects.
#   All grade objects are added to their respective student object
#Student list is displayed in the desired format
#Text files are closed
###############################################################################

import classes

def open_files ():
    """
    Opens the two critical files, students.txt and grades.txt, and returns file
    pointers. If the file cant be found, the program is halted and appropriate
    error message is displayed
    fp_students: the students.txt file pointer
    fp_grades: the grades.txt file pointer
    """
    try:
        fp_students = open("students.txt")
    except FileNotFoundError:
        print("students.txt cannot be opened. Program halting")
        fp_students = ""
    try:
        fp_grades = open("grades.txt")
    except FileNotFoundError:
        print("grades.txt cannot be opened. Program halting")
        fp_grades = ""
    return fp_students, fp_grades


def read_file(fp_students, fp_grades):
    """
    Processes files into grade and student objects. The grade objects are added
    to their respective student object
    fp_students: the students.txt file pointer
    fp_grades: the grades.txt file pointer
    student_list: a list of the complete student objects
    """
    
    student_list, grades_list, students_grades, grade_obj_list = [],[],[],[]
    
    #splits up the lines in the students.txt in order to create student objects
    for line in fp_students:
        stu_id = int(line[:1])
        name1 = line[2:11].strip()
        name2 = line[11:].strip()
        student_list.append(classes.Student(stu_id, name1, name2, []))
    
    for line in fp_grades:
        
        #determine the number of assignments that exist in the grades file
        num = (len(line)-13)/7
        if num%7 > 7/2: #rounds up by adding 1, then rounding down
            num += 1
        num = int(num)
        
        if grades_list == []:
            #initializes the grades_list to have a length equal to the number
            #of assignments
            for i in range(num):
                grades_list.append([])
                
        #splits up the lines in grades.txt in order to create lists of data 
        #that can be turned into grade objects
        for i in range(num):
            grades_list[i].append(line[13+(7*i):13+(7*(i+1))].strip())
    
    #initializes the grade_obj_list to have as many sub-lists as students
    for i in range(len(student_list)):
        grade_obj_list.append([])
    
    for i in range(len(grades_list)):
        students_grades = grades_list[i][2:]
        
        
        #understanding the number of assignments in gradelist, lists of grade
        #objects can be made
        for spot, individual_grade in enumerate(students_grades):
            grade_obj = classes.Grade(grades_list[i][1],int(individual_grade),\
            float(grades_list[i][0]))
            grade_obj_list[spot].append(grade_obj)
    
    #because the students in students list line up with the grade lists in 
    #grade_obj_list, the grade lists at a spot i can be added to the student
    #object at spot i via the Student.add_grade() function
    for i in range(len(student_list)):
        individual_grade_list = grade_obj_list[i]
        student_obj = student_list[i]
        for grade in individual_grade_list:
            student_obj.add_grade(grade)
            
    final_grade = 0
    for student in student_list:
        final_grade = int(student.calculate_grade())
        final_grade_str = "Final grade:{:>5}%{}".format(final_grade, " "*7)
        student.add_grade(final_grade_str)
    return student_list


def display(student_list):
    """
    Displays the information in the student objects contained in student_list
    in the desired format. Also derives class average and displays that info.
    student_list: a list of all the student objects
    """
    class_ave_num = 0.0
    
    for student_obj in student_list:
        display_str = student_obj.__repr__()
        class_ave_num += student_obj.final
        print(display_str[2:19])
        num = (len(display_str)-19)/24
        if num%24 > 24/2: #rounds up by adding 1, then rounding down
            num += 1
        num = int(num)
        
        #forgive me for the janky formatting required to attempt to display
        for i in range(num):
            if display_str[20+(i*25)+(2*i)] != "'" and display_str[20+(i*25)+\
            (2*i)] != "]":
                print(display_str[20+(i*25)+(2*i):20+((i+1)*25)+(2*i)])
            elif display_str[20+(i*25)+(2*i)] == "'":
                try: 
                    print(display_str[20+(i*25)+(2*i)+1:20+((i+1)*25)+(2*i)])
                except:
                    print(display_str[20+(i*25)+(2*i)+1:])
        print(" ")
    print(" ")
    print("The class average is {:.2f}%".format((\
    class_ave_num/len(student_list))))
        
        
students_txt, grades_txt = "",""
students_with_grades = []

students_txt, grades_txt = open_files()
if students_txt != "" and grades_txt != "":
    students_with_grades = read_file(students_txt, grades_txt)
    display(students_with_grades)
students_txt.close()
grades_txt.close()

#Questions
#Q1:6
#Q2:1
#Q3:1
#Q4:7