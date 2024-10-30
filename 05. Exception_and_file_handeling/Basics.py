'''
Exception or error handeling!!!
    - Sometimes there might be some kind of logical error in code
    - When code misbehaves 
    - Used for avoiding code problems
    - we use try.... except
    - Exception handeling has mainly 2 parts:
        try:
            code in try block (that might crash)
        except:
            if code fails rest of the part runs here when error runs when if it crashes 
'''
# while True:
#     x = int(input('enter: '))
#     y = int(input('enter: '))
#     try:
#         outut = x/y
#         print(outut) # run if the input are correct

#     except Exception as e: #excption is the error
#         print('Got error so quitting the loop: ',e)
#         break



'''
Task1:
Start infinite loop, get random numerator and denominator (0-100), calculate total number of crashes and if total number of crashes
== 100 terminate the program
'''
'''
#standard pratice number 1: Try to do everything using functions
def simple_function():
    # code for the function
    return 0
# standard pratice number 2: use try and expect block on each function 
try:
    simple_function()
except Exception as e:
    print(e)
    pass
'''


import random

crashes = 0

while True:
    a = random.randrange(0,5)
    b = random.randrange(0,5)
    try:
        if crashes == 1:
            break
        divide = a/b
    except:
        print(f'numerator: {a}\n denominator: {b}\n Crash: {crashes}')
        crashes += 1


'''
File handeling
    - Building blocks of file handeling, SQL
    - Variables are volitile memory as they are changed in runtime; they are runtime memory
    - All variables are stored in runtime memory during the execution 
    - These variables are volitile in nature
    - To avoid deletion or the use these variables on long term we need to save these variables or state of variables somewhere permanently
    - To ask the data for variables is inefficient like login in we need to run the program again 
    - So we use file handeling, we store the variable and the state of variable or information is stored permanently
    - Abstraction: open a file, and save some changes like saving data to a table.

'''

username = input('enter Username: ') # taking user name
password = input('enter passwoer: ')# taking password 
print(username, password) # stored in volitile memory and the variables aren't stored any where and reset everytime 

# so to store the variable we use file writing
# writting in file
# done to fetch data of the sign up to store the variable in sign up in a database, and to store the above given username and password in database
'''
with open('/Users/Uttam/Documents/hackademia/venv/5. Exception_and_file_handeling/database.txt', 'w') as f:
'''
# with use for exception handeling; if not done if the program crashes then file gets copurt, and also handels crashes
# (mode) only to write or save the username and password
# as the file has been open in write mode it is saved in f variable or file variable
'''
    f.write(username+' '+password) # save or write the username and password in the file database.txt
'''
    # made in the current working folder in the terminal and can also define path

print('--'* 25)

# now reading the username and password or loading the username and password from the database
with open('/Users/Uttam/Documents/hackademia/venv/5. Exception_and_file_handeling/database.txt', 'r') as f:
    # f.readline()
    from_file_output_var = f.readlines() # the method converts all the lines in the code line by line into a list or see by hover the arrow represents the return
    # class bitra ko function is what is a method
print(from_file_output_var[0]) #store in list as a file may have multiple lines and as such each new line are stored list 
# first line = index[0]
# append adds new lines
# while write clears all the lines and adds new lines - rewrite the file
# write ma over write hunxa ani append maaa add garxa tesma
print('--'*25)
'''
Task 2: WAP that first gives 2 option:
    1: Write note
    2: Read note
    
    if 1 is pressed the program directs u to write a long note, as the note is written and complected the note is 
    stored in database. txt file

    if 2 is pressed all the writtn notes are displayed.
''' 
'''
# Task 2 answer
def write (message):
    with open('/Users/Uttam/Documents/hackademia/venv/5. Exception_and_file_handeling/note.txt', 'a') as f:
        f.write(f'{message}\n')

def read ():
    with open('/Users/Uttam/Documents/hackademia/venv/5. Exception_and_file_handeling/note.txt', 'r') as f:
        from_file_output_var = f.readlines()
        return from_file_output_var

while True:
    print('\n1. Write Note')
    print('2. Read Note')
    print('3. Exit')

    user_input = input('enter: ')
    if user_input == '1':
        message = input('Write a message to store: ')
        write(message)
        print('Your meassage has been stored: Exiting .....')
    elif user_input == '2':
        print('Displaying the stored information......\n')
        readfile = read()
        for words in readfile:
            print(words)
    elif user_input == '3':
        break
    else:
        print('Please enter a Number')
'''

'''
Task 3: WAP that first gives 2 options:
    1. Sign up
    2. Sign in 

    When 1 is pressed user needs to provide following information 
    1. username 2. password 3. Mobile number
    all this information is saved in a file everytime a new user signs up the same file is updated
    (hint: append over the same file)

    when 2 is pressed 
    user needs to provide username and password 
    this username and password is checked with username and password in the database
    if matched: 
        welcome to the device and show theri phone number
    else:
        terminate the program saying incorect credentials
'''
# apppend the information of the user to the database 
choice = int(input("Enter your choice: "))
if choice == 1:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    mob = input("Enter mobile number: ")
    with open('signupinfo.txt', 'a') as f:
        f.write( username + ' ' + password + ' ' + mob + '\n')
else:
    flag= 0
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open('signupinfo.txt', 'r') as f:
        for x in f.readlines():
            values = x.split(' ')
            print(values)
            if(username == values[0] and password == values[1]):
                print("welcome to the program")
                print("your info")
                print("username: " + values[0])
                print("password: " + values[1])
                print("mobile: " + values[2])
                flag = 0
                break
            else:
                flag = 1
    if(flag == 1):
        print("Login Error")

'''
CSV = with commas values are seperated
JSON = Java script object notation
JSON file
{
 'Ram': <-  ram information is stored in another dictionary 
        {  
        'math' : 10, 
        'science' : 20, <-ram futher information stored in this dictionary
        'social' : 30
        }
'Sita': <- this is a key value pair where the key is a name and value is another dictionary with more values 
        { 
        'Math' : 20,  # this can be translated into a perfect JSON, JSON are light weight database all informatinon are store in a complex JSON
        'Science':30, # light weight and powerful database 
        'Social':40
        }
} 
'''
# dificult in text file
import json
to_save_dictionary = {
    'students' : ['Ram', 'Shyam', 'Sita'],
    'Marks' : [10,20,30]
}
with open('database_json.json','w') as f:
    json.dump(to_save_dictionary,f) # dumps the json file to a new file
    #         ^^^^^^^^           ^
    #        the dict to save    where to save

with open('database_json.json','r') as f: # store in f variable
    loaded_jsonn = json.load(f) # loads the json file from f variable and store in loaded_json

print(loaded_jsonn) #csv and json are important in AI and ml programs
# don't use append in json

'''
WAP that first gives 2 options: 
Sign up
Sign in

when 1 is pressed user needs to provide following information 
Username, 2. Password, 3. Mobile number
All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 


Do it using json files, save everything to json and load from json 
 
'''