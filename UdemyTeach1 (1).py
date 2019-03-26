#PRINT FORMATTING
'''
#name = input("What is your name? ")
#print("Good day {} I hope you are well.".format(name))

s = input("What is your name? ")
print("We can place a string within a string using a modulus and %s"%(s))

#Floating point formatting

#%x1.x2f x1 is the minimum number of digits before the dec place, x2 is the mimimum number after
print "this is a floating point number: %1.2f" %14.2345
this is a floating point number: 14.23
print "this is a floating point number: %1.0f" %14.2345
this is a floating point number: 14
print "this is a floating point number: %1.5f" %14.2345
this is a floating point number: 14.23450
print "this is a floating point number: %7.2f" %14.2345
this is a floating point number:      14.23

#multi point insertion (same type)
print "I have one number: %s. Then i have another number: %s" %(14.5, 34.5)
I have one number: 14.5. Then i have another number: 34.5
#Multiple formatting
print "i have one number here: %r then i have a string here: %r" %(24.5, 'hey')
i have one number here: 24.5 then i have a string here: 'hey'

#passing in multiple values i=using.format
#"some string {val}. i can add another value {val2}".format(val = 'value1', val2 = "value2")

#.format including raw_input to pass in multiline comments!!
print " this is using the .format {val1} you should understand at {val2} years old".format(val1 = raw_input("what is your name? "), val2 = raw_input("How old are you?"))
what is your name? Neil
How old are you?30
 this is using the .format Neil you should understand at 30 years old

 #similar... 
print("First name: {f}\nLast name: {l}".format(f = input("what is your first name?"), l = input("what is your last name?")))
#returns
#what is your first name?Neil
#what is your last name?Davis                           REMEMBER TO CHANGE RAW_INPUT TO INPUT IN HERE!
#First name: Neil
#Last name: Davis

print("First word: {w}\nSecond word: {w}\nThird word: {w}".format(w = input("pick three identical words!")))
pick three identical words!Triplets
First word: Triplets
Second word: Triplets
Third word: Triplets

from __future__ import print_function
print("first : {x}".format(x = 4.5))
first : 4.5

                      LISTS

#create list
my_list = [1,2,3,4,5]
print(my_list)
[1, 2, 3, 4, 5]

print(my_list[:4-1])
[1, 2, 3]

list2 = [1,4,9.9,8.4,'I can have strings']
print(list2)
[1, 4, 9.9, 8.4, 'I can have strings']

len(list2)
5

#indexing
list2[4]
'I can have strings'

list2 + ['hello world']                   adding stuff to lists
[1, 4, 9.9, 8.4, 'I can have strings', 'hello world']

#To make it permenant...
list2 = list2 + ['hello world']

list2 * 2
[1,
 4,
 9.9,
 8.4,
 'I can have strings',
 'hello world',
 1,
 4,
 9.9,
 8.4,
 'I can have strings',
 'hello world']
 
     #append method - adds an element at the end of the list
 list2.append('This will be appended')
 list2
 [1, 4, 9.9, 8.4, 'I can have strings', 'hello world', 'This will be appended']
 
     #to remove items from a list
 list2.pop(5)
 'hello world'
 list2
 [1, 4, 9.9, 8.4, 'I can have strings', 'This will be appended']

 list2.pop()   # this will remove an object from the end of th list
list2.pop()
list2.pop()
list2.pop()    #repeated removes multiplefrom the end
list2.pop()
4

my_list
[1, 2, 3, 4, 5]
my_list.reverse()
my_list
[5, 4, 3, 2, 1]

# coding: utf-8

# In[6]:

print("First word: {w}\nSecond word: {w}\nThird word: {w}".format(w = input("pick three identical words!")))


# In[8]:

from __future__ import print_function
print("first : {x}".format(x = 4.5))


# In[9]:

#create list


# In[10]:

my_list = [1,2,3,4,5]


# In[11]:

print(my_list)


# In[14]:

print(my_list[:4-1])


# In[15]:

list2 = [1,4,9.9,8.4,'I can have strings']


# In[16]:

print(list2)


# In[17]:

len(list2)


# In[18]:

#indexing
list2[4]


# In[20]:

list2[::-2]


# In[24]:

list2 + ['hello world']


# In[25]:

list2 = list2 + ['hello world']


# In[27]:

print(list2)


# In[28]:

list2 * 2


# In[29]:

#append method - adds an element at the end of the list


# In[30]:

list2.append('This will be appended')


# In[31]:

list2


# In[32]:

list2.pop(5)


# In[33]:

list2


# In[34]:

list2.pop()
list2.pop()
list2.pop()
list2.pop()
list2.pop()


# In[35]:

list2


# In[36]:

my_list


# In[39]:

my_list


# In[40]:

my_list.reverse()


# In[41]:

my_list


# In[42]:

list2


# In[49]:

list3 = ['n','e','i','l']


# In[50]:

list3


# In[51]:

list3.sort()


# In[52]:

list3


# In[53]:

list3.reverse()


# In[54]:

list3


# In[55]:

list3.sort()


# In[56]:

list3


# In[57]:

list4 = [4,6,2,2,2,5,8,1,1,9]


# In[58]:

list4


# In[60]:

list4


# In[66]:

list4.reverse()


# In[67]:

list4


# In[68]:

#nesting within lists **[lists[within[lists]]]


# In[69]:

firstlist = [1,3,5]
secondlist = [2,4,6]
thirdlist= [5,7,8]


# In[70]:

matrixlist = [firstlist,secondlist,thirdlist]


# In[71]:

matrixlist


# In[72]:

# using indexing to grab elements (we have multiple levels to index now)
#if we want to grab the [2,4,6] section then...


# In[76]:

matrixlist[1]


# In[77]:

matrixlist[1][0] # will grab the 0th index in the 1st list


# In[84]:

matrixlist[2][1]


# In[81]:

matrixlist[2].reverse()


# In[82]:

matrixlist[2]


# In[85]:

# how to delete elements


# In[95]:

subjects = ['math','chemistry','physics','art']


# In[87]:

subjects


# In[91]:

subjects


# In[92]:

#to delete physics     ===> use 'del' statement


# In[96]:

del subjects[2]


# In[97]:

subjects


# In[99]:

del subjects[0]


# In[100]:

subjects


# In[ ]:

tuple = (1,3,5,6)
tuple2 = (3,5,5.2,5.2,4.2,'string','in my tuple')
tuple2
(3, 5, 5.2, 5.2, 4.2, 'string', 'in my tuple')
tuple2.count(5.2)
2
tuple2.index('string')
5
'''

OPERATORS

#Arithmetic operators

There are 7 types:
+,-,/,*,**,%(remainder after division),//

#Python adheres to BODMAS

#Assignment operators

#These will change the value of of a variable after it's operation

=, assigns from right to left c = a+b
+=, add then =
-=, sub then =
*=, mul then =
/=, div then =

#Comparison operators

== Equal
!= not equal
< Less than
> Greater than
<= less than or equals
>= greater than or equals
<> Less than or greater than (basically NOT the same as)

#You can use these as boolean eg...
 A=5
 B=6
 a>b = False
 a<b = True


















