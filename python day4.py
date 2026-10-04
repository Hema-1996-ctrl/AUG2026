'''
# Dictionary : unordered, mutable wher key must be unique and immutable, value can be duplicate and it is mutable
# Dictionary stores key and value pair
emp_details = {1:'Hema',2:'Santu',3:'Pihu',4:'chotu',5:'Gundu'}
print(f'my dictionary is:{emp_details} and  type is {type(emp_details)}')

# get all the keys(empno) using for loop
for key in emp_details: # by default behaive : for key in emp_details.keys():
    print(key)

# get all the values(empname)
for value in emp_details.values():  # by default behaive : for key in emp_details.values():
    print(value)

# get all the key and values = item
# way 1
for item in emp_details.items():  # by default behaive : for key in emp_details.values():
    print(item,type(item)) # each item presents like tuple

# way 2
for item in emp_details.items():
    eno = item[0]
    ename = item[1]
    print(eno,':',ename)

#way 3
for k,v in emp_details.items():
    print(k,':',v)


# get a values for a specific key(empno = 4)
print(emp_details[4])

# add one more item to the dictionary
emp_details[6] = 'amma'
print(emp_details)

# update ename  for empno 6
emp_details[6] = 'Laxmibai'
print(emp_details)

# remove items from the dictionary : using  pop we can delete any item
print('Before removal :', emp_details)
removed_val = emp_details.pop(1)
print('After removal :', emp_details)
print(removed_val)

# # remove items from the dictionary : using  popitem we can delete  item from the last inserted one and able see complete tuple
removed_popitem = emp_details.popitem()
print('After removal :', emp_details)
print('Removed values popitem : ',removed_popitem)

'''

'''
# functional way of writing python program
# function contains block of code to put together
# it supports modularization

# defining a function and running
# function that does not return any value
def display():
    print('display') # in procedure way if i want print 5 times i need write 5 time, in functional way just we need to call the function that how many times we want to print
    print('hi')
display()
display()

# function that  return the value
def print_name():
    name = 'HemaSantu'
    #print(name)
    return name
#print_name()
ans = print_name() # this ans varibale not storing any value because we are not returning any value to the function
print(ans)

'''

# why set is faster than list and tuple?