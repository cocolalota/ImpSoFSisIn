#!/usr/bin/env python
# coding: utf-8

# In[1]:


try: 
    if'carlos' == carlos.nombre: 
        print("eres carlos")
except NameError:
    print("define la variable carlos primero")

escribe tu edad:   22
24
define la variable carlos primero 


# In[9]:


lista =[1,2,3]
print(lista[4])


# In[17]:


for line in open("myfile.txt"):
    print(line, end="")


# In[25]:


x = "5"
y = 10
print(x + y)


# In[27]:


diccionario = {'a': 1, 'b': 2}
print(diccionario['c'])


# In[29]:


int("hola")


# In[31]:


a = 10
b = 0
print(a / b)


# In[33]:


import noexiste


# In[35]:


print(variable_inexistente)


# In[37]:


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n)

print(factorial(5))


# In[ ]:




