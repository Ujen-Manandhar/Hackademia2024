'''
AP that first gives 2 options: <br/>
Sign up<br/>
Sign in<br/>

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
# importing packages (Json)
import json

# creating a function to read the JSON file 
def read_data():
    try:
        with open('Database_JSON.json', 'r') as f:
            load_json_data = json.load(f)
            return load_json_data
    except:
        return {}

# creating a function to write the JSON file
# A JSON file will not append data as mustiple dictionary will be made making it difficult
def write_data(file_json):
    with open ('Database_JSON.json', 'w') as f:
        json.dump(file_json, f, indent= 4)
        print('Succesfully Stored')

# create a function to sign up
def sign_up():
    # how the json will be save 
    # dicti = {
    #     username :
    #     {
    #         'password' : password,
    #         'mobile': mobile
    #     }
    # }
    data = read_data()
    username = input('Enter a Unique User Name: ')
    # checking for new username
    if username in data:
        print('The Username is Taken')
    else:
        password = input('Enter a password: ')
        mobile = input ('Enter your phone number: ')
        # checking for dublicate numbers 
        for user_data in data.values():
            if mobile in user_data['Mobile']:
                print("Number exist try new number")
        # getting out of loop to store values in data variable using the unique username key
        data[username] = {
            'Password' : password,
            'Mobile' : mobile
        }
        # writing a new file of all the stored data 
        write_data(data)

# Creating a sign in function 
def sign_in():
    # reading the file
    data = read_data()
    username = input("Enter Your User Name: ")
    # to check the user is in the database
    if username in data:
        count = 0
        # giving the user 4 chances to input password
        for i in range(1,4+1):
            # user input password
            password = input('Enter Your Password: ')
            # checking the password from going into the dictionory of username and geting value
            # after geting value getting the key and checing the value again
            # data[username]->{"Password" : Stored passsword} -> username["Password"] -> stored password /
            # username is a new dict or is the new var with stored dict with new key value pairs
            # username_key -> {password_key: stored password} -> password_key -> stored password
            if data[username]['Password'] == password:
                # if password is correct display the mobile no
                print(f'\nWelcome {username}\nYour Mobile no is {data[username]['Mobile']}')
                break
            else:
                # if incorrect password
                print('Password is Incorrect')
                print(f'You have {4-i} try left')
                count += 1
        # too many failed attempts
        if count == 4:
            print('Too many failed attempts')
    # if user name dosen't match
    else:
        print(f'No User with : {username} avaliable')

def main():
    while True:
        print('\nPress one for Sign up')
        print('\nPress two for Sign in')
        user_input = input('Enter your choice: ')
        if user_input == '1':
            sign_up()
            print('Done signing up')
        elif user_input == '2':
            print('\nDisplaying informaiton')
            sign_in()
        else:
            print("exiting.....")
            break

main()