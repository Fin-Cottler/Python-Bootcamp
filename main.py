from dog import Dog

# this is a comment. No code is run

'''
This is a multiline comment
I can write down here
and no code is run
'''

######################################################

'''  
these are prim  itive data types

int - integer 
  ex. 10

string - characters 
  ex. "hello, I am a string"
it is in quotes

float - non integer number
  ex. 15.25

boolean - True or False
'''

######################################################

''' Variables are 'titles' assigned a value. '''

my_var = None
''' ^ This is a variable that has no value ^  

We can assign value to this variable
'''
my_var = "A string"


'''These variables have primitive data type values'''
my_integer = 33
# integer value

my_string = "33"
# string of characters

my_float = 33.1
# non-integer numerical value

my_boolean = True
# True or False 

'''
Variables can have literally any name
here is an example
'''
phoogle_noogle_loogle = False

'''as seen above, in python the standard naming convention is word_word_word with no capital letters'''


'''
Write some practice variables and assign them value
'''

######################################################

'''
We can also 'print' values
write the following line to see what happens
'''

print("Hello World")

'''
this line prints a string. 
We can print any primitive data type. 
Try printing the 4 primitive data types we learned
'''

print("My String")
print(145)
print(12.5)
print(False)

'''What if we want to print a variable?'''

my_var = "A string"
print(my_var)

'''^ try now ^'''

'''We can add line breaks in multiple ways'''
print("hello")
print("ok")
#example of a line break

print("hello \n ok")
#\n signifies line break. note that spaces are included when printing

'''
the best part of python (in my opinion) is called an fstring
fstrings are similar to regular strings because they contain a 'string' of characters
the benefit of the fstring is that variable values may be added into the string as well
these values will be encased in brackets like this: {var}
'''
my_var = 33

print(f"my_var has a value of: {my_var}")

'''as seen above, fstrings are denoted with the letter 'f' before the quotes'''

#^ Try it now ^

######################################################

'''Math can be done'''

'''
Basic Operators
+ addition
- subtraction
* multiplication
/ division
% modulo (returns the remainder after division)
** exponent
'''

'''here are some examples'''
print(2 + 1)
print(2 - 1)
print(2 * 3)
print(2 / 3)
print(3 % 2)
print(2 ** 3)

'''math can be done with variables'''

num1 = 2
num2 = 6

print(num1 - num2)
print(num2 / num1)

'''many operators are not "built in" to python so we need to import the 'math' module'''

import math

'''
now we can use operations like square root. 
we call these operators like this
'''

print(math.sqrt(4))

'''
Try using 3 operations found in the math module
https://www.w3schools.com/python/module_math.asp
'''

######################################################

'''
User input can be helpful by allowing the user to provide values that python can use
'input()' is a method that returns the users input in the console
this means we will need to set a variable to the value of the users input
'''

print("Type anything")
user_input = input()
print(user_input)

#the user's input is printed
#this code can be rewritten like this

user_input = input("Type anything\n")
print(user_input)

#lets try performing math on a user input

user_input = input("Type a positive integer\n")
print(user_input / 2)

#this will give us an error

#by default, user inputs are strings so math cannot be performed.
#We can solve this by 'casting' the input to an integer (this will be talked about more in the future)

user_input = int(input("Type a positive integer\n"))
print(user_input / 2)

#the input is casted to an integer allowing us to perform math


###############################################################

'''conditionals'''

'''
if statements are an important part of code
they are used to check IF a condition is satisfied 
'''

'''
common conditions are:

== is equal to
> is greater than
< is less than
>= is greater or equal to
> is less or equal to
'''

'''here is an example'''

var1 = 2
var2 = 4

if var1 >= var2:
  print(True)

'''Notice that the colon signifies the following code will be run. Colons are used often in python'''

'''
try writing your own if statement
if your condition is met print hello
'''

'''
else if and else
if we want to test multiple conditions and have different outcomes for each we use else if and else

if else - checks an alternative condition
else - if no conditions are met run this instead

they are written as follows:
'''

if var1 == var2:
  print(f"{var1} is equal to {var2}")
  # note the fstring
elif var1 > var2:
  # else if is shortened to elif
  # you can write as many 'elif' statements as you want before your else statement
  print(f"{var1} is greater than {var2}")
else:
  print("no conditions were satisfied")

'''try writing your own if, else if, else statments'''


######################################################

'''
Lists 
Python lists can store multiple values

this is an empty list
'''
my_list = []
'''lists have brackets'''

'''
here is an example of a list with values (a list of strings)
'''

colors = ["red","orange","yellow"]


print(colors)
'''this list will be printed'''

'''
note: all items in a list have an 'id' called an index.
indicies start at 0 and count up

in the colors list: the index of red is 0, orange - 1, yellow - 2
'''


'''
lists can have any type of data, even variables
'''
 

'''try making your own list'''

'''we can add items to a list with the append method'''

colors.append("green")
#note: the method is called by specifying the list then the method then the methods respective parameters
'''
list - colors
method - append()
parameter - "green" (what we wanted to add)
'''

print(colors)
'''green was added to the colors list'''

'''
there are many other list methods

append() - Adds an element at the end of the list
clear() - Removes all the elements from the list
copy() - Returns a copy of the list
count() -	Returns the number of elements with the specified value
extend() - Add the elements of a list (or any iterable), to the end of the current list
index() -	Returns the index of the first element with the specified value
insert() - Adds an element at the specified position
pop()	- Removes the element at the specified position
remove() - Removes the first item with the specified value
reverse() - Reverses the order of the list
sort() - Sorts the list
'''

'''using google as a resource try using 3 of these methods on the list you made earlier (sort is more complicated I would not recommend using it right now)'''

##############################################################

'''
loops
Loops are used to execute code multiple times

2 types of loops 
for loop - loops a set amount of times (definite end)
while loop - loops while a condition is true (indefinite end)
'''

'''BASIC FOR LOOP WITH RANGE'''
for x in range(10):
  print(x)
  #tab in to signify code is 'inside' for loop. This rule applies to all python
  
  
'''run this code to see what happens'''

'''
x is a variable that equals every value from 0 to 10 uninclusive 
and runs the code each time
'''

'''Iterating through a list'''
colors = ["red","orange","yellow","green","blue","purple"]
# we will iterate through this list

for x in colors:
  print(x)

# We can change 'x' to anything because its a variable name. 
# perferably something that makes sense

for color in colors:
  print(color)
# this does the same thing 

'''
Note, all for loops iterate through lists

even though at first glance, the range method does not look like a list it actually is
the range(N) creates an N long list of integers from 0 to N uninclusive
'''

'''We can use for loops to search'''
# lets find all colors with o in them using .__contains__()

for color in colors:
  # we will use an if statement 
  if color.__contains__("o"):
    print(color)
  # there is no else statment because if the condition is not satisfied 
  # we dont want any code to run


'''
While loops. These run while a condition is met. 
Be careful of infinite loops (When the condition is always true)
'''

'''Here is an example'''
x = 0
while x < 10:
  print(x)
  x += 1
  # this is a shorter version of x = x + 1
  # we must add to x after every iteration or x will always be less than 10
  # this results in an infinite loop

'''try writing a for loop and while loop'''

############################################## 

'''
objects

We will be writing code in a new python file. 
Create a new file called 'dog.py'
'''

dog1 = Dog("Golden Retriever",6,28.5,True)
'''try creating 2 more dogs'''

print(dog1) 
'''does not print what we want'''

dog1.get_breed()
'''
We do not put the self parameter in the parentheses 
even though we will specify any other parameters
'self' is defined by dog1 as that is the object we call the method on
'''
# Run the code. notice that nothing happens.
# this is because we are only returning the value but we did not print it

print(dog1.get_breed())

dog1.set_breed("Some other dog breed")
# set the breed

print(dog1.breed)
# check to see if the breed was actually changed
