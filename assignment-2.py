#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
0 & 1
True = 1
False = 0


# In[ ]:


get_ipython().set_next_input('2.What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

AND ,OR ,NOT


# In[ ]:


3.Make a list of each Boolean operator's truth tables 
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).


BOOLEAN    imput    output

and        0  1        0
           1  0        0
           1  1        1
           0  0        0

or         0  1        1
           1  0        1
           1  1        1
           0  0        0 
            
         
            
not        0           1
           1           0
         
                            


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')

(5 > 4) and (3 == 5) 
Ans : False
    
not (5 > 4)
Ans : False
    
(5 > 4) or (3 == 5)
Ans : True
    
not ((5 > 4) or (3 == 5))
Ans : False
    
(True and True) and (True == False)
Ans : False
    
(not False) or (not True)
Ans : True


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

==
>
<
>=
<=
get_ipython().system('=')


# In[ ]:


6.How do you tell the difference between the equal
to and assignment operators?Describe a condition and when you would use one.

ans: assignment(a=5) to assign values to the variables. 
    5==5 is eqals to that returns as True.


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

--------------------
ans:
    
spam = 0
if spam == 10: # 1st block
    print('eggs')
    
if spam > 5:  # 2nd  block
    print('bacon')
      
else:  # 3rd block
    print('ham')
    print('spam')
    print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, 
prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

-----------
def fun(int(input())):
    if a


# In[ ]:


spam=int(input('enter 1 or 2 :'))
try:
    if spam == 1:
        print('Howdy')
    elif spam==2:
        print('spam')
    else:
        print('Greetings!')
except Exception as e:
    print('check code',e)


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

ans: break , cntl+c


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

ans: break - to interupt or come out of loop
    continue - to keep in the loop


# In[ ]:



11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

ans: there is no difference ,all gives same results  # it prints 0-9 values except 10 value ,
    #range(0,10,1) 1 is the jump sequence


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

ans: 
    for i in range(1,11):
    print(i)
    
    i=0
    while(i<10):
    print(i+1)
    i += 1


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

ans:
    spam.bacon()

