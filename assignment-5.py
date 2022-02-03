#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("1. What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')

ans   {}

2. What is the value of a dictionary value with the key 'foo' and the value 42?

ans { 'foo':42}

get_ipython().set_next_input('3. What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')

ans: dictionary is an key & value set input type ,list is an collection of ordered data
    
    
4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

ans: error, there is key or value 'foo
'

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
ans: expression 'cat' is stored as key in spam so no difference

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
ans: 'cat' is stored as key in spam and it will be paired with value 
     spam.values() finds the value pair of 'cat' 

get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')
if 'color' not in spam:
spam['color'] = 'black'

ans: spam.setdefault('color', black)

get_ipython().set_next_input('8. How do you "pretty print" dictionary values using which module and function');get_ipython().run_line_magic('pinfo', 'function')

ans: pprint.pprint()

