##--------------OOPS--------------#

#--creata a class student with attributes name and age crteate twk k j==bjhects and print theirt detaiks

# class Student:
#     def __init__(self, name , age):
#         self.name = name
#         self.age  =age
#     def detail(self):
#         print(f"The name of student is {self.name} and age is {self.age}")

# st1 = Student("Divyanshu",21)
# st2 = Student("Divyanshu Yadav",20)

# st1.detail()
# st2.detail()

#--------class car with attributes brnad and oprice write a metghiod show detaikd to print car details create two car object and call the method

class Car:
    def __init__(self,brand, price  ):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"The name of brand is {self.brand} and price is {self.price}")

car1 = Car("Mahindra",2400000)     
car2 = Car("BMW",4800000)         

car1.show_details()
car2.show_details()

#---- create a class employee with name and salary , use the init method pt initialize vales and print them usinfg an opbject

class Employee:
    
    def __init__(self, name, salary):
        self.name = name  
        self.salary = salary  

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary:,.2f}")



emp1 = Employee("Alice Johnson", 60000)


print(f"Accessing attributes directly:")
print(f"Name: {emp1.name}")
print(f"Salary: ${emp1.salary:,.2f}\n")

print(f"Using the display_info method:")
emp1.display_info()

#---------create a class mobile with brand and model create three objects and orint their information

class Mobile:
    def __init__(self,brand, model  ):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"The name of brand is {self.brand} and price is {self.model}")

mob1 = Mobile("Xiaomi","CIVI 14")     
mob2 = Mobile("Vivo","IQOO NEO")         

mob1.show_details()
mob2.show_details()

print(f" the detail of mob1 is {mob1.brand} and {mob1.model} ")



#-----create a ckass college with class variable collegename and instance variable student name

class College:
    college_name = "BBD University"
    def __init__(self, student_name):
        self.student_name = student_name
 
st = College("Divyanshu")
print(st.student_name)
print(st.college_name)


#--------create a class Bike with attributes brand color, create an bject and call a method start that print color brand bike is starting


class Bike:
    def __init__(self,brand, color  ):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f"The name of brand is {self.brand} and color is {self.color}")

    def start(self):
        print("The Bike is starting")

bike1 = Bike("Royal Enfield","Grey")     
bike2 = Bike("Duke","Black")         

bike1.show_details()
bike2.show_details()
bike1.start()


#------------

class Company:
    company_name = "Infosys"
    def __init__(self, emp_name,sal):
        self.emp_name = emp_name
        self.sal = sal
 
emp11 = Company("Divyanshu",4499000)
emp12 = Company("Divyanshu yadav",14500)
print(emp11.emp_name)
print(emp12.sal)