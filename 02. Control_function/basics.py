# conditional statement 
'''
Conditional statement 
- where a certain part of code is activated when a condition is met 
- syntax 
    if (condition1.1 and condition 1.2) or (condition 2): <- suggest doing in bracket as it helps seperate or phrase
        sastify_function()
    elif (condition 3 ): <- else if 
        another function
    else: 
        Unsastifiy_fuction()

the brackets in C is consider as tab in python 
'''
# === assertion make it equal
# x = 10 
# print(x, type(x))
# if (x % 2) == 0:
#     print('Even', x)
# elif (x == 10):
#     print('is ten')
# else:
#     print('Odd', x)

# Task 1 : take username and password from user check if password is same as the one set by the admin
# admin_password = 'Admin123'
# username = input('Enter username: ')
# password = input('Enter Password: ')

# if admin_password == password:
#     print(f'{username} welcome')
# else:
#     print(f'The password is invalid')

# Task 2 : Create a KBC/ quiz where 5 question are asked and 5 answers need to be provided after
# each correct answer score increases 
# .lower()

# username = input('Enter username: ')
# print('Whar is the capital city of Nepal')
# answer = input('enter the answer: ')
# score = 0
# if answer.lower() == 'kathmandu':
#     score += 100
#     print(f'Correct! your score is {score}')
#     print('What is the capial city of India')
#     answer = answer = input('enter the answer: ')
#     if answer.lower() == 'new dehli':
#         score += 100
#         print(f'Correct! your score is {score}')
#         print('What is the capial city of China')
#         answer = answer = input('enter the answer: ')
#         if answer.lower() == 'bejing':
#             score += 100
#             print(f'Correct! your score is {score}')
#             print('What is the capial city of Bangladesh')
#             answer = answer = input('enter the answer: ')
#             if answer.lower() == "dhaka":
#                 score += 100
#                 print(f'Correct! your score is {score}')
#                 print('What is the your username')
#                 answer = answer = input('enter the answer: ')
#                 if answer == username:
#                     score += 100
#                     print(f'Correct! your won with a score of {score}')
#                 else:
#                     print(f'Better luck next time your score is {score}\n You were so close')
#             else:
#                 print(f'Better luck next time your score is {score}')
#         else:
#             print(f'Better luck next time your score is {score}')
#     else:
#         print(f'Better luck next time your score is {score}')
# else:
#     print(f'Better luck next time your score is {score}')

'''
loop and iteration:
- repeatidly do a particular task
- repeat same tak over and over again
- can be used for various cases, runing program indifidenitly

for loop and while loop

    -for loop is when we know the starting point and we know the ending point of the loop
    - execute a program at 12 pm to say happy birthday
while loop:
    - loop to continue 
    - loop is used when the developer himself dosen't know the ending point.

'''

# for variable_name in range(1,10,2):#<- (start, end, step(difference))
#     print ('Ujen ') # <- show the name 9 times
#     print(variable_name)

for odd_number in range(1,10,2):
    print(odd_number)

for odd_number in range(1,10):
    if odd_number % 2 != 0:
        print(odd_number, "odd")

'''
While Loop:
    - Standard pratice is to write a while loop in infinite condition
    - in situaion where the condition is met or not met we use BREAK in order to get out

while alive:
    if death:
        break

while (condition_where_the_loop_will_continue):
    if (stoping_condition) == True:
        stop(break)
'''

# Task 4  continously take input from user until and unless they give a number that is divisible by 5
while True:
    user_input = int(input('enter number: '))
    if user_input % 5 == 0:
        break

'''
function:
    - A particular piece of code that preforms a particular task pretty well
    and used repetaidly to do the paricular task always
    - done to make the code reusable 
    - no duplication of code 

    - defination = define the function and what it will do
        def function_name (arguments):
            print(arguments) or return value

    - calling = invoke or call that particular function that was defined 

        function_name(arguments)

'''

def even_number_checker(number):
    if number%2 == 0:
        print('Even')
    else:
        print('Odd')

even_number_checker(5)
even_number_checker(10)

# task 6 create a function that takes inupu x and print us if it's a multiple of 10
def multiple_checker(number):
    #inside the function and end the work inside the function and code ends here no return value
    if number%10 == 0:
        print("multiple of 10")
    else:
        print("not a multiple of 10")

multiple_checker(10)
multiple_checker(9)

# a return value is something that is brought back from the function
'''
print type function is like going to the barber you don't bring anything
return type function is like going to a shop you bring back something 

'''

def even_odd_checker(x):
    if x%2 == 0:
        return "even",x
    else:
        return "odd",x
# a function is called only when a function is called 
# but a function takes a dedicated memory but after repetatily calling eats up memory
output = even_odd_checker(5) # the return value is sent in a tuple 
print(output)

# recursive function is a type of function that calls itself repeatively
# An alternative of loop

def factorial (n): # 5
    #base case : if n is 0 or 1, return 1
    if n == 0 or n == 1: #stoping condition (always write the stoping condition first)
        return 1
    # recursive case : n * factorial of (n-1)
    else:
        return n * factorial(n-1) # function with 4 call 

# primarly recursive is used for loop alternative or core functional programming 
print(factorial(5)) # output will be 120

# calculate sum of n numbers useing recursinve function N -> provided by user 
def sum_of_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_num(n-1) #recursion main part 5+[4+[3+[2+[1+0]]]]

print(sum_of_num(5))
# index =  01234
# string = Apple
# reverse a string using recursive function
def reverse(string):
    if string == '' :
        return ''
    else:      # [pple]<- goes inside the function + a
               # [ple] +pa
               #  [le] + ppa 
        return reverse(string[1:]) + string[0] # g[]

print(reverse('ujen'))

# Global and Local variable !!
# a variable inside a function is only limited to the variable only

# if a variable is outside the function then the variable is global

global_var = 10 # main flow # scope all over the code

def local_function():
    local_var = 15 # scope of this variable is within this function local_function()
    print(f'Global Variable: {global_var}')

print(global_var)# ok
# print(local_var)# error