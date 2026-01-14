# ============================================
# BBDU PYTHON TECHNICAL TRAINING
# PART A + PART B (Q1 to Q20)
# ============================================


# ---------------- Ques 1 ----------------
# Salary Increment Logic
salary = float(input("\nQ1 Enter salary: "))

if salary < 30000:
    new_salary = salary + salary * 0.20
elif salary <= 60000:
    new_salary = salary + salary * 0.10
else:
    new_salary = salary

print("New Salary:", new_salary)


# ---------------- Ques 2 ----------------
# Multiple Conditions Check
num = int(input("\nQ2 Enter a number: "))

if num % 3 == 0 and num % 4 == 0:
    print("Divisible by both 3 and 4")
elif num % 3 == 0 or num % 4 == 0:
    print("Divisible by only one of them")
else:
    print("Divisible by none")


# ---------------- Ques 3 ----------------
# Bill Discount Calculator
bill = float(input("\nQ3 Enter bill amount: "))
payment_mode = input("Enter payment mode (card/cash): ").lower()
member = input("Premium member? (yes/no): ").lower()

discount = 0

if bill > 5000 and payment_mode == "card":
    discount = 0.15
elif bill > 5000 or member == "yes":
    discount = 0.10

final_bill = bill - (bill * discount)
print("Final Bill:", final_bill)


# ---------------- Ques 4 ----------------
# Even–Odd and Range Check
n = int(input("\nQ4 Enter number: "))

if n % 2 == 0 and 50 <= n <= 100:
    print("Even and between 50-100")
elif n % 2 != 0 and n > 100:
    print("Odd and greater than 100")
else:
    print("Invalid Category")


# ---------------- Ques 5 ----------------
# Assignment Operator Tracker
x = int(input("\nQ5 Enter value of x: "))

x += 10      # adding 10
x *= 2       # multiplying by 2
x -= 5       # subtracting 5

print("Final value of x:", x)


# ---------------- Ques 6 ----------------
# Comparison Chain
a = int(input("\nQ6 Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b < c:
    print("Increasing Order")
else:
    print("Not Increasing")


# ---------------- Ques 7 ----------------
# Login Attempt Validator
username = input("\nQ7 Enter username: ")
password = input("Enter password: ")
attempts = int(input("Enter login attempts: "))

if username == "admin" and len(password) >= 6 and attempts < 3:
    print("Login Allowed")
else:
    print("Login Denied")


# ---------------- Ques 8 ----------------
# Mathematical Expression Evaluation
a = int(input("\nQ8 Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result = (a + b) ** 2 > a**2 + b**2 + c
print("Expression Result:", result)


# ---------------- Ques 9 ----------------
# Divisibility Priority
num = int(input("\nQ9 Enter number: "))

if num % 2 == 0 and num % 5 == 0:
    print("Divisible by 2 and 5")
elif num % 2 == 0:
    print("Divisible by only 2")
elif num % 5 == 0:
    print("Divisible by only 5")
else:
    print("Not divisible by 2 or 5")


# ---------------- Ques 10 ----------------
# Income Tax Slab
income = float(input("\nQ10 Enter income: "))

tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.10
else:
    tax = income * 0.20

print("Tax:", tax)
print("Net Income:", income - tax)


# ================= PART B =================


# ---------------- Ques 11 ----------------
# Student Grading System
marks = int(input("\nQ11 Enter marks: "))

if marks >= 90:
    print("Grade A - Excellent")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# ---------------- Ques 12 ----------------
# Electricity Bill Calculation
units = int(input("\nQ12 Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Electricity Bill:", bill)


# ---------------- Ques 13 ----------------
# ATM Withdrawal System
balance = float(input("\nQ13 Enter balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount % 100 == 0 and balance >= amount and (balance - amount) >= 500:
    print("Withdrawal Successful")
else:
    print("Withdrawal Denied")


# ---------------- Ques 14 ----------------
# Day Type Checker
day = int(input("\nQ14 Enter day number (1-7): "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")


# ---------------- Ques 15 ----------------
# Menu-Driven Calculator
a = int(input("\nQ15 Enter first number: "))
b = int(input("Enter second number: "))
choice = int(input("1.Add 2.Sub 3.Mul 4.Div : "))

match choice:
    case 1:
        print("Result:", a + b)
    case 2:
        print("Result:", a - b)
    case 3:
        print("Result:", a * b)
    case 4:
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    case _:
        print("Invalid Choice")


# ---------------- Ques 16 ----------------
# Insurance Eligibility
age = int(input("\nQ16 Enter age: "))
salary = int(input("Enter salary: "))
medical = input("Medical clear? (yes/no): ")

if age >= 25:
    if salary >= 40000:
        if medical == "yes":
            print("Eligible for Insurance")
        else:
            print("Medical not clear")
    else:
        print("Salary too low")
else:
    print("Age not eligible")


# ---------------- Ques 17 ----------------
# Traffic Signal Simulator
color = input("\nQ17 Enter signal color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")


# ---------------- Ques 18 ----------------
# Triangle Type Checker
a = int(input("\nQ18 Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")


# ---------------- Ques 19 ----------------
# Exam Attempt Rules
result = input("\nQ19 Exam result (pass/fail): ")
attempts = int(input("Attempt count: "))

if result == "fail" and attempts <= 3:
    print("Re-attempt Allowed")
else:
    print("No more attempts")


# ---------------- Ques 20 ----------------
# Password Strength Checker
password = input("\nQ20 Enter password: ")

has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if len(password) >= 8 and has_digit and has_upper:
    print("Strong Password")
else:
    print("Weak Password")
