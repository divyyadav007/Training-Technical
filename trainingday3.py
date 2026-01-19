##------------- -list of 5 numbers. print the first n last and lenght of element --------#

# l = [1,2,3,4,5]

# print(l[0])
# print(l[-1])
# print(len(l))

#----------take a list of nunber and dins the sum ana d average using built functions---------

# num = [1,2,3,4,5,6,7,8,9]

# print("Sum is:", sum(num))
# print("Average is:", sum(num)/len(num))

#--------list of fruits , add a new fruioit using append and insert one at position 2 using insert_____

# fruit = ["apple","mango ", "guava","pineapple"]
# fruit.append("peach")
# print(fruit)
# fruit.insert(1,"grapes")
# print(fruit)

#-----remove and element from a list using remove and dwelete the last elemtne using pop------------

# fruit = ["apple","mango ", "guava","pineapple"]
# #using remove
# fruit.remove("apple")
# print(fruit)
# #using pop
# print(fruit.pop())
# print(fruit)

#---------- a list with duplicates number sand use couint to check how many time a number appears=--------

# lis = [8,5,1,4,2,6,5,4,4]

# print("COunt is :", lis.count(lis[3]))

#-------searching ans sorting---------#

#--- check is number exist in a list or not-----

# lis = [8,5,1,4,2,6,5,4,4]
# number = 4

# if number in lis:
#     print("Yes, present in list")
# else:
#     print("Not present in list")


#-------------create a list of 5 integram use index to find the position of iven  umber

# lis = [8,5,1,4,2,6,5,4,4]
# print("the index of number is :", lis.index(4))

#------sort a list in ascending and descending order

# lis = [8,5,1,4,2,6,5,4,4]
# print(lis.sort())
# print(lis)
# lis.sort(reverse=True)
# print(lis)


#  #-----reverse a list---------#
# fruits = ['apple', 'banana', 'cherry', 'date']
# print(f"Original list: {fruits}")
# fruits.reverse()
# print(f"Updated list: {fruits}")

########## TUPLE QUESTIONS ########################

# tup = (1,2,3,4,5)
# print(tup[0],",",tup[-1])

# print("Lenght of tuple is:",len(tup))

# fruits = ('apple', 'banana', 'cherry', 'date')
# for fruit in fruits:

# fruits = ('apple', 'banana', 'cherry', 'date')
# if 'apple' in fruits:
#     print("Yes, 'apple' is in the fruits tuple")
# else:
#     print("No, 'apple' is not in the fruits tuple")

# tup1 = (1,2,3,4,5)
# tup2 = (6,7,8,9,10)
# print(tup1 + tup2)

##-------------Tuple methods------------#

#create a tuplwe wqith a repeated numbers uise count to dinsd hpowq m amuy time a number appears

# tup1 = (1,2,3,4,5,2,1,58,6,4,2,2,3)
# print(tup1.count(2))

# #find position using index
# print(tup1.index(58))


## conversion and nesting###


#convert a list ionto tuple

# my_list = [10, 20, 30, 'apple', 'banana']

# my_tuple = tuple(my_list)

# print(my_tuple)
# print(type(my_tuple))
# 
#   ##convert a tuple into a list and modfy it and convbbert it into tuple again


# my_tuple = (1, 2, 3, 'a', 'b')
# print(f"Original tuple: {my_tuple}")

# my_list = list(my_tuple)
# print(f"Converted to list: {my_list}")

# my_list.append('c')       
# my_list[0] = 10           
# my_list.remove('b')       
# print(f"Modified list: {my_list}")

# my_new_tuple = tuple(my_list)
# print(f"Converted back to tuple: {my_new_tuple}")



nested_tuple = (("apple", "banana"), ("carrot", "daikon"), ("eggplant", "fig"))
print("The entire nested tuple:", nested_tuple)
element = nested_tuple[1][1]
print("The specific element at nested_tuple[1][1] is:", element)