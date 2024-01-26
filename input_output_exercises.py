# input and output exercises in python
'''Exercise 1: Accept numbers from a user'''
# accept two numbers input and do : multiplication / addition / comparison / prime or not

def input_manip():
    x,y = '',''
    while x=='' or y=='':
        try:
            x = int (input ('Give an integer x = '))
            y = int (input ('Give an integer y = '))
            print (f' {x} + {y} = {x+y}')
            print (f' {x}* {y} = {x*y}')
            print (f' {x} / {y} = {x/y}')
         
        except:
            print ('Need to enter integers only')
            yes_no = input ('Do you want to replay again ? \n YES to replay , anything else to break \n')
            if yes_no.lower() != 'yes':
                print ('See you next time')
                break
            else:
                continue
# input_manip()

'''Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”'''
def print_strings(separation='**',*words):
    for word in words:
        print (word,separation,end='')
        
# print_strings('**','Name', 'Is','James','American')
# or try the built in like this
print('My', 'Name', 'Is', 'James', sep='**')

'''Exercise 3: Convert Decimal number to octal using print() output formatting'''
x = 10
# print (f' x= {x} , in octane system = {oct(x)}')
# print ('x decimal , becomes in octale :' % x)

'''Exercise 5: Accept a list of 5 float numbers as an input from the user'''
def get_floats():
    # get input of 5 float and display them
    list = []
    for num in range(1,6):
        
        x = float(input (f'Enter a float number : #{num} /→ '))
        list.append(x)
    print (list)
# get_floats()

'''Exercise 6: Write all content of a given file into a new file by skipping line number 5 '''
# file name test.txt
def copy_write_file():
    with open("test.txt", "r") as fp:
    # read all lines from a file
        lines = fp.readlines()
        print ('lines = ',lines)

    # open new file in write mode
    with open("new_file.txt", "w") as fp:
        count = 0
        # iterate each lines from a test.txt
        for line in lines:
            # skip 5th lines
            if count == 4:
                count += 1
                continue
            else:
                # write current line
                fp.write(line)
            # in each iteration reduce the count
            count += 1
    with open('new_file.txt','r') as fpup:
        for lines in fpup:
            print ('second open ',lines)
    with open('new_file.txt','a') as fpup:
        fpup.write('\nNow the file has more content!')
        print ('after append head')
        # lines = fpup.readlines()
        # print ('lines after append = ',lines)
    with open('new_file.txt','r') as fpup:
        for lines in fpup:
            print ('last open ',lines)
# copy_write_file()

'''Exercise 7: Accept any three string from one input() call'''
#  get three input by the same input line
def three_inputs():
    in_str = input ('Give your 3 inputs separated by comma ')
    list_input = in_str.split(',')
    print ('The input line of words ', in_str)
    print ('The input list : ',list_input)
            
three_inputs()