# # # File handling 

# # ##OPEN function

# # # file_object = open("file.txt","r")
# # # print(file_object.read())


# # # #closing a file

# # # file_object.close()

# # ## using with

# # with open("file.txt","r") as file_object:
# #     print(file_object.read())


# # #write mode

# # with open("file.txt","w") as file_object:
# #     file_object.write("Hello world")


# # #append mode

# with open("file.txt","a") as file:
#     file.write("My name is divyanshu yadav")
#     # file.read()

#     file = open("file.txt","r")
#     print(file.read())


# #

## STUDENT FILE HANDLING OPERATIONS

##Opening a file

with open("student.txt","r") as file:
    print(len(file.readlines()))


#rad and write mdoe 

with open("student.txt","r+") as file:
    print(file.read())


