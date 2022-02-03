#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What are escape characters, and how do you use them');get_ipython().run_line_magic('pinfo', 'them')

the charector '\' is used as escape charectors to insert some words or to perform inside string .
use \ and enter the string that u want to inserts 

get_ipython().set_next_input('2. What do the escape characters n and t stand for');get_ipython().run_line_magic('pinfo', 'for')

n =new line t = tab space


get_ipython().set_next_input('3. What is the way to include backslash characters in a string');get_ipython().run_line_magic('pinfo', 'string')
by using \use @ at the begining

4. The string "Howl's Moving Castle" is a correct value. 
get_ipython().set_next_input("Why isn't the single quote character in the word Howl's not escaped a problem");get_ipython().run_line_magic('pinfo', 'problem')

ans: single quote preservce the literal value so this will consider its as charecter

get_ipython().set_next_input("5. How do you write a string of newlines if you don't want to use the n character");get_ipython().run_line_magic('pinfo', 'character')

ans: end " "
    
    
get_ipython().set_next_input('6. What are the values of the given expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello, world!'[1] = e
'Hello, world!'[0:5] = Hello 
'Hello, world!'[:5] = Hello
'Hello, world!'[3:] = lo, world!

get_ipython().set_next_input('7. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello'.upper()  = 'HELLO'
'Hello'.upper().isupper() =True
'Hello'.upper().lower() = 'hello'


get_ipython().set_next_input('8. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')

'Remember, remember, the fifth of July.'.split() 
= ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']


'-'.join('There can only one.'.split()) = 'There-can-only-one.'


get_ipython().set_next_input('9. What are the methods for right-justifying, left-justifying, and centering a string');get_ipython().run_line_magic('pinfo', 'string')

.rjust()
.ljust()
.center

get_ipython().set_next_input('10. What is the best way to remove whitespace characters from the start or end');get_ipython().run_line_magic('pinfo', 'end')
.strip()

