# This is a sample proj11-test.py program
# There are two requirements:
#   A) Demonstrate all methods (except __repr__ which can only be demonstrated 
#      in the Python shell)
#   B) Include print statements so your output can be read and understood 
#      without reading the code

import classes

print("Create a Grade instance: p01, 70, 0.25")
p1 = classes.Grade("p01",75,0.25)    # tests __init__
print("Print the Grade instance")
print(p1)        # tests __str__
# we cannot test __repr__ in a program, only in the Python shell

# Create another grade instance, let's call it g2
print("Create a Grade instance: p02, 80, 0.50")
p2 = classes.Grade("p02",80,0.50)
print("Print the Grade instance")
print(p2) 

# Maybe create more grades
print("Create a Grade instance: p03, 90, 0.25")
p3 = classes.Grade("p03",85,0.25)
print("Print the Grade instance")
print(p3) 
print(" ")

# Create a Student instance, let's call it s1
s1 = classes.Student(1, "Jack", "Booker", [p1, p2])

# Then print s1, include descriptive print statements such as above
print("Create a Student instance: 1 Booker, Jack   [p01, p02])")
print("Print the Student instance")
print(s1)
print(" ")

# Demonstrate add_grade and calculate_grade
print("Demonstrate appending an assignment onto the grade list")
s1.add_grade(p3)
print(s1)
print("Demonstrate a calculation of the student's final grade")
s1_final = s1.calculate_grade()
print(s1_final)
print(" ")

# Create another student instance, let's call it s2
s2 = classes.Student(1, "Jessica", "Book", [p1, p2, p3])
print("Create another Student instance: 1 Book, Jessica  [p01, p02, p03])")
print(s2)
s2_final = s2.calculate_grade()
print(" ")

# Demonstrate comparison operators
print("Demonstrate if Jack's grade is greater than Jessica's")
print(s1.__gt__(s2_final))
print("Demonstrate if Jack's grade is less than Jessica's")
print(s1.__lt__(s2_final))
print("Demonstrate if Jack's grade is equal to Jessica's")
print(s1.__eq__(s2_final))