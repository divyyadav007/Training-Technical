# 

## default and keyword arguments

def simple_interest(principal, rate=0.05, time=1):
    interest = principal * rate * time
    return interest

result = simple_interest(1000)
print(result)

#-------------------------------#
# def print_details(name, age):
#   """Prints a person's name and age using keyword arguments."""
#   print(f"Hello, my name is {name} and I am {age} years old.")

# # --- Using keyword arguments ---
# print_details(age=25, name="Alice") 
# print_details(name="Bob", age=30)

# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: ")) 

# print_details(name=user_name, age=user_age)

##-------------------recursive functions---------------------#

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"The factorial of {num} is {factorial(num)}") 

#fibonacci series upto a n terms


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
