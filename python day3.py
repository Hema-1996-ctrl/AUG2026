
'''
# primitive data types : int, float, string and boolean
# non-primitive data types(collection data types) : list,tuple,set and dictionary

# list : ordered,index,mutable,we can add different data and allow duplicate

# adding different data types
name_list = ['a','b','c',1,2,3,4.5]
print('our list is:',name_list, 'and type if name list is:',type(name_list))

# duplicates
name_list = ['a','b','c',1,2,3,4.5,3,3]
print(name_list)

#order : using index we can access item
print(name_list[0])
print(name_list[1])

# mutable : add or remove items
name_list.append(1)
name_list.append('Hema')
print(name_list)
name_list.remove(3)
print(name_list)



# using for loop print all the item in the list
list = ['hema', 'santu','pihu','chotu']

#way 1
for idx in range(0,4,1):
    print(list[idx])

#way 2 advanced for loop : it is always starts with 0 index and we can't fetch middle items
for item in list:
    print(item)


# create a smaller list from 1st  to 3rd item in the list
# way 1 using for loop

list = ['hema', 'santu','pihu','chotu','hemanth']
smaller_list = []
for idx in range(1,4,1):
    print(list[idx])
    smaller_list.append(list[idx])
print(smaller_list)


# List slicing --> it is available in only python
# way 2 using list slicing

smaller_list2 = list[1:4:1]
print(smaller_list2)

# get me 1st,3rd and 5th element from the list
# list = ['hema'(0), 'santu'(1),'pihu'(2),'chotu'(3),'hemanth'(4)]
print(list[0:5:2])



# tuple : ordered,index,immutable,we can add different data and allow duplicate
name_tuple = ('a','b','c',1,2,3,4.5,3)
print('my tuple is',name_tuple, 'and type is',type(name_tuple))
# Fstring way of printing
print(f'my tuple is {name_tuple} and type is {type(name_tuple)}')



# set : un-ordered collection of unique data and it is a mutable
name_set = {'a','b','c',1,2,3,4.5,3}
print(f'my set is {name_set} and type is {type(name_set)}')
name_set.add('Gundu')
print(name_set)

# print all the item from the set
for item in name_set:
    print(item)


'''
# special method applicable to set
# union , intersection, difference(minus/except)

num_set1 = {1,2,3,4}
num_set2 = {5,6,3,7}
# Union ( || --> this symbol called or)
final_set = num_set1 | num_set2
print('Union Operation')
print(num_set1.union(num_set2))
print(f'final_set is {final_set} and type is {type(final_set)}')
final_set = num_set1.union(num_set2)
print(f'final_set is {final_set} and type is {type(final_set)}')

# intersection ( & --> this symbol called and  )
final_set = num_set1 & num_set2
print('Intersection Operation')
print(f'final_set is {final_set} and type is {type(final_set)}')
final_set = num_set1.intersection(num_set2)
print(f'final_set is {final_set} and type is {type(final_set)}')

# Difference ( - --> this symbol called minus  )
final_set = num_set1 - num_set2
print('Difference Operation')
print(f'final_set is {final_set} and type is {type(final_set)}')
final_set = num_set1.difference(num_set2)
print(f'final_set is {final_set} and type is {type(final_set)}')

# symmetric Difference ( - --> this symbol called minus  )
final_set = num_set1 ^ num_set2
print('Symmetric Difference Operation')
print(f'final_set is {final_set} and type is {type(final_set)}')
final_set = num_set1.symmetric_difference(num_set2)
print(f'final_set is {final_set} and type is {type(final_set)}')
