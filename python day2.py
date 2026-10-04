'''
# Taking input from user

# Input
name = input("Enter your name: ")
print('data type of name is :', type(name))
print('my name is :', name)

# input() :  input() taking the input in string formate
age = int(input("Enter your age: ")) # i converted into int
print('data type of age is :', type(age))
print('my age is :', age)



# Control statement : manage the flow execution  of our program
# if
age = 20
if age >= 18:
    print("Eligible for voting")
print("program completed")


# if ...else
age = 20
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
print("program completed")



# elif
age = int(input("Enter your age: "))
if age > 18:
    print("Eligible for voting")
elif age == 18:
    print("Near Eligible for voting")
else:
    print("Not eligible for voting")

print("program completed")



name = "Hema Santu" # if string become empty then it gives false
if name:
    print("True")
else:
    print("False")



# Looping statement
# 1) for 2) while
# range(10) --> 0,1,2,.....9 , starts with 0 and ends with number-1
# range(start_value, end_value, steps)
# range(2,20,3) --> 2,5,8,11,14,17

# for loop
# range(10) == range(0,10,1)
for num in range(10):
    print(num)



# print even numbers till 16 starts from 2
for num in range(2,17,2):
    print(num)

# print odd numbers till 13 starts from 1
for num in range(1,14,2):
    print(num)

'''

# while loop stops when condition gets false
# print 1 to 10

start_val  = 1
end_val = 10
while start_val <= end_val:
    print(start_val)
    start_val = start_val + 1