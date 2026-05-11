# Tuples: A tuple is a finite ordered sequence of values. The term "tuple" comes from mathematics. Tuples are immutable (just like strings which means once they have been created their value can't be changed or else it would result in a TypeError) ordered sequence of values (these values can be duplicate) seperated by comma inside a pair of parenthesis ().

# How to Create a Tuple:
    # 1) Tuple Literals: A tuple literal is when you create a tuple by explicity writing out values or items seperated by comma surrounded by a pair of parenthesis.
my_tuple: tuple = ("I", "do", "it", "anyways") # This creates a tuple containing words I do it anyways. You can confirm if what you created is a tuple using the type() function:
print(type(my_tuple)) # Output: <class 'tuple'>

    # 2) The tuple() Constructor: The tuple() constructor is a built in constructor that allows you to convert an iteratable into a tuple, if no iteratable is given it returns an empty tuple. It requires a single parameter which needs to be an iteratable otherwise you can't give it a single value (such as an integer) and expect it to convert it into a tuple. You need an actual iteratable. If you still do that the python interpreter will through a TypeError.
forming_a_tuple: tuple = tuple([1, 2, 3])
print(forming_a_tuple)

# Finding the Length of Tuples: Just like lists and strings you can find the length of a specific tuple by using the len() function which returns the length of the given argument.
length_of_my_tuple: int = len(my_tuple)
print(length_of_my_tuple) # Output: 4

# Selecting a specific element in a tuple using Index: Tuples in python support index selection. Each element or item in a tuple is ordered using an index which starts from 0 to (length of the tuple - 1). 
second_word: str = my_tuple[1]
print(second_word) # Output: "do"

# count(): The count() method is used to count the number of times a specific element or value is repeated:
times_repeated = my_tuple.count("I")
print(times_repeated)

# index(): The index() method returns the index of the first ever occurence of a specific value or element in a list:
index_of_I = my_tuple.index("I")
print(index_of_I)

# sorted(): The sorted() function in python is used to return a new sorted version of the iterable as a list in python:
sorted_list = sorted(my_tuple) # returns it as a list
sorted_tuple = tuple(sorted_list) # We need to convert the list into a tuple.
print(f"The sorted my_tuple is: {sorted_tuple}")

# slice(): The slice() function in python is used to return a sliced object, in simpler terms it is used to extract a specific part of a data structure. It takes three parameteres: (start, stop, step)
    # Long syntax: 
slice_of_my_tuple = slice(0, 2)
actual_slice_of_my_tuple = my_tuple[slice_of_my_tuple]
print(actual_slice_of_my_tuple)

reversed_Tuple = my_tuple[::-1]
print(reversed_Tuple)

# Tuples Are Iteratable: As tuples are also data structures you are able to iterate over them in the same way you are able to iterate over other data strucutures like lists or strings:
for word in my_tuple:
    print(word)

# Packing Tuples: There is another way to create tuples in python by using tuples packing. Tuple packing is the process of grouping or packing several indiviuals values into a single tuple:
coordinates_of_my_point = 16, 41
print(coordinates_of_my_point) # You can confirm if you formed a tuple by using the built-in type function.

# Unpacking Tuples: As there is packing tuples this only suggests that there is also the ability of unpack tuples. Unpacking tuples allows you extract those values back into indiviual variables:
x_coordinates, y_coordinates = coordinates_of_my_point
print(f"The x coordinates are: {x_coordinates}, The y coordinates are: {y_coordinates}")

# Converting a tuple into a string:
    # 1) Using the .join() method: The syntax for this method is: seperator.join(your_tuple). It is an important thing to note that this only works if the elements of your tuple are all strings:
string_of_my_tuple = " ".join(my_tuple)
print(string_of_my_tuple) # Output: I do it anyways

    # 2) Using the .join() method with map(): The syntax for this method is: seperator.join(map(str, your_tuple)). This syntax is best for if your tuple contains different data types, the map() method applies a specific transformation function to each item in an iteratable:
every_data_type = ([1, 2, 3], "hi", TypeError, 4.5, 7, True)
string_of_every_data_type = ", ".join(map(str, every_data_type))
print(string_of_every_data_type)

# Checking if a given item is in the tuple or not: You can use the "in" keyword to check if a given item or element is found within a tuple or not. In this example we are gonna level up the game a bit instead of simple examples we are gonna include functions, documentation, type hints, and everything else in between:
def digits_of_decimal() -> tuple:
    """This function uses the tuple constructor to convert the range object from the range() function into  a tuple."""
    return tuple(range(0, 10))

digits_of_decimal_number_system: tuple = digits_of_decimal()

def is_digit_in_username(username: str) -> bool:
    for digit in digits_of_decimal_number_system:
        if str(digit) in username:
            return True
    return False

def user_name_auth() -> bool:
    """This function first asks the user your their username and then checks if the given username is valid or not by using a combination of try/except and calling another function"""
    while True:
        username = input("\n What is your username? (Your username can only include characters no numbers): \n\t")
        username = username.strip()
        boolean = is_digit_in_username(username)
        if not username:
            print("Please enter a username. ")
        elif boolean:
            print("Please enter a valid username. (Don't enter a number)")
        else:
            print(f"Your username is: {username}")
            return username

valid_username = user_name_auth()
print(f"Successfully added user: '{valid_username}' to the database.\n")

# This is one method to check if a particular string contains a number or not. A more efficient way to implement this is to use the any() function. The any() function in python checks if any value in an iteratable is true and returns true if it finds a True value. To check if a particular character is a digit we use isdigit() function to check for this case.
def check_for_digit(username) -> bool:
    return any(char.isdigit() for char in username)

def ask_user() -> str:
    while True:
        username = input("\nEnter your username: \n\t")
        username = username.strip()
        if not username:
            print("\nEnter a username!!!")
        elif check_for_digit(username):
            print("\nEnter a valid username. (Username can't contain a number)")
        else:
            print(f"Your username is: {username}")
            return username
        
valid_username = ask_user()
print(f"Successfully added user: {valid_username} to the database.")

# Nested Tuples: Nested Tuples are essentially tuples inside other tuples. For example, this is a tuple of x and y coordinates stored as tuples in a tuples.
coordinates = ((1, 2), (4, 5), (-1, -5), (-4, -2))
x_coordinate_of_4th_point = coordinates[3][0]
print(f"The x coordinate of the 4th point is: {x_coordinate_of_4th_point}")

# Single Element Tuples: There is an important thing you need to know before creating single element tuples. Tuples with a single element such as lets say an integers have the data type of an integer rather than a tuple to actually create a single element tuple you need to have a trailing comma after that element:
not_single_integer_tuple = (5) # You may think that this is a tuple but it actually is not and you check it by using the type() function:
print(type(not_single_integer_tuple)) # Output: <class 'int'>

single_integer_tuple = (5,) # This is the actual way to create a single element tuple by using a trailing comma after it.
print(type(single_integer_tuple))

# Performance of Tuples: 
    # Memory Efficiency: Tuples are better than lists in terms of memory efficiency. This is because tuples occupy the exact space needed for the elements inside them, they don't occupy excess space. Lists on the other hand over allocates space in the memory to account for future operations. We can check this by the .getsizeof() method from the sys module:
import sys
same_list = [1, 2, 3]
same_tuple = (1, 2, 3)
print(f"Size of the list is: {sys.getsizeof(same_list)} bytes")
print(f"Size of the tuple is: {sys.getsizeof(same_tuple)} bytes")

    # Creation Speed: Tuples can be initialized faster than lists. Tuples are approximately 86% faster in creation speed than lists. This is because python is able to reuse existing tuples to create new ones, whereas with lists you need to create a new list every time and also need to allocate additional space for future operations. We can check this by using the timeit module:
import timeit
print(f"Time taken to initialize list is: {round(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]'), 3)}s")
print(f"Time taken to initialize tuple is: {round(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)'), 3)}s")

# ---------------------------------------- Important Note --------------------------------------------
# You can have trailing commas in tuples, this helps in inserting or removing items because all the elements of a tuple or lines look the same way.

# Similar to *args (arbitary arguments) in functions in python you can also perform the same thing in unpacking tuples allowing you to grow multiple values when unpacking a tuple. If you don't use this method it is important to ensure that the number of variables you use when unpacking the tuple is equal to the number of values of the tuple:
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_Number, *middle_Numbers, last_Number = numbers
print(f"The first number in the tuple is: {first_Number}, The middle numbers in the tuple are: {middle_Numbers}, The last number in the tuple is: {last_Number}")