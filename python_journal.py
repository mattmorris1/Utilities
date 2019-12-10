#!/usr/bin/env python
# coding: utf-8

# In[8]:


test = "hello world how are you?"
test_count = test.count(" ") + 1
print(test_count)

#another way to do it?
def return_number(test_string):
    return len(test_string.split())
return_number(test)


# In[9]:


ar = [1,2]
print(len(ar))
print(len("hello"))

def num_of_strings(sentence):
    array_words = sentence.split(" ")
    print(array_words)
    if(len(array_words) > 5):
        print("long sentence")
    return len(array_words)

print(num_of_strings("hello world how are you today?"))


# text explaining what code does (in markdown)

# In[10]:


#variables wow
myint = 7
#print statements wow
print(myint)


# In[11]:


#ways to do floats
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)


# In[12]:


#strings are single or double quotes
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)


# In[13]:


#Double quotes needed to use apostrophes
mystring = "Don't worry about apostrophes"
print(mystring)


# In[14]:


#Operators can be done on numbers and strings
one = 1
two = 2
three = one + two
print(three)
#also multiple variables can be declared simultaneously on one line
hello, world = "hello", "world"
helloworld = hello + " " + world
print(helloworld)


# In[15]:


#Can't mix operators for numbers and strings
one = 1
hello = "hello"
print(one + hello)
#This will break


# In[17]:


#building a list. Lists can hold different variables and be accessed easily
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)


# In[22]:


# % sign prints the remainder of first number divided by second number
remainder = 11 % 3
print(remainder)


# In[24]:


#Two multiplication symbols allows you to use #1 to power of #2
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)


# In[26]:


#can combine strings together with +
helloworld = "hello" + " " + "world"
print(helloworld)


# In[29]:


#You can also multiply strings if needed
lotsofhellos = "hello " * 10
print(lotsofhellos)


# In[31]:


#Lists can be joined with operators
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


# In[34]:


#Also you can multiply lists like strings
print([1,2,3] * 3)


# In[47]:


# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)
# %s is for strings or any object with string representation like numbers
# %d is for integers
# %f is for floating point numbers
# <number of digits>f is for floating points with a fixed amount of digits
# to the right of the dot
# %x%x is for integers in hex representation (lowercase/uppercase)
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)


# In[65]:


### astring = "Hello world!"
print("single quotes are ' '")
#prints how long the string is including punctuation and spaces
print(len(astring))
#Prints first location of specified character
print(astring.index("o"))
#Counts number of specified characters in string
print(astring.count("l"))
#Prints the characters from the 3rd place to the 6th place. Leave front blank
#to count from start and end blank to go to end. Use - numbers to find 
#character in relation to the end. Use one number to print one character
print(astring[3:7])
#Same as above but skips by specific ammount [start:stop:step]
print(astring[0:7:2])
#This lets you reverse a string
print(astring[::-1])
#These print strings in all uppercase or lowercase
print(astring.upper())
print(astring.lower())
#Prints whether something starts with or ends with something respectively
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
#Splits the string into a list of strings using the specified character
afewwords = astring.split(" ")
print(afewwords)


# In[74]:


#Python uses booleans to evaluate conditions. True or false.
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
#And/or can be used when evaluating variables
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
#"In" operator looks for object in a specific container like a list
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
#Indentations used for code blocks. If, else if and else statements
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass
# "Is" checks if two things are the same instance, not if they're equal
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
#Not operator inverts a boolean
print(not False) # Prints out True
print((not False) == (False)) # Prints out False


# In[80]:


#Python has two types of loops. For and while
#For loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
#For can use range to iterate through a sequence
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
#While loop
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
#Break is used to exit a loop, continue is used to skip the current block and
#return to the for/while statement
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
#Python can use else statements in conjunction with loops
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


# In[89]:


#How to define a function. Function includes everything indented
def my_function():
    print("Hello From My Function!")
#Functions can be given arguments/parameters like so
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
#Functions can return value to the caller using the return keyword
def sum_two_numbers(a, b):
    return a + b
#Functions are called by writing the name and then () with any arguments in
#the brackets
my_function()
my_function_with_args("example_username", "sup")
x = sum_two_numbers(1,2) #sum now holds 3

