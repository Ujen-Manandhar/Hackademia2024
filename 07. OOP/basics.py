'''
Class:
    - Collection of functions and variables, which can work independently on its own
    - Meaning that if class code are left alone these code are independent entity 
    - Everything is an object in python : meaning all the function are an object; even a file .py is a class as we can import it create an object and use it as variable
    - Everything is a class (all script .py is a class) everything is an object
    - Animal is a class while dog is an object 
    - A special Umbrella topic is a class: example is Animal, Vehicles, Dress

Object:
    - Its Jus an instance (class ko tukra with seperate identity) of class (Its a part of class that has its own independent identity )
    - Dog from animal can be an object, cars is an object of vehicles (here dog and cars have their seperate identity)
    - Object can also be a class (eg: Dog breeds) as an object might contain various instances
    - Each object has its own set of attributes(variables/features) and methods (function, behaviour) and also acts differenly
    - Dogs has 4 legs(variables) and barks(function/ behaviour) / Different identity of object


In facebook
class User:
    def __init__(self, id, password):
        self.id = id
        self.password = password
    template of user

# object identity of user 
user1 = User(Id1, password)
user2 = User(Id2, password)

Why oop?
Here from a class (template) user we can make different user using the same template. In procudual programing we need to create code for each 
user which isn't efficient to scale.
Python is a pure oop level programing languagae
'''

# class
class Animal:
    def what_sound_does_it_make(self, flag):
        if flag.lower() == 'bark':
            print('Hey It\'s a dog')
        elif flag.lower() == 'meow':
            print('Hey it\'s a cat')
        else:
            print('It\'s a human')

# object
species_1 = Animal() #created an object
# here the object has acess to the method(function) of the animal class
# functionality (method), arg ('bark')
species_1.what_sound_does_it_make('Bark') # here bark is acting as the credentials, or even parameter to seperate the different identity
# output >> Hey It's a dog

species_2 = Animal()
# here functionality has change to meow so identity changes 
species_2.what_sound_does_it_make('meow')

# here from the one baseline code different instances were made
# created 3 different users with different identity with taking parameter (bark, meow, talk)
# different variation with the same code 
print('--'*25)

'''
Create a Class name calculator, that must have following methods
add_2_numbers(), substract(), multiply(), divide()
create 2 different instances of calculator (create 2 objects) and run the methods
'''

class Calculator:

    def add_num(self, x, y):
        print(x+y)
    
    def sub_num(self, x,y):
        print(x-y)
    
    def product(self, x,y):
        print(x*y)
    
    def divide(self, x,y):
        print(x/y)


instance_cal1 = Calculator()
instance_cal1.add_num(1,2)
instance_cal1.sub_num(1,2)

instance_cal2 = Calculator()
instance_cal2.product(5,2)
instance_cal2.divide(10,5)

# Constructor
'''
Constructor:
    - Constructor is used during initalization, such that as soon as an object is created it jumps to the constructor part.
    - After an object is made the object has no values and is sitting as a variable in the species1 variable and only after sending it to the fucntion then only the object acted before that it was just a variable
    - So as soon as we create an object make a function to keep values by default or funcutionaly to do direct is done by constructor
    - Syntax
        def __init__(self):
            constructor_code_here()
    - When we call a constructor in the time when the object is created in order to set variables or call function  or set values, or even operations
    - After witing the username and password, authencation is done automatically and goes to the profile is a constructor 
'''
print('--'*25)
class KBC:
    def __init__(self, name): # automatically called no need to call method
        print('Welcome to KBC', name)

# if a constructor is made then at the time when object is created we can pass the parameter at initation; if there wasn't a constructor then there is error as it is just working as a class
game_for_Siddhant = KBC('Siddhant')
game_for_Ujen = KBC('Ujen') # at starting the game initializes when the objec is created

# Encapsulation
'''
How does encapsulation and different instances work!!

Create different instances with different information 

Encapsulation: 
    different instances has its different information an encuplate the information
    - Like in facebook each user status histoy is saved in their onwn object

The prev code was like a funnel and nothing was stored in the code the input was taken and output given and nothing was stored
Encapsulation helps to store the values in variables for the different instances
Similar to storing username and password of the user as an object 
Creating a Cup(class), to sotre tea(object variables) or coffee(object variables)
'''
print('--'*25)
# class should be such a type that it stores both variable and function 
class Animal2:
    def display_all_its_attributes(self):
         # inside a class to call an attribute we need to use self.attibute_name inside the class
        print(self.name, self.species, self.dob) # mero object ko yo variable 

    # hold information for an object (information of the animals)
    # here self points to the instance (object)
    # self = species_1
    # initialize and store the variable values
    # constructor dosen't matter the order of where the method is placed 
    # parameter first code send were just a guest and aren't permenant
    def __init__(self, animal_name, animal_species,animal_dob): #three parameter
        # acting as a universal vaiable for the entire class
        self.name = animal_name # create name variable of self ie species_1 and hold by the species_1 and store the variable of name and this varible is hold by the species_1 variable
        self.species = animal_species #create a variable for an instance(object) and is hold by the variable self.<variable_name> where self dentoes the object
        self.dob = animal_dob # saving the dob value in self.dob or the particualr instance dob being saved in variables
        #like saving of profile attributes of the user and is different for every one user as all user may have different attributes
        # ---------------------------------------------------------------------------------------------------------------------------
        # we can't use return as we are not terminating the instance only creating the instance
        # return is like terminating as when the item is return  the user is created and deleted at the same time 
        # seperate entitiy being created where everything is the save in object
        #-------------------------------------------------------------------------------
        # print from constructior calling a method # from class calling the method 
        # call function in the same python script
        self.display_all_its_attributes() # jun object ma chu tesko nai ma vasara function call gara la 
'''
species_1.py inside file
# class file is working as a py file 
def dispaly_all_its_attributes()
    print() #as name sepcies are univeseral variables it understands itself so name, dob and species are acesed by all function


made a universal variable 
name = 
species = 
dob = 

# call function in the same python script
display_all_its_attributes() 
# similar to the above class

we can also save the object in its state in a data base 
load from the previous value is more easier by saving the current state of the object 
'''
species_1 = Animal2('Rojo', 'Dog', '2015-3-3') # object are classes or an instance of a class
# here self.name what happens is in the memory of sepcies_1 object the .name  variable has been stored in memory
# all the variables values are stored in object
# the values are given and in itself the variables are created and store the values
print('--'*100)
print('Information from outside')
print(f'Object: {species_1}\nName: {species_1.name}\nSpecies : {species_1.species}\nDOB: {species_1.dob}')
print('--'*100)
# hold different memory for different specieds
species_2 = Animal2('Dwarfa', 'Yak', '2022-02-02')
print('--'*100)
print('Information from outside')
print(f'object: {species_2}\nName: {species_2.name}\nSpecies : {species_2.species}\nDOB: {species_2.dob}')
# this to replicate in functional programming is hard and difficult; and takes ages to design
# here each object has it's own attributes and the two object can have different functionalities 
# A lot of info is save in the variable only 
print('--'*25)

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

