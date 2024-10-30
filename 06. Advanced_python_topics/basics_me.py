# List comprehensions
'''
1. List Comprehensions and Generator expressions
List Comprehensions are a consie way to create list in python 
They are faster than using a for loop to ceate a list 
'''
# creaing a  list
list_variable = [1,2,3,4] # static way of creating  a list 
list_variable = []
list_variable.append(1) # dynamic way of creation of a list
'''
From list comprehensions we are able to generate list from one line of syntax
consise way of making list with different operations
'''
odd_numbers = [i for i in range(1,10,2)] # simple syntax to create a list; It can loop inside the list creation itself
# can do various operation in list comprehensions
print(odd_numbers)

'''
List comprehension works best when we are working with very simple data modifications or conditions 
when complex conditions arises list comprehensions is difficult to code
like in multiple if.. else.. statement it might be dificult or make error
'''
a = [1,2,3,4,5]
# mini task, you have list a create list b which has each element of a squared
b = []
for i in a:
    b.append(i**2)
print(b)
#or through lst comprehension
b = [element**2 for element in a ]# basic syntax [variable_to_put_in_list operations(loop, conditions and so on)]
print(b)

# even odd using if
even_numbers = [i for i in a if i%2 == 0]
print(even_numbers)
# task if even number get its squared value elif odd number get its cube value
square_cube = [i**2 if i%2 == 0 else i**3 for i in a]
print(square_cube)


'''
Generator object similar to list comphresion
   
    - Special type of function that returs multiple value for multiple different instances using yeild
    - multiple instances called returns multiple values
    - Return isn't used Yeild value is used (ie give value)
    - Generate new result at multiple call 
    - Generate object are used as itterators for projects
    - def function_name():
        yield statement

    function is defined diffently in python in different cases
        - inside a class in oop it is called method
        - yeild is done then it is a generator
'''
print('--'*25)
# simple generator:
def simple_generator_function():
    yield 'a'
    yield 'b'
    yield 'c'
    # now a generator as yeid syntax is used 
    # the generator must give new result for the new instance for being called
    # RNG (random number generator) and generate new number non repeating 

# first approch to getting results from generator function
for value in simple_generator_function(): # generator can be iterated # the function can be called as a list 
    # generator is working as a list and give 3 values
    print(value)

# Generator
'''
Generator are used when:
    - Generator are different from basic data type as no memory is dedicated and allocated for the generator function
    - as a list has certain variable allocated in the memory
    - help save memory as variable isn't stored in the memory and that variable can be used when needed
    - Generator expressions are similar to list comprehensions but product generator object insted of a list.
    - Generators do not store their results in memory, making them more memory efficient for large data sets
    work requires to store variable without takinng memory
'''
print('--'*25)
x = simple_generator_function()
print(x) # x is a generator object and use as iterator object
print(next(x)) # next() is an iterator function shows the next variable
print(next(x))
print(next(x))
# print(next(x)) # stop iteration error
'''
loop is different from iterator 
-loop works with forloop and it starts and ends at certain threshold some works are done

while iterator
- works on the basis of us 
- as if we need only the first element we acess only the first element; where in a for loop it wasn't possible
- and if the work of the first element is done we then work on the second element till we want
- works in a sequence like a list but no memory is taken (variable storage).
- if a then no memory of b and c 
needed for memory management

generator is the object and doing next is the iterator

'''

# Generator expression can also be created by
'''
Simple way of creating generator object
Create generator object very similar to list comprehenshion
No memory is taken
'''
# generator expression
square_gen = (x**2 for x in range(10)) # isn't a tuple as there isn't a tuple comphrenshion
print(square_gen) # <genexpr> at 0x1099b3920> #generator object
print(list(square_gen))# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
Create a geneartor operator that yeilds all the even numbers using generator expression 
Create an infinite loop where user is asked to type something
if the user types next 
display the next value of the geneartor operator
when the iteration is over the loop must exit (Hint: Using try except to handle this situation) 
'''
'''
square_gen1 = (x for x in range(5) if x % 2 == 0)

while True:
    try:
        user_input = input('Enter something: ')
        if user_input == 'next':
            print(next(square_gen1))
        else:
            print(square_gen1)
            
    except:
        print("Exiting as generator are finished")
        break
'''
# Lambda
'''
Lambda: 
    -Lambda are often refered as annonymous functions
    - as function are more detail using def but lambda helps write the straight return function with simple code 
    - For very short and sweet operations / as if lambda has complicated function just write a function 
    - These functions are used in conjunction with higher level functions like map, filter, so on 
'''
print("--"*25)
x = lambda parameter: parameter**2 # works best for simple function if to much of else statement then use a function
#          parameter to send  : what to return is parameter square
print(x(5))

sum_of_2_num = lambda parameter, parameter2 : parameter+parameter2
print(sum_of_2_num(1,2))

#Task 2, Given a list_1= [1,2,3,4,5,6,7,8,9,10] create a lambda function that returns half of that value and pass 
#each element of this list to that function and save everything in new list (using list comprehension)
#list_2=[0.5,1,1.5,2,.....]

list_1 = [i for i in range(1, 11)]
half = lambda element: element/2
list_2 = [half(x) for x in list_1]
print(list_2)

# using if else inside lambda
get_greater_number = lambda x,y : x if x>y else y
print(get_greater_number(5,6))

'''
WAP to basically take in N (N= number of elements on a list)
Loop till N times and get different numbers 
put all the numbers in a list named list_variable
create a lambda function that takes in parameter 1, return 'even' if the number if even and returns 'odd' if the number is odd
using list comprehension create another list named odd_even_list it should contain all the output of lambda function 
passed over each element of list_variable
Finally create a dataframe with 2 columns , Number, Even/odd 
Number column should have list_variable on it and Even/odd column should have odd_even_list
dispaly the final dataframe
'''

user_input = int(input('Enter the number of times to loop: '))
list_variable = [int(input('Enter Number: ')) for _ in range(user_input)]
even_odd = lambda x : 'Even' if x % 2 == 0 else 'Odd'
odd_even_list = [even_odd(number) for number in list_variable]
dataframe_var = {
    'Number' : list_variable,
    'Even/Odd': odd_even_list
}
print(dataframe_var)
'''
for pandas
datframe_pd = pd.DataFrame(dataframe_var)
datframe_pd.tocsv('Data.csv', index = False)
'''

"""
for _ in range(100):

- the _ is used to denote unused variable as the _ won't be used in the entire code 

"""

# Map
'''
Map 
    - The map functionn appplies a specified function to each item of an iterable and returns a map object(an iteratot)
    contaning the results.
    - We have a function with only one argument and with map we can keep the function and list in the same 
    - the map passes the iterable to the argument one at a time and gives a iterable object
    - Map can also be used to map out 2 different parameters from 2 different collections over a function (meaning two argument then two list)
    - 
    <Syntax>
    map(function, iterable)
'''
print('--'*25)
list_of_numbers = [i for i in range(10)]
output_of_map = list(map(lambda x: x**2 , list_of_numbers))
print(output_of_map)

# map is not only use for lambda function but also functions
print('--'*25)
def add_squared_numbers(x,y):
    return x**2+y**2

list_a = [1,2,3,4,5]
list_b = [6,7,8,9,10]
answer= list(map(add_squared_numbers,list_a,list_b))
print(answer)

print('--'*25)

'''
1. Take N from user (number of elements)
2. Create a listo fo length N asking number from user(ask numbers and put it in a list)
3. Create another list of length N sking number from user (2 nd list create with first list)
4. using map figure out which from both list add up to 10. Concat the 2 numbers and display result in list

'''
user_loop_input = int(input("Enter the number of times to looop:"))
list_first = [int(input('Enter First Number: ')) for _ in range(user_loop_input)]
list_second = [int(input('Enter Second Number: ')) for _ in range(user_loop_input)]

total = list(map(lambda x, y : str(x)+str(y) if x+y >= 10 else None, list_first, list_second))
print(total)

# Filter
'''
The filter() function constucts an iterator from elements of an iterable for which a function returns true 
<Syntax>
filter(function, iterable)
    Function that returns True or False for each item

Key Points 
    - Returns a filter object 
    - If function is None , it defaults to the identity function ie it filters out element that are falsey 
    (like None, 0, False)

    - Filter works very similar to map  
    - It takes function and iterable as input # filter(function, iterable)
    - Returns output whenever its true removes unstastiy cases.
    - Write filter with mostly conditional statement 
'''
print('--'*25)

numbers = [1,2,3,4,5]

# map output [False, True, False, True, False]
even_map =map(lambda x : x % 2 == 0, numbers)
# only gives the element that are true in the function
# except giving true or false, it gives the corresponding value are only returned
# [2, 4]
even = filter(lambda x : x % 2 == 0, numbers)
print(list(even), list(even_map))
print('--'*25)

'''
Given a list = ['apple', 'ball', 'cat', 'dog', 'elephant']
create another list of words which have length > 3
'''
list_words = ['apple', 'ball', 'cat', 'dog', 'elephant']
fil_words = filter(lambda word : len(word) > 3, list_words)
print(list(fil_words))


'''
from functiontools import reduce
Reduce()
    - [1,2,3,4,5]
    - multiplication of the list
    - rather than a loop
    - we use reduce()
    <syntax>
    reduce(function, iterable, initianal_value = 0)
        def multiply (x,y)-> x*y
        reduct (multiply(), list)
    - it runs the function in one by one in cumulative way from left to right
    - [1,2,3,4,5]
    - using the function and the retun is multiply at each step to the ultimate ans[(1*2)(2*3)(6*4)(24*5)] = 120
    - if initation is 10
    - [10][1,2,3,4,5] -> (10*1)(10*2)(20*3) -> the initation is kept at the first of the list [10,1,2,3,4,5] = only one final result
    - Note: no need to convert
'''
print('--'*25)
from functools import reduce
list_of_numbers2 = [1,2,3,4,5]
multiply = reduce(lambda x, y: x*y, list_of_numbers2)
print(multiply)

'''
-Create a list taking N like done previously

-create a function square_and_add_4(x)
return x**2+4

-using map create transition_list_1 passing over 
the function 

-using filter create another transition list_2 which 
accepts only those numbers divisible by 5

-Finally create sum of all the numbers of transition_list_2
using reduce 
'''

user_loop_input2 = int(input("Enter the number of times to looop 2:"))
list_first1 = [int(input('Enter Number: ')) for _ in range(user_loop_input2)]
transition_list_1 = list(map(lambda number : ((number**2) + 4), list_first1))
transition_list_2 = list(filter(lambda number : number % 5 == 0, transition_list_1))
# transition_list_3 = reduce(lambda num1, num2 : num1 + num2, transition_list_2)
# print(transition_list_1, transition_list_2, transition_list_3)

# Decorators
'''
Decorators:
    - Special type of function that can take another function inside it as a paramenter
    - A decorator is a function that take another function and extends or alters its behavior without
    modifiying the original function's code
    - An simple example can be 
    - Understand the time taken by a function of 50 mil function
    - The time logic is hard, in adding to all 50 mil 
    - so we use decorators where the function using the decorator is able to use that function every where
    - Decorators are special function that takes in other function as parameter
    - Decorators are understood by the code editiors with `@`

    @ decorator_function

    def my_function():
        pass
'''
print('--'*25)
# if we add string there is an error
# a special function that changes all arguments into integer

# the function takes in a parameter 
# the func take everything of function called 
def smart_conversion(func): #decorator is a function that can take other function
    # takes in the parameter of the function passed inside the smart_conversion automatically
    def wrapper(x,y): # can be used or not and parameters are already taken # acess the parameter 
        # the function (division) is called with the new converted parameter 
        # call the function with the new parameter and return the ans
        return func(int(x), int(y))
    # call the above wrapper to return it (call of the wrapper function) and return the answer of wrapper 
    return wrapper

# calling a decorator first and then the function is called 
# when the fucntion is called then goes to decorator and then passes the function
# adding new feature to the function
@smart_conversion
def division(x,y):
    return x/y

def add(x,y):
    return x + y

print(division('1', '2'), add('1', '2'))

print('--'*25)

import datetime

def decorator_function(func):
    # wrapper function are used for working with function parameter
    #
    def wrapper_function(n):
        start_time=datetime.datetime.now() #currenttime
        func(n) # calls the function with the parameter # the above func() the function that is passed into the argument
        end_time=datetime.datetime.now()#Time after completion
        print(f'Total time: {end_time}-{start_time}')
        print(f'{func.__name__}') # display the function name 
        return end_time-start_time, func(n)
        # here only the end_time will be return and not the function call result of (random_computation)
        # in order to return the (random_computation) we must return func(n)

    return wrapper_function # the use is it first calls the wrapper function here this is were the code stats
    # after the wrapper function is called the above wrapper function code is executed and return an output
    # from a decorator what will be return is what is inside the wrapper function

@decorator_function
def large_computation(n):
    random_computation=0
    for i in range(0,n):
        for j in range(0,i):
            random_computation+=j

    return random_computation

@decorator_function
def other_large_computation(n):
    random_computation=0
    for i in range(0,n%2):
        random_computation+=i
    return random_computation

#Intiial time
lol= large_computation(1000) # (datetime.timedelta(microseconds=42961), 166167000)
print(lol)
print('--'*25)
#Final time 
#calcualte final-initial_time
other_large_computation(100) # no print no return function
# if we have two decorator then design such a decorotor function to handel both task
print('--'*25)
'''
Create a function named 
division()-> that divides 2 number
addition()-> that adds 2 number 
subtraction()-> that subtracts 2 number 
multiplication()-> that multiplies 2 number 

function structure should be something like this 
def addition(x,y):
    return x+y

create a decortaor named identify_function_and_parameters
that should display which function is running 
and what are its parameters

at the end result should be something like this 

division(10,20)

output -> 
Division running between 10 and 20 
10/20

addition(10,20)
output-> 
addition running between 10 and 20 
10+20

'''
print('--'*25)

def identify_function_and_parameters(func):
    def wrapper_function(x, y):
        print(f'{func.__name__} running between {x} and {y}')

        return func(x, y)
    return wrapper_function

@identify_function_and_parameters
def division(x,y):
    return x/y

@identify_function_and_parameters
def addition(x,y):
    return x+y

@identify_function_and_parameters
def subtraction(x,y):
    return x-y

@identify_function_and_parameters
def multiplication(x,y):
    return x*y

divide = division(10,5)
print(divide)
