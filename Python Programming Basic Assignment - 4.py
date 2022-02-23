#!/usr/bin/env python
# coding: utf-8

# Write a Python Program to Find the Factorial of a Number?
# 2. Write a Python Program to Display the multiplication Table?
# 3. Write a Python Program to Print the Fibonacci sequence?
# 4. Write a Python Program to Check Armstrong Number?
# 5. Write a Python Program to Find Armstrong Number in an Interval?
# 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[4]:


# factorial number

def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)
    

n=int(input('enter number:'))
print('factorial of',n, 'is',factorial(n))
factorial(n)


# In[1]:


#display multiplication program

def multi(m):
    i=1
    while i<=10:
        print(f'{m}x{i}={m*i}')
        i+=1
    print('done')   
m=int(input('enter the multiplication table:'))

multi(m)


# In[16]:


# Print the Fibonacci sequence
#1 2 3 4 5=0 1 1 3 5 7 9


def fibun(fib):
    if fib > 0:
        a=0
        b=1
        sum=0
        i=1
        while i<=fib:
            print(sum,end=' ')
            a=b
            b=sum
            
            sum=a+b
            i+=1
            
    else:
        print('input proper value:')

fib=int(input('enter the number'))
fibun(fib)


# In[9]:


# Python Program to Check Armstrong Number  
n=int(input('entered value:'))

if n>0:
    value=n
    power=len(str(n))
    num=int(n)
    result=0

    while n!=0:
        i=n%10
        result=result+i**power
        n=n//10

      
    if value==result:
        print('yes')
    else:
        print('no')

else:
    print('enter positive value')


# In[8]:


#Python Program to Find Armstrong Number in an Interval

def armt(a,b):
    for i in range(a,b+1):
        num=i
        p=len(str(i))
        result=0
        
        while (i!=0):
            d=i%10
            result=result+d**p
            i=i//10
        if num==result:
            print(num,end=' ')
    
a=int(input('enter the positive lower limit number:'))
b=int(input('enter the positive upper limit number:'))
armt(a,b)


# In[20]:


#Python Program to Find the Sum of Natural Numbers 0,1,2,3,4,5,6
1,3,6,10

def natural(b):
    s=0
    for i in range(1,b+1):

        s=s+(i)

    print(f'the sum of natural numbers upto {b} is {s}')
           
    
b=int(input('n th value to be entered:'))
natural(b)


# In[ ]:




