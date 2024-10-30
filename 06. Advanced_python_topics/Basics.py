"""
1. List Comprehensions and Generator Expressions
List Comprehensions are a concise way to create lists in Python. 
They are faster than using a for loop to create a list.
"""
#Creating a list 
list_variable=[1,2,3,4,5] #static way of creating a list 
list_variable=[]
list_variable.append(1)#Dyanmic way of creating a list 
list_variable.append(2)
list_variable.append(3)
print('--'*25)
odd_numbers=[i for i in range(1,100,2)] #It can loop inside the list creation itself
print(odd_numbers)

'''
List comprehension works best when we are working with very simple data modifications or conditions 
when complex conditions arises list comprehension is diffcult to code 
'''
print('--'*25)
a=[1,2,3,4,5]
#Approach 1
b=[]
#Mini Task. You have list a=[1,2,3,4,5] create list b which has each element of a squared.b=[1,4,9,16,25]
for element in a: 
    b.append(element**2)

print(b)
print('--'*25)
#Approach 2
b=[element**2 for element in a] #Basic syntax [variable_to_put_in_list operations(loop,conditions and so on)]
print(b)

print('--'*25)
#even off using if 
even_numbers=[i for i in range(1,100) if i%2==0] #if even number get its squared value elif odd number get its cube value
print(even_numbers)
'''
Geneartor in python: 

    - Special type of function that returns multiple value for multiple different instances using yield
    - def function_name():
        yield statement 

'''

#Simple generator: 
def simple_generator_function():
    yield 'a'
    yield 'b'
    yield 'c'

#First approach to getting results from geneartor function 
for value in simple_generator_function():
    print(value)
print('--'*25)
x=simple_generator_function()
print(next(x))
print(next(x))
print(next(x))


#Generator Expression: 
'''
Create generator object very similar to list comprehension
'''

square_gen=(x**2 for x in range(10)) #Generator Expression !!
print(square_gen)
print(list(square_gen))

'''
Create a geneartor operator that yeilds all the even numbers using generator expression 
Create an infinite loop where user is asked to type something
if the user types next 
display the next value of the geneartor operator
when the iteration is over the loop must exit (Hint: Using try except to handle this situation) 
'''

'''
Lambda: 
    -Lambda are often refered as annonymous functions
    - For very short and sweet operations
    - These functions are used in conjunction with higher level functions like map, filter, so on 
'''
print('--'*25)
x=lambda parameter: parameter**2
print(x(5))
print(x(10))

sum_of_2_numbers=lambda parameter1,parameter2: parameter1+parameter2
print(sum_of_2_numbers(1,2))

#Task 2, Given a list_1= [1,2,3,4,5,6,7,8,9,10] create a lambda function that returns half of that value and pass 
#each element of this list to that function and save everything in new list (using list comprehension)
#list_2=[0.5,1,1.5,2,.....]
print('--'*25)

#using if else inside lambda

get_greater_number=lambda x,y: x if x>y else y
print(get_greater_number(10,20))

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

print('--'*25)

'''
for (i=0;i<=10;i++)
{
    printf(i);
}

for variable in range(1,100,1) / for variable in list / for variable in dictionary

for i in range(1,100) i is essentially a variable 
for j in range(1,100) j is essentially a varaible 

for _ in range(1,100):
    print(_)


'''
for _ in range(1,100):
    print(_)



'''
map,filter and reduce
- map takes in function and collection and iterates all 
elements one by one over that function 

-map can also be used to map out 2 different parameters
from 2 different collections over a function

'''
print('--'*25)

list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
output_of_map=list(map(lambda x:x**2,list_of_numbers)) #Syntax map(function,list/iterable)
print(output_of_map)

print('--'*25)
def add_squared_numbers(x,y):
    return x**2+y**2

list_a=[1,2,3,4,5]
list_b=[6,7,8,9,10]

output_of_map_2=list(map(add_squared_numbers,list_a,list_b))
print(output_of_map_2)

'''
1. Take N from user (Number of elements)
2. Create a list of length N asking number from user (ask numbers and put it in a list)
3. Create another list of length N asking number from user (2nd list created with first list )
4. using map figure out which from both list add up to 10. Concat the 2 numbers and display the result in list 

list_a=[1,2,3,4,5],
list_b=[9,2,7,6,0]

[19,37,46]

'''
# N=int(input('Enter number of items to have in list: '))
# def check_ten(x,y):
#     if x+y==10:
#         return str(x)+str(y)


# list_a=[int(input("Enter element for list a: ")) for i in range(N)]
# list_b=[int(input("Enter element for list b: ")) for i in range(N)]

# output=list(map(check_ten,list_a,list_b))
# output=[i for i in output if i!=None]
# print(output)

'''
filter: 
    - Filter works very similar to map 
    - It takes function and iterable as input 
    - Returns output whenever its true 
'''

numbers=[1,2,3,4,5]
#evens_map=list(map(lambda x: x%2==0,numbers))
evens=list(filter(lambda x: x%2==0,numbers))
print(evens)

'''
given a list =['apple','ball','cat','dog','elephent']
create another list of words which have length >3
from the given list

ouptut_list=['apple','ball','elephent']

'''
print('--'*25)
# print(len('apple'))

from functools import reduce
'''
reduce:
    -[1,2,3,4,5]
    -multiply(x,y)->x*y
    -reduce(function,iterable,initial_value)
    - It runs the function one by one in cumulative way 
    from left to right 
        [1,2,3,4,5] -> [multiply(1,2),3,4,5]->
        [multiply(2,3),4,5]
'''

list_of_numbers=[1,2,3,4,5]
output=reduce(lambda x,y:x*y,list_of_numbers)
print(output)

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


'''
Decorators: 
    -Decorators are special function that takes in other 
    functions as prameter

    -Decorators are understood by the code editors with 
    @ 
'''
print('--'*25)

def smart_conversion(func):
    def wrapper(x,y):
        return func(int(x),int(y))
    
    return wrapper

@smart_conversion
def division(x,y):
    return x/y

@smart_conversion
def addition(x,y):
    return x+y

print(addition('1','2'))
print(division('4','2'))


print('--'*25)

import datetime

def decorator_function(func):
    def wrapper_function(n):
        start_time=datetime.datetime.now() #currenttime
        func(n)
        end_time=datetime.datetime.now()#Time after completion
        print(f'Total time: {end_time}-{start_time}')
        print(f'{func.__name__}')
        return end_time-start_time
    return wrapper_function

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
large_computation(1000)
#Final time 
#calcualte final-initial_time
other_large_computation(100)

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