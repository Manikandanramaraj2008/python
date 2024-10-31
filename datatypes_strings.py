# Python--
# Offers range of  libraries and tools that make excellent data processing,
# analysis,and visualization

# Jupyter

# Browser based interpreter interactively work with python.

# _ === use as output of previous operation

# Notebook open source, web based applications single document contain 
# Python code, output window, explanations, formula, charts. Powerful tool
# Popular w/ data scientis and AI experts for data cleaning, manipulation,
# Statistical modeling, machine learning, AI. Needed for developing and presenting 
# AI models and projects. 

# DATA Types
#Text -- string  / character
# Numeric--- integer / float / complex
# Sequence --list , tuple , and range
# Mapping -- dictionaries - dict
# Set == set , frozenset
# Boolean == bool
# Binary == bytes, bytearray, memoryview

# literal assignment

first_name ="Arutperunjothi"
print(first_name)

print(type(first_name))

print(first_name==int)

print(type(first_name==int))

print(isinstance(first_name,str))

#constructor function

name ="Arutperunjothi"
last_name ="sidhivalakam"

# print (name + ","+ last_name + "!!!")  # to add comma

full_name =  name + " "+ last_name + "!!!"  # concatenation
print (full_name)

# casting number to string

decade = str(1988)
print(decade)
print(type(decade))

statement = " i like musics from devaram"+ " " + decade +"s"
# statement = " i like musics from devaram"+ decade +"s"
print(statement)

# for multiline printing the string use triple quote
multi_line =''' I love thiruarupa, muthagha siddhi
                    suddha pranava, gnanugh thegham,
                        maranamillaperuvaluvu'''
print(multi_line)

# use  \ backslash for appostrope ,
#  use / back shalsh and t for tab space , 
# use  / back slash and n for new line

new_line =  'I am Vallalar\'s devotee \t welcome to vadaloor \n gnanugh sabai'
print(new_line)

sentence = " I am Arutperunjothi"

print(sentence.lower())
print(sentence.upper())
print(sentence.title())
print(sentence.replace("I am", "Manikandan is" ))


print(len(sentence))
sentence+= "   "
sentence = "   " + sentence

print(sentence)
print(len(sentence))  # length of the string
print(len(sentence.strip())) # remove spaces
print(len(sentence.lstrip())) # remove left spaces 
print(len(sentence.rstrip()))

sentence_1 = "Arutperunjothi"
print(sentence_1)
print(sentence_1.startswith("A")) # start letter
print(sentence_1.endswith("Y"))  # end letter

# BOOLEAN DATA TYPE

my_value = True
x= bool(False)
print(type(x))
print(isinstance(my_value,bool))

# NUMERIC DATA TYPE

# integer type

sell = 100
sell_price =int(50)
print(type(sell_price))
print(isinstance(sell,int))

# float data type

y=float(3.14)
print(type(y))

# complex data type

z=  3+14j   # for declare complex number use " J " " with num
print(type(z))
print(z.real)  # real value of complex number 
print(z.imag)  # imaginary  value of complex number 

# built in functions for numbers

print(abs(y))      # absolute number is positive number
print(abs(y* -1))   # eventhough negative number, this will return positive number

print(round(y))  # the decimal num removed
print(round(y, 1))  # 1 decimal removed

import math

print(math.pi)
print(math.sqrt(25))
print(math.ceil(y))  # round of to successor
print(math.floor(y))  # round of to integer

# casting a string to number

zipcode = "627657"
zip_value = int(zipcode)
print(zipcode)
print(type(zipcode))

print(zip_value)
print(type(zip_value))

# user input 

a= input("did you attain immortality : \n") # the next line answer
print(a)
































