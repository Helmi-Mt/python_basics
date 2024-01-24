''' Here , we will solve some basic python problems
 Exercise 1: Calculate the multiplication and sum of two numbers'''
# the result = sum if product <1000 else result = product
# all will be put in functions to control the execution
def sum_product():
    x1 = float(input ('give the first number \n'))
    x2 = float (input ('give the second number \n'))
    result = x1+x2 if (x1*x2>1000) else x1*x2 # this is a one-line if statement
    print (f'result of {x1} + {x2} = {result}') # f in print do the formatting of variables values not names
# sum_product()

''' Exercise 2: Print the sum of the current number and the previous number'''
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

def iterate_sum():
    index = 0
    for num in range(10): # this will range from 0 to 9
        if index == 0:
            print (f' number = {num} and sum = {num}')
        else:
            print (f'number = {num} and sum = {index+num}')
        index = num
# iterate_sum()

'''Exercise 3 :Print characters from a string that are present at an even index number'''
def text_even_char():
    text = input ('Write some text, random text : ').strip() # strip function to remove spaces at beginning and end
    print ('typed text = ',text)
    index = 0
    for char in text:
        if index%2 == 0:
            print (char+',',end='')

        index += 1

# text_even_char() # if you print a function with no return, you will print None (that what all functions return by default)

'''Exercise 4 :Remove first n characters from a string'''
# Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_characters(text,number):
    return text[number:]
    
# print (remove_characters('pynative',2))

'''Exercise 5 :Check if the first and last number of a list is the same'''
def check_list(l1):
    return True if l1[0]==l1[-1] else False
    
# print (check_list([1,2,3,4,5,11]))

'''Exercise 6: Display numbers divisible by 5 from a list'''
def display_Modulo_5(list):
    print ('Given list = ',list)
    print ('The following are divisible by 5 : ')
    for num in list:
        if num%5 == 0:
            print (num)
            
# display_Modulo_5([1,5,15,10,67,60,75])

'''Exercise 7: Return the count of a given substring from a string'''
# Write a program to find how many times substring “Emma” appears in the given string. (should work with any substring)
# print (dir(str)) # this will show all the str methods 
import re # we import the  re : regular expression module to play with it *-__-*
def substring_count(string,sub_string):
    
    list = re.findall(sub_string,string) # this will return the list of all the occurences
    print (f'{sub_string}, the sub_string,  appears in the string {len(list)} times.')

substring_count('Emma is good developer. Emma is a writer','Emma')

def substring_count_2(string,sub_string):
    return string.count(sub_string) # count method will count the number of occurences of substring in string
print ('the count way : ',substring_count_2('Emma is good developer. Emma is a writer','Emma'))

'''Exercise 8: Exercise 8: Print the following pattern'''
# exercise : 