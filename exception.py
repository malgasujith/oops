
# try block: The code that might raise an exception.
# except block: Handles specific exceptions.
# else block: Runs if no exceptions were raised in the try block.
# finally block: Runs no matter what, useful for cleanup.
# raise: Used to throw exceptions manually.
# This approach helps in managing and controlling errors

try:
    file = open('myfile.txt', 'w')
    file.write('Hello, world!')
except IOError as ex:
    print(f"Error occurred: {ex}")
finally:
    print("Cleaning up...")
    file.close() 

# types of errors 
1) Syntax Errors
2) Exceptions
1. Syntax Errors
A SyntaxError occurs when the Python interpreter encounters invalid syntax in the code. This usually happens when the code doesn't follow the proper structure of the language.


if True
    print("Hello, world!")  # Missing colon after 'if' statement
Output:

arduino

2. Exceptions
Exceptions are errors that occur during the runtime of a program. Python provides various types of exceptions, and they can be caught using try and except blocks.

a) NameError
Occurs when you try to use a variable or function that has not been defined.

print(x)  
Output:


b) TypeError
Occurs when an operation or function is applied to an object of inappropriate type.

python

result = 'hello' + 5  # Cannot concatenate string and integer
Output:


c) ValueError
Occurs when a function receives an argument of the right type but inappropriate value.

int('abc')  # Cannot convert string 'abc' to integer
Output:

csharp
Copy code
ValueError: invalid literal for int() with base 10: 'abc'

d) IndexError
Occurs when you try to access an index that is outside the range of a list or sequence.

lst = [1, 2, 3]
print(lst[5])  # Index 5 does not exist in the list
Output:

sql
Copy code
IndexError: list index out of range
e) KeyError
Occurs when a dictionary key is not found.

python
Copy code
# KeyError Example
d = {'name': 'Alice'}
print(d['age'])  # Key 'age' does not exist in the dictionary
Output:

vbnet
Copy code
KeyError: 'age'
f) AttributeError
Occurs when an invalid attribute reference is made, such as trying to call a method on an object that doesn’t exist.

python
Copy code
# AttributeError Example
lst = [1, 2, 3]
lst.append_item(4)  # 'list' object has no attribute 'append_item'
Output:


g) ZeroDivisionError

Occurs when you try to divide a number by zero.

python
Copy code
# ZeroDivisionError Example
result = 10 / 0  # Division by zero

python
Copy code
# FileNotFoundError Example
file = open('nonexistent_file.txt', 'r')  # File does not exist
Output:



