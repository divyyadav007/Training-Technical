# ## OOPS Pillars

# #Q1 0 create a ckass student with attirbutes name , roll_no , and marks, write mthod to accept student detaild display student details

# class Student:
#     def __init__(self, name="", roll_no=0, marks=0):
#         # Initializing attributes
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

#     def accept(self):
#         print("Enter student details:")
#         self.name = input("Enter name: ")
#         self.roll_no = input("Enter roll no: ")
#         self.marks = input("Enter marks: ")
        
#     def display(self):
#         print("\n--- Student Details ---")
#         print("Name: ", self.name)
#         print("Roll no: ", self.roll_no)
#         print("Marks: ", self.marks)

# s1 = Student()

# s1.accept()
# s1.display()

# #Q3(Inheritance) create a base class person 

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary =  salary
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


# #Q4(Inheritance) create  two classes
# vehicle (base class) with method start()
# car (derived class ) with method drive()
# Now, createa an object od car and call both methods 
# 
class vehicle:
    def start(self):
        print("The vehicle is starting")

class car(vehicle):
    def drive(self):
        print("The car is driving")

car1 = car()
car1.start()
car1.drive()       


#Multilevel inheritance

#create a class grandgather , father and son such that each class has itw own show* mthod
#demonstate how multioleve; inheritance work by call three snow method using a son objects


class Grandgather:
    def show_g(self):
        print("Grandfather")


class Father:
    def show_f(self):
        print("Father")


class Son(Grandgather, Father):
    def show_s(self):
        print("Son")


son = Son()
son.show_g()

son.show_f()
son.show_s()