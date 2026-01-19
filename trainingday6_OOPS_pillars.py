## OOPS Pillars

#Q1 0 create a ckass student with attirbutes name , roll_no , and marks, write mthod to accept student detaild display student details

class Student:
    def __init__(self, name="", roll_no=0, marks=0):
        # Initializing attributes
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def accept(self):
        print("Enter student details:")
        self.name = input("Enter name: ")
        self.roll_no = input("Enter roll no: ")
        self.marks = input("Enter marks: ")
        
    def display(self):
        print("\n--- Student Details ---")
        print("Name: ", self.name)
        print("Roll no: ", self.roll_no)
        print("Marks: ", self.marks)

s1 = Student()

s1.accept()
s1.display()

