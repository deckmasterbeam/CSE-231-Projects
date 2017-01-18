###############################################################################
# Class Grade
###############################################################################

class Grade ( object ):
    def __init__ ( self, name="assignment", grade="0", weight="0" ):
        """
        Function initializes the assignment object with the relevant 
        information
        name: a string of the name of the assignment
        grade: the int value of the grade received
        weight: the float value of the weight of the grade compared to other 
        grades
        """
        self.name = name
        self.grade = grade
        self.weight = weight
        
    def __str__ ( self ):
        """
        The inherent representation of the object as a string
        self: the grade object
        """
        out_str = "{},{},{}".format(self.name, self.grade, self.weight)
        
        return out_str
        
    
    def __repr__( self ): 
        """
        The representation of the grade object for use in display
        self: the grade object
        """
        out_str = "{:<11}:{:>5}%{:7.2f}".format(self.name, self.grade, \
        self.weight)
        
        return out_str

###############################################################################
# Class Student
###############################################################################

class Student ( object ):
    def __init__ ( self, stu_id= 0, name1= "John", name2= "Doe", grade_list=\
    None ):
        """
        Function initializes a student object with the relevant information
        self: the student object
        stu_id: the int of the student's id number
        name1: students first name
        name2: students second name
        grade_list: a list of all the Grade objects associated with this 
        student
        """
        self.stu_id = stu_id
        self.name1 = name1
        self.name2 = name2
        self.grade_list = grade_list
    
    def add_grade ( self, grade_obj ):
        """
        Appends a grade object onto a student object's grade_list
        self: the student object
        grade_obj: the grade object to be appended
        """
        self.grade_list.append(grade_obj)
    
    def calculate_grade ( self ):
        """
        Calculates the final grade based on the grade and weight the student 
        has on each assignment
        self: the student object
        total: the final grade
        """
        total = 0
        for grade in self.grade_list:
            grade_calc = grade.grade * grade.weight
            total += grade_calc
        #the final is added as an atribute of the object for calcuations
        self.final = total
        #the final is still returned because its nesseccary in calculations and
        #diplaying the final
        return total
    
    def __str__ ( self ):
        """
        The inherent representation of the object as a string
        self: the student object
        """
        out_str = "{}, {}, {}".format(self.stu_id, (self.name2+", "+\
        self.name1), self.grade_list)
        
        return out_str
    
    def __repr__ ( self ):
        """
        The representation of the student object for use in display
        self: the student object
        """
        out_str = "{:<2d}{:<17}{}".format(self.stu_id, (self.name2+", "+\
        self.name1), self.grade_list)
        
        return out_str

    def __gt__ ( self, other_final ):
        """
        Compares the final grade of the object to the final grade of the other
        object. Returns True if the first is greater. Returns False if they 
        aren't.
        self: the student object
        other_final: the final value of the other object
        """
        if self.final > other_final:
            return True
        else:
            return False
            
    def __lt__ ( self, other_final ):
        """
        Compares the final grade of the object to the final grade of the other
        object. Returns True if the first is less than. Returns False if they 
        aren't.
        self: the student object
        other_final: the final value of the other object
        """
        if self.final < other_final:
            return True
        else:
            return False
    
    def __eq__ ( self, other_final ):
        """
        Compares the final grade of the object to the final grade of the other
        object. Returns True if they are equal. Returns False if they aren't.
        self: the student object
        other_final: the final value of the other object
        """
        #the diffrence between the two is known as epsilon. If epslion is very
        #small, it can be understood that the floating point numbers are equal
        if (self.final - other_final) < 10**-6: 
            return True
        else:
            return False