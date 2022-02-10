#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to Check if a Number is Positive, Negative or Zero');get_ipython().run_line_magic('pinfo', 'Zero')
get_ipython().set_next_input('2. Write a Python Program to Check if a Number is Odd or Even');get_ipython().run_line_magic('pinfo', 'Even')
get_ipython().set_next_input('3. Write a Python Program to Check Leap Year');get_ipython().run_line_magic('pinfo', 'Year')
get_ipython().set_next_input('4. Write a Python Program to Check Prime Number');get_ipython().run_line_magic('pinfo', 'Number')
5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# In[3]:


# Check if a Number is Positive, Negative or Zero

def fun():
    a=int(input('Enter the value:'))
    if a>0:
        print('entered value is positive:')
    elif a<0:
        print('entered value is negative:')
    else:
        print('entred value is equals to zero:')
        
fun()
    


# In[11]:


# Check if a Number is Odd or Even

def fun2():
    
    b=int(input('enter the int values:'))
    
    
    if (b%2)==0:
        print('entered value is even:',b)
    else:
        print('enteerd value is odd:',b)
        
fun2()
    
    


# In[33]:


# Check Leap Year

def leap(year):
    
    # leap is divisible by 4 if it is not century
    # if year is century it is divisible by 400
    
    if (year%400==0) or (year%100!=0)and(year%4==0):
        print('entered year is leap year:',year)
    else:
        print('entered year is not leap year:',year)
        
year=int(input('enter the year:'))

leap(year)
    


# In[2]:


# Check Prime Number
from math import sqrt
num=10
for i in range(2,num):
    if num % i ==0:
        print('not prime')
        break
else:
    print('prime')


# In[5]:


n=int(input('enter the value to find:'))
prime_flag=0

if(n>1):
    for i in range(2,int(sqrt(n))+1):
        if(n%i ==0):
            prime_flag=1
            break
    if (prime_flag==0):
        print('prime')
    else:
        print('not prime')
else:
    print('false')
    


# In[11]:


def isPrime(n):

    for i in range(1,n):
        if (i%n==0):
            return False
    else:
        return True

N=1001

for i in range(1,N):
    if (isPrime(i)):
        print(i,end=' ')


# In[ ]:




