# USING PRINT STATEMENT
print("HELLO WORLD!!")
# USING IF STATEMENT
if 5 > 2:
    print("5 is greater than 2")

# USING MULTIPLE IF
if 5 < 3:
    print("5 is less than 3")
if 5 > 3:
    print("5 is greater than 3")

# VARIABLE DECLERATION
x = 5
y = "HELLO LUNA!"

# PRINTING THE DECLARED VARIABLES
print(x)
print(y)

# type(var) IS USED TO PRINT THE TYPE OF THE VARIABLE var
print(type(x))
# <class 'int>

"""
THIS IS A MULTI LINE COMMENT
"""

# CASTING
a = 4      # a IS OF TYPE int
a = "LUNA" # a IS OF TYPE str
print(a)
print(len(a)) # len IS USED TO FIND THE LENGTH OF STRING
print(a[0])   # var[a] IS USED TO FIND THE CHARECTER OF var AT POSITION a+1
print(a[0:2]) #var[a:b] IS USED TO FIND CHARECTERS OF STING var FROM a+1 to b

p = str(3)   # p is '3'
q= int(3)    # q is 3
r= float(3)  # r is 3.0

# STRINGS CAN BE DECLARED USING "" OR ''
d= "LUNA MOON"
e= 'LUNA MOON'
print(d,"\n",e)

# VARIABLES CAN BE CASE SENSITIVE
f = 4
F = "MOON"  #F WILL NOT REWRITE f

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 

Rules for Python variables:

--> A variable name must start with a letter or the underscore character
--> A variable name cannot start with a number
--> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
--> Variable names are case-sensitive (age, Age and AGE are three different variables)
--> A variable name cannot be any of the Python keywords.
"""

# VARIABLE CASES IN PYTHON
"""
MULTI WORD VARIABLES CAN BE WRITTEN USING CASES IN PYTHON.
FOR EG:
CAMEL CASE:  myVariableName
PASCAL CASE: MyVariableName
SNAKE CASE:  my_variable_name
"""

# PYTHON ALLOWS US TO ASSIGN MULTIPLE VARIABLE IN THE SAME LINE
g, h, i = "VENUS", "MARS", "JUPITER"
print(g, h, i)

# WE CAN ALSO ASSIGN MUTIPLE VARIABLES THE SAME VALUE IN THE SAME LINE
G= H= I= "SATURN"
print(G, H, I)

# Python allows you to extract the values into variables. This is called unpacking.
planets = ["EARTH", "MARS", "SATURN"]
X, Y, Z = planets
print(X, Y, Z)

print(type(planets))
# <class 'list'>

#MULTIPLE STRINGS CAN BE PRINTED USING ',' OR '+'
A="EARTH "
B="IS "
C="BLUE"
print(A+B+C)
print(A, B, C)

# IF VARIABLE IS MATHEMATICAL CHARECTER
j= 10
k= 20
print(j+k)
print(j, k)

J = "BLUE"
def myfunc():
    print("LUNA LIKES " +J)

myfunc()

# IF VARIABLE IS GIVEN A DIFFERENT VALUE WHEN IT IS LOCAL, LOCAL VALUE IS USED IN THE FUNCTION
def myFunc():
    J= "EMERALD GREEN"
    print("LUNA LIKES " +J)

myFunc()

def my_func():
    global K
    K = "WINTER"

my_func()
print("LUNA'S FAV SEASON IS " +K)

# global KEYWORD CAN ALSO BE USED TO CHANGE THE VALUE OF THE GLOBAL KEYWORK INSIDE THE FUNCTION

K= "WINTER"
def my_Func():
    global K
    K = "AUTUMN"

my_Func()
print("LUNA'S FAV SEASON IS " +K)

# TUPLE DECLARATION
X= ("SUN", "MOON", "STARS")
print(type(X))
# LIST DECLARATION
Y= ["ASTERIODS", "NEUTRON STARS", "WHITE DWARFS"]
print(type(Y))
# DICTIONARY DECLARATION
Z = {"NAME" : "LUNA", "AGE" : 18}
print(Z)
print(type(Z))

# BULIT IN DATA TYPES IN PYTHON
"""
Python has the following data types built-in by default, in these categories:

1) Text Type:	str
2) Numeric Types:	int, float, complex
3) Sequence Types:	list, tuple, range
4) Mapping Type:	dict
5) Set Types:	set, frozenset
6) Boolean Type:	bool
7) Binary Types:	bytes, bytearray, memoryview
8) None Type:	NoneType
"""

# NUMERIC TYPES IN PYTHON
"""
There are three numeric types in Python:
--> int
--> float
--> complex
"""
l = 1    # INTEGER
m = 2.8  # FLOAT
n = 2j   # COMPLEX

# RANDOM NUMBERS
import random
print(random.randrange(1,10))
# int, string
L= int(100.3)
print(L)

M = '''Audere est faucere.
Non ducor, duco.'''
print(M)

"""" ARRAYS: 
-->Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
-->However, Python does not have a character data type, a single character is simply a string with a length of 1.
-->Square brackets can be used to access elements of the string."""
N = "HOLA! LUNA"
print(N[3])

""" LOOPING THROUGH A STRING:Since strings are arrays, we can loop through the characters in a string, with a for loop. """
for o in "Blue Berry":
    print(o);
#_____________________________________________________________________________________________________________________________________________
# CHECK IF A STRING/ CHAR ARE PRESENT IN A STRING
worD= "Blue berries are the best things"
print("b" in worD)
if "b" in worD:
    print("Luna loves Blue Berries")
print("worst" not in worD)

# STRING SLICING
print(worD[2:11])

print(worD[:11])   # SLICE FROM THE START
print(worD[10:])   # SLICE TO THE END
print(worD[-2:-3]) # USE -VE INDEX TO START THE SLICE FROM THE END OF THE STRING

# CASES OF STRING
O = "Ciao! Luna"
# UPPERCASE
print(O.upper())
# lowercase
print(O.lower())

# REMOVES WHITESPACE FROM THE BEGINNING OR THE END OF THE STRING
t = " ASTERIA "
print(t.strip())

# replace() METHOD REPLACES A STRING WITH ANOTHER STRING
print(worD.replace("e", "Z"))

"""
split() splits the string into substrings if it finds instances of the separator
"""
print(t.split("T"))