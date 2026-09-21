# Python Best Practices

## General
### Naming Variables
When naming a variable, it should follow these recommendations:

* `snake_case` (all lowercase with words separated by underscores `_`)
* descriptive nouns or noun phrases
* full words, avoid abbreviations or single character names
* Single characters are only acceptable when they are commonly recognized as a regularly used value:
  * `x`, `y`, `z` for coordinates.
  * `i`, `j`, `k` for iteration control structures.
  * `n` for a number of terms.
  * `a`, `b`, `c` for mathematical numbers used in calculations.
  * `w`, `h` for width and height.

```python
# GOOD:

my_variable = 8
variable = 8
my_favourite_number = 8

# Below single characters are used instead of full words.
# This is okay because x and y are commonly associated with coordinates.
x = 200
y = 100
```

```python
# BAD:

my_var = 8        # Uses abbreviation.
myvariable = 8    # Does not use snake_case.
MyVariable = 8    # Does not use snake_case, uses capital letters.
myVariable = 8    # Does not use snake_case, uses capital letters.
v = 8             # Single character used as variable name.
silly = 8         # Not a descriptive noun or noun phrase.
```

### Naming Functions
When naming a function, it should follow these recommendations:

* `snake_case` (all lowercase with words separated by underscores `_`)
* descriptive verbs or verb phrases
* full words, avoid abbreviations or single character names

```python
# GOOD:

def get_user_name():
    return input("Enter your name: ")

def add_ten(value):
    return value + 10

def set_turtle_color(color):
    my_turtle.color(color)
```

```python
# BAD:

def name():                 # Not a descriptive verb or verb phrase.
    return input("Enter your name: ")

def ADDTEN(value):          # Does not use snake_case or lowercase characters.
    return value + 10

def setTurtleColor(color):  # Uses uppercase letters and does not use snake_case.
    my_turtle.color(color)

def f():                    # Function named with a single character.
    return True
```

### Naming Constants
When naming a constant, it should follow these recommendations:

* `UPPER_SNAKE_CASE` (all uppercase with words separated by underscores `_`)
* descriptive nouns or noun phrases
* full words, avoid abbreviations or single character names

```python
# GOOD:

MY_CONSTANT = 20
MAX_HP = 100
FIRST_NAME = "Nathan"
RED = (255, 0, 0)
```

```python
# BAD:

MY_CONST = 20    # Uses an abbreviation instead of full words.
myconstant = 20  # Uses lowercase letters and does not use UPPER_SNAKE_CASE.
C = 20           # Uses a single character.
```

### Naming Classes *(Advanced)*
Eventually, you will learn about implementing classes when using object-oriented programming (OOP). Classes have different naming conventions and should follow these recommendations:

* `CapWords` (words put together with the first letter of each word capitalized)
* descriptive nouns or noun phrases
* full words, avoid abbreviations or single character names

```python
# GOOD:

class MyClass:
    pass

class ClassName:
    pass
```

```python
# BAD:

class My_Class:  # Should not use underscores to connect words.
    pass

class my_class:  # Should not use underscores to connect words.
    pass

class MYCLASS:   # Only first letters should be capitalized.
    pass
```

### Indentation
When indenting code, indentations should be 4 spaces. Most editors will have this as a default for when you press `Tab` key.

```python
# GOOD:

def my_function():
    indentation = 4

if indentation == 4:
    print("Nice indentation!")
```

```python
# BAD:

# Indentation is set to 1 space:
def my_function():
 indentation = 1

if indentation == 4:
 print("Nice indentation!")

# Indentation is inconsistent within the example:
def my_function():
    indentation = 4

if indentation == 4:
 print("Nice indentation!")

# Indentation is set to 8 spaces:
def my_function():
        indentation = 8

if indentation == 4:
        print("Nice indentation!")
```

### Using Strings
When using strings that need to contain the values of variables, formatted strings *(f strings)* are preferred over comma separation and concatenation.

```python
# GOOD:

my_number = 20

print(f"Your number is {my_number}!")
```

```python
# BAD:
my_number = 20

print("Your number is", my_number, "!")         # Adds unnecessary spaces.
print("Your number is" + str(my_number) + "!")  # Code becomes more difficult to read.
```

### Comments
When adding comments, the best practice is to add block comments that describe what code does in plain language. 

* Comments should not restate what the code does but explain its purpose. 
* Block comments are preferred over inline comments and describe the block of code beneath them. 
* Inline comments can be used when absolutely necessary.
* Inline comments should have 2 spaces between them and the code they are referring to.
* Comments should be written in full sentences with punctuation and capitalization.

```python
# GOOD:

# A beginner practice exercise for using input and output.
name = input("What is your name? ")
print(f"Hello {name}!")

x += 1     # Compensate for border.
y = x + 2  # Compensate for top and bottom border.
```

```python
# BAD:

# practice code
name = input("What is your name? ")
print(f"Hello {name}!")

# Ask user for input, then print "Hello" with their name.
name = input("What is your name? ")
print(f"Hello {name}!")

name = input("What is your name? ")  # Ask for user input
print(f"Hello {name}!")  # Then print "Hello" with their name

x += 1#Increment x
y = x + 2#Add x + 2

x += 1  # Compensate for border.
y = x + 2  # Compensate for top and bottom border.
```

## Function Definitions

To master function definitions, there are 3 key components your function definition must include:

* Type hints for your parameters
* Type hints for your return
* A docstring to explain it

Including these 3 components leads to clearer, cleaner, more maintainable code.

### Parameter Type Hints
Parameter type hints make it easier to remember what kind of data a function expects.

```python
# GOOD:

def add_ten(number: float) -> float:
    """
    Add 10 and return the value.

    :param number: The starting number.
    :return: Ten more than the starting number.
    """
    return number + 10
```

```python
# BAD:

def add_ten(number) -> float:
    """
    Add 10 and return the value.

    :param number: The starting number.
    :return: Ten more than the starting number.
    """
    return number + 10
```

### Return Type Hints
Return type hints make it easier to remember what kind of data a function will give you.
```python
# GOOD:

def add_ten(number: float) -> float:
    """
    Add 10 and return the value.

    :param number: The starting number.
    :return: Ten more than the starting number.
    """
    return number + 10

# For a function with no return, use None
def add_greet(name: str) -> None:
    """
    Print a message to the given name.

    :param name: The starting number.
    :return: None
    """
    print(f"Hello {name}!")
```

```python
# BAD:

def add_ten(number: float):
    """
    Add 10 and return the value.

    :param number: The starting number.
    :return: Ten more than the starting number.
    """
    return number + 10
```

### Docstrings
Docstrings allow you to remember what a function does, as well as what the inputs and outputs each do.
```python
# GOOD:

def add_ten(number: float) -> float:
    """
    Add 10 and return the value.

    :param number: The starting number.
    :return: Ten more than the starting number.
    """
    return number + 10
```

```python
# BAD:

def add_ten(number : float) -> float:
    return number + 10
```

## Ordering Code

### Without `if __name__ == "__main__":`
Code should be ordered with the following pattern:

```text
Document Level Docstring
Module Imports
Partial Module Imports
Constant Initialization
Variable Initialization
Function Definitions
Main Code
```

For example:
```python
"""
Example of Document Structure
Author: Nathan Forsyth
"""

import math

from sys import exit

EXPONENT = 2
ANGLE_DEGREES = 180

operation_count = 0

def get_radians(angle: float) -> float:
    global operation_count
    operation_count += 1
    return math.radians(angle)

def get_square(base: float) -> float:
    global operation_count
    operation_count += 1
    return math.pow(base, EXPONENT)


print(f"3^2: {get_square(3)}")
print(f"{ANGLE_DEGREES} in radians: {get_radians(ANGLE_DEGREES)}")
print(f"90 in radians: {get_radians(90)}")
print(f"Total operations: {operation_count}")
exit()
```

### With `if __name__ == "__main__":`
Code should be ordered with the following pattern:

```text
Document Level Docstring
Module Imports
Partial Module Imports
Constant Initialization
Global Variable Initialization
Function Definitions
Main Function Definition
    LOCAL Variables Initialized in Main Function
if __name__ == "__main__":
```

For example:

```python
"""
Example of Document Structure
Author: Nathan Forsyth
"""

import math

from sys import exit

EXPONENT = 2
ANGLE_DEGREES = 180

operation_count = 0

def get_radians(angle: float) -> float:
    global operation_count
    operation_count += 1
    return math.radians(angle)

def get_square(base: float) -> float:
    global operation_count
    operation_count += 1
    return math.pow(base, EXPONENT)

def main():
    print_count = 0
    print(f"3^2: {get_square(3)}")
    print_count += 1
    print(f"{ANGLE_DEGREES} in radians: {get_radians(ANGLE_DEGREES)}")
    print_count += 1
    print(f"90 in radians: {get_radians(90)}")
    print_count += 1
    print(f"Total operations: {operation_count}")
    print_count += 1
    print(f"Total prints: {print_count + 1}")
    exit()

if __name__ == "__main__":
    main()
```