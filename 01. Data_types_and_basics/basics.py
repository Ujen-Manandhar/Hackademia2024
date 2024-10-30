print("hello world")

# every syntax has its own code
# hover in the code gives every detail of the function
# '#' to write comments and are skiped also known as inline comments (works in a particular line only)

"""
3 double inverted commas 
multiple lines comments 
comments works in multiple line

"""

x = 10
#python has abstraction
print(type(x))
# type helps to identify the type of data type

x = 10.5 # float number with decimal
print(type(x))

# cordinate system as decimal can bring error and as such float is used for no margin of error
# python is a intreperated language as such is run line by line and variable can change easily

x = 'a' # string 
x = int('1') # convert string to int 
# data type conversion is easy in python 

x = 10
y = 20
print(x+y) # sum 

x = 'a'
y = 'pple'
print(x+y) # concat join the two strings 

x = 10
y = 20
print(x+y) # sum 
print(x-y) # substract
print(x/y) # divide
print(x*y) # multiply


#approch
print(f'{x/y}: divide,\n{x*y}: multiply,\n{x+y}: add')
print('add'+str(x+y)) # convert to string after adding 

# input and output:
input_from_user = input("Enter your name: ") # ctrl and click code then leads to documentation
# the input function takes input from user
# the input goes to the input variable the input is always a string 

num1 = int(input("enter number: "))
num2 = int(input("enter second number: "))
print(num1+num2)

#bolean is True or False

# write a program for simple intrest 
principle = float(input("enter the principle: "))
time = float(input("enter the time period: "))
rate = float(input("enter the rate: "))/100

simple_intrest = principle * time * rate
print(
    f'principle: {principle},
    \ntime: {time},
    \nrate: {rate},
    \nintrest amount: {simple_intrest},
    \nAmount: {principle+simple_intrest}'
      )
