#mytuple=(1,2,3,4,5,6)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
#mytuple=mytuple + (9,)

#adding items in a specific index
#mytuple = mytuple[:5] + (15, 20, 25)


#converting the tuple to list
#mytuple=list(mytuple)

#print(mytuple)

#Create a tuple with numbers
"""tuplex = 5, 10, 15, 20, 25
print(tuplex)
#Create a tuple of one item
tuplex = 5,
print(tuplex)"""
#Create an empty tuple

"""x = ()
print(x)"""


#create a tuple
"""tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuplex)
"""
#return the number of times it appears in the tuple./ how many times one element in repeat items
"""count =tuplex.count(4)
print(count)"""
"""listx.append(30)
tuplex = tuple(listx)
print(tuplex)
"""
#Convert list to tuple
list1=[1,2,3,4,]
print(list1)
tuple=tuple(list1)
print(tuple)

# convert tuple string
tuple=("A","N","J","U")
str=''.join(tuple)
print(str)

#slice tuple
tuple = (1,2,3,4,5,6,7,8,9)
slice=tuple[3:5]
print(slice)

#if the start index isn't defined, is taken from the beg inning of the tuple
slice = tuple[:5]
print(slice)

#if the end index isn't defined, is taken until the end of the tuple
slice = tuple[2:]
print(slice)


#if neither(Star/End) is defined, returns the full tuple
slice = tuple[:]
print(slice)

#The indexes can be defined with negative values
slice = tuple[-5:-1]
print(slice)

#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
slice = tuple[2:9:2]
print(slice)


#returns a tuple with a jump every 3 items
slice = tuple[::3]
print(slice)


#when step is negative the jump is made back
slice = tuple[9:2:-2]
print(slice)