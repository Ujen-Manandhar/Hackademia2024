'''
Task 2: 
WAP that uses oop
has class user
when initalized it provides options: 
    1. Sign up 
    2. Sign in 

if 1 is pressed it redirects to a method named Register_User
this method takes in username, password and mobile number

if 2 is pressed it redirects to a method name authentication
this method checks input username and password with self.username
and self.password 

if match it redirects to another method named welcome_user

welcome user method greets them,displays username and displays 
their mobile number

also this method gives 3 options. 
1. enter note 
2. Display notes
3. exit 

if 1 is pressed user can input a large note that is saved for that 
object 

if 2 is pressed display the note that was saved earlier 

if 3 is pressed terminate 
'''

class User:
    def __init__(self):
        self.userinput = input('1. Signup: \n2. Signin: \n3. exit')
        if self.userinput == '1':
            self.username = input('Enter Username: ')
            self.password = input('Enter Password: ')
            self.mobile = input('Enter mobile number: ')
        elif self.userinput == '2':
            print('exit')

    def signin(self):
        
User1 = User()

