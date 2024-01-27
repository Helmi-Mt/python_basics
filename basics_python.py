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


# substring_count('Emma is good developer. Emma is a writer','Emma')

def substring_count_2(string,sub_string):
    return string.count(sub_string) # count method will count the number of occurences of substring in string
# print ('the count way : ',substring_count_2('Emma is good developer. Emma is a writer','Emma'))

'''Exercise 8: Exercise 8: Print the following pattern'''
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4
def pattern_printer(n):
    for i in range (1,n+1):
        st_int = str(i)+' '
        print (st_int*i)
        
# pattern_printer(9)

'''Exercise 9: Check Palindrome Number'''
def check_Palindrome():
    x = int (input('Give a number = \n'))
    y = str(x)
    z = int(y[::-1])
    print (f'x= {x} and reverse x = {z} ')
    result = True if x == z else False
    return result

# print ('The input is a Palindrome = ',check_Palindrome())

'''Exercise 10: Create a new list from two list using the following condition '''
#  New list should contain odd numbers from the first list and even numbers from the second list.
def merge_lists(l1,l2):
    l3 =[]
    for i in l1:
        if i%2 != 0:
            l3.append(i)
    for j in l2:
        if j%2 == 0:
            l3.append(j)
    return l3
        
# print (merge_lists([1,2,3,4,5], [10,20,30,40,50]))

'''Exercise 11: Write a Program to extract each digit from an integer in the reverse order.'''
def extract_digits(n):
    new_str =''
    st_num = str(n)
    st_num_inv = st_num[::-1]
    for char in st_num_inv:
        if (st_num_inv.index(char) != len(st_num_inv)-1):
            new_str += char+' '
        else:
            new_str += char
    print (n)        
    print (new_str)
        
# extract_digits(156484)

'''Exercise 12: Calculate income tax for the given income by adhering to the rules below'''
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000. // after the first 20,000 the remaining is 20% taxable
def tax_calculation(income):
    tax = 0
    if (income > 10000 and income<=20000):
          tax = (income-10000)*0.1
    elif (income > 20000):
        tax = 10000*0.1 + (income-20000)*0.20
    return tax

# print (tax_calculation(45000))

'''Exercise 13: Print multiplication table from 1 to 10'''
def multip_table():
    for num in range (1,11):
        i = 1
        while i<=10:
            print (num*i,' ',end='')
            i += 1
        print ('')
          
# multip_table()

'''Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)'''
# ****
# ***
# **
# *
def downwar_pattern(char='*',length=5):
    pattern_length = length
    for num in range(1,length+1):
        while pattern_length>=1:
            print (char*pattern_length)
            pattern_length -= 1

# downwar_pattern('_-_',10)

'''Exercise 15 : Write a function called exponent(base, exp) that returns
an int value of base raises to the power of exp.'''

def exponent(base, exp):
    result = 1
    exponent = exp
    while exponent>0:
        result *= base
        exponent -=1
    return result

print (exponent(2,5))

'''******************************************** END OF BASICS / firt section'''

substring_count('Emma is good developer. Emma is a writer','Emma')

def substring_count_2(string,sub_string):
    return string.count(sub_string) # count method will count the number of occurences of substring in string
print ('the count way : ',substring_count_2('Emma is good developer. Emma is a writer','Emma'))

'''Exercise 8: Exercise 8: Print the following pattern'''
# exercise : 

