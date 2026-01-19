# x= int(input("Enter the number:"))
# y = int(input("Enter the 2nd number:"))

# print("Sum", (x+y))
# print("Product",(x*y))
##=========================================##
# a = 25
# b=4
# print("Floor division", (a//b))
# print("Remainder",(a%b))
# print("Power",(a**b))
##=============================================##

# a= int(input("Enter the subject 1 marks:"))
# b= int(input("Enter the subject 2 marks:"))
# c= int(input("Enter the subject 3 marks:"))
# d= int(input("Enter the subject 4 marks:"))
# e= int(input("Enter the subject 5 marks:"))
# print("Average is :", (a+b+c+d+e)/5)

##===========================================##

# convert seconds to minutes and seconds

##=============================================##

# a = int(input("Enter the number to check:"))
# b = int(input("Enter the number :"))

# if(b%a ==0):
#     print(f"Number {a} is multiple of number {b}")
# else:
#     print(f"Number {b} is not a multiple of number {a}")

    ##================================================##

# a = int(input("Enter the number 1:"))
# b = int(input("Enter the number 2 :"))

# if a == b:
#     print("Number 1 is equal to number 2")
# else:
#     print("Number 1 is not equal to number 2")

##========================================##

# a = int(input("Enter the number 1:"))
# b = int(input("Enter the number 2 :"))

# if a > b:
#     print("Number 1 is greater than number 2")
# elif b>a:
#     print("Number 2 is greater than number 2")
# else:
#     print("Number are equal")

##===========================================##

# Assignemnt operators

# a = 10
# print(a)

#=====#

# a =20
# a+= 5
# print("Question 2:",a)

# b = 21
# b -= 3

# print("Question 3:",b)

# c = 34
# c *= 4
# print("Question 4:",c)

# d = 23
# d /= 4
# print("Question 4 is :", d)

# e = 23
# e //= 4
# print("Question 5 is :", e)

# f = 23
# f %= 4
# print("Question 6 is :", f)

# e = 23
# e //= 4
# print("Question 5 is :", e)


## Conditional Statements ##

# a = int(input("Enter the number to check:"))
# if a>0:
#     print("positive number")
# elif a<0:
#     print("Negative Number")
# else:
#     print("Number is 0")


#===========#

# age = int(input("Enter the age:"))
# if age > 18:
#     print("Eligible to vote")
#     print("Age is", age)
# else:
#     print("Not Eligible to vote")
#     print("Age is", age)

#----------------------------#

# num = int(input("Enter the number to check :"))
# if num%2==0:
#     print("Number is even ")
# else:
#     print("Number is odd")

    #----------------------------#


# mark= int(input("Enter the marks to know Grade:"))
# if mark>=90:
#     print("Grade A")
# elif mark>=75:
#     print("Grade B")
# elif mark>=50:
#     print("Grade C")
# else:
#     print("Fail")

#----------------------#

#check whether the given number is single digit double digit or more than two digit


# number = int(input ("Enter the number to check:"))


# if number > 0:
#         if number % 2 == 0:
#             print(f"{number} is positive and even")
#         else:
#             print(f"{number} is positive and odd")
# elif number < 0:
#      print(f"{number} is negative")
# else:
#      print(f"{number} is zero")

     #-------------------------------#
# take a password as input , it it is correct , print access granted else access denied

# password = int(input("Enter the passcode"))

# corrPass = 986532

# if password == corrPass:
#     print("Access Granted")
# else:
#     print("Access Denied")

#-----------------#

# write a prohra,m to check idf a character is vowel consinand or not an alpohabet

ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")
elif not ch.isalpha():
    print("The character is not an alphabet.")
elif ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

