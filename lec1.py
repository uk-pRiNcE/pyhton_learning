print("hello pyhton!!!")
# today i'm starting to improve my pyhton from basics
# variables and datatypes 
name = "Prince Chauhan" #this how we assign a string data type to a variable. 
age = 19 #this is how we assign a integer datatype to a variable.

# now we can use this variable in our code as shortcut by using argument specifiers like this
print("my name is %s and I'm %d years old nice to meet you everyone"%(name, age))
 
# there are many data types in python for example 
list_of_datatypes_in_python = ["a", 2, 2 + 5j ,{"key":"value"}, True, {1,2,3,4}, (1,2,3),[1,2,3,4,5]]

# let's try to run a for in loop for the list_of_datatypes_in_python
print("these are some datatypes")
for i in list_of_datatypes_in_python:
    print(i)
print("these are the types of the above datatypes respectively")
for i in list_of_datatypes_in_python:
    print(type(i))