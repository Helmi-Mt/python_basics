''' Here , we will solve some basic python problems'''
# Exercise 1: Calculate the multiplication and sum of two numbers
# the result = sum if product <1000 else result = product
# all will be put in functions to control the execution
def sum_product():
    x1 = float(input ('give the first number \n'))
    x2 = float (input ('give the second number \n'))
    result = x1+x2 if (x1*x2>1000) else x1*x2 # this is a one-line if statement
    print (f'result of {x1} + {x2} = {result}') # f in print do the formatting of variables values not names
# sum_product()

# Exercise 2: Print the sum of the current number and the previous number\
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

def iterate_sum():
    index = 0
    for num in range(10): # this will range from 0 to 9
        if index == 0:
            print (f' number = {num} and sum = {num}')
        else:
            print (f'number = {num} and sum = {index+num}')
        index = num
iterate_sum()