# data_types.py

# Integer
my_int = 42

# Float
my_float = 3.14

# String
my_str = "Hello, world!"

# Boolean
my_bool = True

# List
my_list = [1, 2, 3, 4, 5, 1, 2, 3]
#list doesnt print out repeated values rather it prints unique values
print ("list:" ,my_list[3])
# Tuple
my_tuple = (10, 20, 30)
# Tuples are immutable, meaning they cannot be changed after creation
# and they can contain duplicate values
print("Tuple:", my_tuple[1])

# Dictionary
my_dict = {"name1": "Alice", "age": 30, "city": "New York","name": "Bob", "age": 25, "city": "Los Angeles", "name": "Charlie", "age": 35, "city": "Chicago"}
print("dictionary:", my_dict["age"])#prints out the last age in the dictionary so you have to specify 
# Dictionaries store key-value pairs and can have unique keys

# Set
my_set = {1, 2, 3, 4}
print ("Set:", my_set[1], "Set does not support indexing")  # This will raise an error
print("Set:", my_set)  # Prints the set as a whole
# Sets are unordered collections of unique elements

# NoneType
my_none = None

# Print all data types
print("Integer:", my_int)
print("Float:", my_float)
print("String:", my_str)
print("Boolean:", my_bool)
print("NoneType:", my_none)