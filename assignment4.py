#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	What exactly is []?
Its an square bracket used to assign list (Ordered & muteable )


# In[3]:


#2.	In a list of values stored in a variable called spam,
#how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

Spam.insert(2,'helloe')


# In[ ]:


#. What are the list concatenation and list replication operators?

concatenation by use []+[]
replication []*


# In[ ]:


Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
3. What is the value of spam[int(int('3' * 2) / 11)]?

ans: 'd'
    
4. What is the value of spam[-1]?

ans: 'd'
    
5. What is the value of spam[:2]?
ans: a,b


# In[ ]:


#Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

6. What is the value of bacon.index('cat')?
ans: 1
    
get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')
ans:[3.14, 'cat,' 11, 'cat,' True,99]
    
get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')
ans: [3.14, ' 11, ' True,99]


# In[ ]:


# What is difference between the list methods append() and insert()?

Append is used to add the data at the last/end of the list

insert is to add data to a specific location


# In[ ]:


# What are the two methods for removing items from a list?

pop & remove

# 12. Describe how list values and string values are identical.

the values & string values are orderly collecting inside the list. they are ordered collection

# What's the difference between tuples and lists?

tuples are immutable ,and used to represent ()
list are mutable and represented by []

# 14. How do you type a tuple value that only contains the integer 42?
t=(42,)

# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?

by using tuple() 

list() functions

#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

they contain the reference. address of the location

#17. How do you distinguish between copy.copy() and copy.deepcopy()?

copy.copy is shallow copycreats copy of the object but references each element of the object
copy.deep copy creats a copy of the object and the elements of the object.
.

