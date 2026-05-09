# Function are a reuseable block of code that performs a specific tasks or calculates a value. Functions in python are created using the "def" keyword followed by the name of the function followed by a set of parenthesis and then a colon and then indentation in which you would place the body of the function.
def greet():
    print("Hello Hassan!")

# Invoking or Calling a function:  Is when you actually run the function by writing the name of the followed by a set of parenthesis().
greet() # This is when we actually invoke the function causing the program to print Hello Hassan!

# We can make functions more reuseable by using parameters which are placeholders for the values that will be passed when the function is called or invoked, these values are called the arguments.
def greetTheUser(userName):
    print(f"Hello {userName}!")
greetTheUser("John Doe")

# You can also give defualt value to parameters in the case if no argument was passed when the function was invoked. To specify default value to functions you write the name of the parameter followed by the default value you want the parameter to have:
def hello(userName = "Guest"):
    print(f"Hello {userName}")
hello()

# A function can also have more than one parameter which are seperated by using a comma. But one important thing that you need to consider is the fact that you need to give the arguments in the same order in which you defined the parameters.
def printInfo(userName = "Guest", age = 0):
    print(f"{userName} is {age} years old")
printInfo("Bob", 18) # In positional arguments the order matters. By default the arguments passed in most functions are position arguments.

# Keyword Arguments: Is similar to positional arguments allowing you to have more than one argument and parameter to your function but the main difference is that in positional argument the order matters while in keyword arguments you can invoke or call a function by explicitly naming the parameters thus the order of the arguments does not matter. It also helps in readability of the code.
printInfo(age = 24, userName = "John Doe")

# You can also return the value produced by a function by using the return keyword. This helps you store the value produced or calculated in a variable. You can return multiple value from a function by seperating each with a comma.
def lengthOfName(userName = ""):
    return len(userName)
numberOfCharactersInUserName = lengthOfName("John Doe")
print(f"The number of charaters in the usersName is {numberOfCharactersInUserName}")

# Specifiying the DataTypes of Parameters and Function: In python you are able to specify datatype for function parameters and the whole function using:
    # Type hints (often called type annonations). This is done by adding a colon (:) after the parameter name and then the data type. This helps you to identify errors and help in type checking. You can also -> to tell the type of value a function returns. If a function doesn't return anything like prints some value then it has the default type None
def message(userName: str) -> None:
    print(f"Welcome to the World of Python {userName}")
message("Bob")

# Arbitary Arguments: Sometimes in your program you create function and you don't know the exact number of arguments the user may pass so in such a case you use arbitary arguments. It is denoted by placing a asterik (*) before the name of the parameter.
def addTheNumbers(*numbers: int) -> int:
    return sum(numbers)
print(addTheNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))

# Docstrings and Documentation: You can add multi-line strings which are similar to comments to document what a specific function does. This helps in improving the IDE support and readability for future you and others.
def arithmeticOperations(a: int, b: int) -> tuple[int, int, int]:
    """ This function performs various arithmetic operations on the given numbers when it is called. """
    return a + b, a - b, a * b

result = arithmeticOperations(3, 6)
print(result)
sum, difference, product = arithmeticOperations(3, 6)
print(f"Sum: {sum}, Difference: {difference}, Product: {product}")

# lambda functions: A lambda function is a small, anyonymous functions that are declared using the lambda keyword. A lambda function can take any number of parameters and arguments but can only execute one expression. The result of the expression is returned automattically. It is best for short functions. The basic syntax for a lambda function is: 
add = lambda a, b: a + b
print(add(1, 2))

# Stub: A stub is a function that does nothing which is a temporary placeholder for the body of a function that will be implemented later on. It can be defined using the "pass" statement or you could use python ellipsis(...):
tasks = []
def addTask(task: str) -> str:
    """ This functions add the task inputted by the user to the list of tasks """
    ... # You could also write "pass" statement