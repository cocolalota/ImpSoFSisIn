#!/usr/bin/env python
# coding: utf-8

# In[3]:


class padre:
    mama = "madre"
    papa = "padre"

class hijo(padre):
    __hijo1 = "angel"
    def calificacion(self):
        print("6")

class hijo2(padre): 
    __hijo2 = "cristopher"
    def calificacion(self):
        print("9")

la_calificacion = hijo()
segundo = hijo2()
print(segundo.calificacion())
print(la_calificacion.calificacion())

