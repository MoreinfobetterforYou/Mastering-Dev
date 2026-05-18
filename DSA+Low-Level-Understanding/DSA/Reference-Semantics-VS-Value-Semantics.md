# Reference Sematics VS Value Semantics:
In computer science we study two main types of semantics: reference semantics and value semantics.

---

## Semantics:
Semantics is the study of meaning in programming languages. It defines the different constructs and rules that govern how a programming language behaves. It is important to understand the semantics of a programming language in order to write correct and efficient code.

---

## Value Semantics:
Value semantics typically deals with primitive and non-mutable data types such as integers, floats, and booleans. When you assign a value to a variable, you are creating a named container that holds the value. Properties:
* ### Assignment: 
    When you use the assignment operator to assign a value to a variable, you are actually creating a new named collection that holds that value. For example, in Python:
    ```python
    x = 5 # This creates a new variable x that holds the value 5
    ```

* ### Mutability:
    Value semantics typically involves immutable data types, meaning that once a value is assigned to a variable, it cannot be changed. For example, in Python:
    ```python
    x = 5 # This creates a new variable x that holds the value 5
    x = 10 # This creates a new variable x that holds the value 10, the original value 5 is not changed
    ```

* ### Equality: 
    Two different variables that hold the same value are considered equal. For example, in Python:
    ```python
    x = 5
    y = 5
    print(x == y) # This will print True because x and y hold the same value
    ```

* ### Copying: 
    When you copy a variable that uses value semantics, you are creating a new variable that holds the same value. For example, in Python:
    ```python
    x = 5
    y = x # This creates a new variable y that holds the same value as x (which is 5)
    ```

* ### Independence: 
    The copy of the variable you created using value semantics is independent of the original variable. Changes to one variable do not affect the other. For example, in Python:
    ```python
    x = 5
    y = x # This creates a new variable y that holds the same value as x (which is 5)
    y = 10 # This changes the value of y to 10, but x still holds the value 5
    print(x) # This will print 5
    print(y) # This will print 10
    ```

---

## Reference Semantics:
Reference semantics typically deals with mutable data types such as lists, dictionaries, and objects. When you assign a value to a variable, you are creating a reference to that value that is stored in a memory location inside the computer. Properties:

* ### Assignment: 
    When you use the assignment operator to assign a value to a variable, you are creating a reference (think of the reference as a pointer or an address point or telling you the exact location where that value or thing is stored in the memory) to that value. For example, in Python:
    ```python
    x = [1, 2, 3] # This creates a new variable x that holds a reference to the list [1, 2, 3]
    ```

* ### Mutability:
    Reference semantics typically involves mutable data types, meaning that once a value is assigned to a variable, it can be changed. For example, in Python:
    ```python
    x = [1, 2, 3] # This creates a new variable x that holds a reference to the list [1, 2, 3]
    x.append(4) # This changes the value of the list that x references to [1, 2, 3, 4]
    ```

* ### Equality:
    Two different variables that use reference semantics are considered equal if they reference the same value. For example, in Python:
    ```python
    x = [1, 2, 3]
    y = [1, 2, 3]
    print(x == y) # This will print True because x and y hold the same value (the list [1, 2, 3]. However, they are not the same reference.)

    print(x is y) # This will print False because x and y do not reference the same value (they are different lists in memory even though they have the same content)

    z = x # This creates a new variable z that holds the same reference as x or you could think of it like it has the same address as x (which is the list [1, 2, 3])
    print(x is z) # This will print True because x and z reference the same value (the list [1, 2, 3])
    ```

* ### Copying:
    When you copy a variable that uses reference semantics, you aren't creating a new named memory location with that value rather you are creating a new reference (address) to the same value. For example, in Python:
    ```python
    x = [1, 2, 3]
    y = x # This creates a new variable y that holds the same reference as x (which is the list [1, 2, 3])
    ```

* ### Independence:
    The copy of the variable you created using reference semantics is not independent of the original variable. Changes to one variable will affect the other because they reference the same value. For example, in Python:
    ```python
    x = [1, 2, 3]
    y = x # This creates a new variable y that holds the same reference as x (which is the list [1, 2, 3])
    y.append(4) # This changes the value of the list that y references to [1, 2, 3, 4], which also changes the value of the list that x references to [1, 2, 3, 4]
    print(x) # This will print [1, 2, 3, 4]
    print(y) # This will print [1, 2, 3, 4]
    ```

---
## Conclusion:
In summary, value semantics and reference semantics are two different ways of understanding how data is stored and manipulated in programming languages. Value semantics involves creating new named memory locations for each variable, while reference semantics involves creating references to the same value. Understanding the difference between these two types of semantics is important for writing correct and efficient code.