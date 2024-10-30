def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def product(a,b):
    return a*b

def divide(a,b):
    return a/b

# here a.py is independent as it dosen't require other packages of .py files to do it's operations 
# independent enity as the file has it's own functions and variables run independently or run certain task independently on its own 
# like a class is also independent (having its own variables and function) and can run independently, the script can also run indepndently so the script can also be a class
# so the script can run the file in the independently on its own and 
# also from another file we can create a object of the a.py to acess it class a.py

# working independently to give output
print('Add form a.py file:',add(1,2)) # this is also run when being imported 

# unit testing of each function the import is aslo running the print statement 
# which we don't need

# so if we don't want to see the unit tesiting result then we

if __name__ == '__main__':
    print('Sub form a.py file:',sub(1,2))

# here if the a.py script is run then the condition after the if clause is run and will not run if it is imported 
# this skips the unit testing part as the condition isn't run

# in this case it is know as a module rather than a class; as we are importing the whole script 