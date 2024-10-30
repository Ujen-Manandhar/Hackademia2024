'''
List

- List is a collection datatype that is capable of holding more than 1 variable
- It's very similar to Array but has 1 fundamental difference
- For list in python you can put in any type of value (any datatypes)
- It is denoted with "[]" big brackets 
- Each value has index or location associated with it

'''
# address= [0,1,2,3,4] <- index of list 
list_var = [1,2,3,4,5]
print(list_var, type(list_var), list_var[0])
print(len(list_var))
# iteration over list using index value 

for i in range(0, len(list_var)): 
    # i basically has the index value
    print(list_var[i])
print('- -'*25)
# iteratiing over each value itself

for list_element in list_var:
    # list_element is iterated
    print(list_element)
print('- -'*25)

# for finding out index and value in list
# the enumerate function returns the index along with the list elements

for list_index, list_element in enumerate(list_var):
    print(list_index, list_element)
print('- -'*25)

list_var_2 = [n for n in range(1, 11) if n % 2 == 0]
# task 1 : loop over each element of this list and show me only the even numbers
# for n in list_var:
#     if n % 2 == 0:
#         print(n) 

print(list_var_2)

#how to add elements in list:

list_var_3 = [] #no element of list 
#if there is no element then there is error

#staticaly adding elements to list , this is worst posslibe approch !!
list_var_3= [1]
print(list_var_3)

#dynamicaly adding element to the list
list_var_3.append(10)
list_var_3.append(20)
print(list_var_3)

print("--"*25)

# appending into the list using the for loop and append function
list_var_4 = []
for element in range(1,10):
    list_var_4.append(element) # append adds to the last so [1,2] and element = 3 => [1,2, element =3]
#Task 2 : Create a list name even list that should contain all the even numbers from 1-100
print("--"*25)

even_list = [n for n in range(1, 101) if n % 2 == 0]
# OR
even_list_1 = []
# for number in range(1,101):
#     if number % 2 == 0:
#         even_list_1.append(number)
for number in range(1,51):
    even_list_1.append(number*2)
print(even_list, even_list_1)

print('--'*25)

#slicing in list
# from a list only see a particular list slices of biger list
list_var_5 = [1,2,3,4,5]
print(list_var_5[1:])
print(list_var_5[1:4])

print('--'* 25)
#Removing element from a list
list_var_6 = [1,2,3,4,5,6]
print(f'Original: {list_var_6}')

#easiest approach to removing element from list is using pop
list_var_6.pop(1)
print(list_var_6)

# remove the index after the above pop will change the index  
list_var_6.pop(3)
print([list_var_6])
print("--"*25)

# Task 3: create a list of numbers from 1-100 using append , then remove all the odd numbers form that list
list_var_7 = []
for number in range(1,5):
    list_var_7.append(number)

# in the for loop the list is dynamic it changes as changes is done to the list
for index, number in enumerate(list_var_7):
    print(list_var_7)
    if number % 2 == 0:
        list_var_7.pop(index)

print(list_var_7)
print('--'*25)
'''
Dictionary 
- It is a collecction datatype with key and value pair
- Works on similar concept as hash maping 
- Key hold the address of the element and value holds the element present
- Classic dictionary is an example
    word : meaning
- It is denoted by '{}' bracket
'''

dictionary_val = {
    'key_1': [1,2,3,4,5], # <- nested datatype means inside a data type there is another data type
    'key_2': {'key_3': 'random values'},    # <- nested dictionary (JASON files)
}
'''
- in dictionary the we can look up key and their corresponding value using the key
- directly the key is given to identify the key
- for the index not to be dynamic the dictionary was made 
- as dictionary key are unique and to search each unique key there is no problem of index being dynamic
- no dynamic indexing as seen in .pop function
- like loking in the dict for word and returning the meaning
- keys are mostly string while values can be anything even list
'''

print(dictionary_val['key_1'])
print(dictionary_val.keys(), dictionary_val.values())
print('--'*25)

# How to add elements to a dictionary or modify


# Approch 1 using list:

list_keys = ['apple', 'ball', 'cat']
value_list = ['red color fruit', 'somthing children use to play', 'animal that makes meow']
# here the list of values and keys map  each other or one to one match

dictionary_val_2 = dict(zip(list_keys, value_list)) # (keys, values) zip requires equal or none is shown
# the iterable must be of same length
# the zip function is used to put the keys and values side by side in a truple and convert to dict
# [('apple', 'red color fruit'), ('ball', 'somthing children use to play'), ('cat', 'animal that makes meow')]
print(dictionary_val_2)

# Task 4 : Create quiz question answer dictionary using zip function and 2 list

question = []
answer = []

# for _ in range(1, 4):
#     user_input_question = input('Enter the question ? ')
#     user_input_answer = input('Enter the answer for the question : ')
#     question.append(user_input_question)
#     answer.append(user_input_answer)

# dictionary_quiz = dict(zip(question, answer))
# print(dictionary_quiz)
print("--"*25)
# Approach 2 using update:
# Better approch than append 
# is the best approch and the update methon sends a sub- dictionary and is sent to last of dict

dict_var_1 = {'Key_1' : 10, "Key_2" : 20}
print(f'Before update {dict_var_1}')
dict_var_1.update({'Key_3' : 30, 'Key_4': 50})
print(f'After update {dict_var_1}')

# Approch 3 using append:
dict_var_2 = {'Key_2': 10}
dict_var_2['Key_3'] = 20
print(f'Appending : {dict_var_2}')