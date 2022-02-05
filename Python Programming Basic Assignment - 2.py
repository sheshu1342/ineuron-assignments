#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')
get_ipython().set_next_input('2. Write a Python program to convert Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')
get_ipython().set_next_input('3. Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')
get_ipython().set_next_input('4. Write a Python program to solve quadratic equation');get_ipython().run_line_magic('pinfo', 'equation')
get_ipython().set_next_input('5. Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[2]:


# convert kilometers to miles

a=int(input('enter the value:'))

km=a*0.621371
print('{}KM is = {} miles'.format(a,km))


# In[3]:


# Celsius to Fahrenheit

def fun2(a):
    b=(a*(9/5)) + 32
    print('{} degree celcius is = {} F'.format(a,b))
    
a=int(input('enter degree celcius:'))

fun2(a)


# In[4]:


# display calendar
import calendar

yy=int(input('enter the year :'))
mm=int(input('enter the month in mm format:'))

print(calendar.month(yy,mm))


# In[ ]:


# quadratic equation
import math

def quad():
    print('Quadratic eq is ax**2+bx+c=0 ')
    a=int(input('enter \'a\' a!=0 value:'))
    b=int(input('enter b value:'))
    c=int(input('enter c value:'))
    # descriminant calculation
    d=(b**2)-(4*a*c)
    
    sqr_root_value=math.sqrt(abs(d))
    sol1=(-b+sqr_root_value)/(2*a)
    sol2=(-b-sqr_root_value)/(2*a)
    print('under squr value',sqr_root_value)
    # checking condition for discriminant
    
    if d>0:
        print('roots are real and differen' )
        print(f'{sol1}')
        print(f'{sol2}')
        
    elif d==0:
        print(-b/(2*a))
        
        
    else:
        #sqr_root_value<0:
        print('complex roots' )
        print(-b/(2*a),'i',sqr_root_value)
        print(-b/(2*a),'-i',sqr_root_value)
        
         
quad()     


# In[1]:


#swap two variables without temp variable?

def fun9():
   
   a=int(input('enter the a value:'))
   b=int(input('enter the b value:'))
   
   a=a+b
   b=a-b
   
   a=a-b
   
   return(a,b)

fun9()


# In[ ]:




