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

# sorted(): The sorted() function in python is used to return a new sorted version of the tuple in python:
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)

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
    """This function first creates a list of the digits of the decimal number system using a for loop and then coverts the list into a tuple using the tuple constructor"""
    digits_of_decimal_number_system: list = []
    for digit in range(1, 10):
        digits_of_decimal_number_system.append(digit)
    return tuple(digits_of_decimal_number_system)

digits_of_decimal_number_system: tuple = digits_of_decimal()

def does_username_contains_Num() -> bool:
    """This function first asks the user your their username and then checks if the username contains a digit from the decimal number system or not and then returns the result as a boolean."""
    while True:
        username = input("What is your username? (Your username can only include characters no numbers)")
        username = username.strip()
        if not username:
            print("Enter a username")
            continue
        else:
            break
    for digit in digits_of_decimal_number_system:
        if digit in username:
            print("Your Username contains numbers. We don't allow any numbers in our username.")
            return False
        else:
            return True
is_number_in_username: bool = does_username_contains_Num()

# This is one method to check if a particular string contains a number or not. Now i am gonna give you an assignment for you to do. Find and document any alternative methods to check if a particular string contains a number or not.

# ---------------------------------------- Important Note --------------------------------------------
# You can have trailing commas in tuples, this helps in inserting or removing items because all the elements of a tuple or lines look the same way.

# Similar to *args (arbitary arguments) in functions in python you can also perform the same thing in unpacking tuples allowing you to grow multiple values when unpacking a tuple. If you don't use this method it is important to ensure that the number of variables you use when unpacking the tuple is equal to the number of values of the tuple:
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_Number, *middle_Numbers, last_Number = numbers
print(f"The first number in the tuple is: {first_Number}, The middle numbers in the tuple are: {middle_Numbers}, The last number in the tuple is: {last_Number}")