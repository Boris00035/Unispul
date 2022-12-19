# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:03:48 2022

@author: brech
"""

def polynoom(a,b,c,x):
    y = a*x**2 + b*x + c
    return y

i = 1
j = 2
k = 3
z = 1

waarde = polynoom(i,j,k,z) # hier gebruiken we positional arguments
print(waarde)
#%%

a = 20 # globale variabele a
b = 2 # globale variabele b
def f1(x):
    a = 21 # dit is een lokale variabele
    c = a*x + b # lokale a (waarde 21) en globale b (waarde =2)
    return c
def f2(x):
    global a
    a = 21 # de globale variabele a krijgt nu waarde 21
    c = a*x + b # zowel a als b zijn globale , maar c is lokaal
    return c
x = f1 (3);
print(x) # geeft 21*3=2 = 61
print(a) # geeft 20
y = f2 (3);

print(y) # geeft 21*3=2 = 61
print(a) # geeft 21 want f2 heeft de globale a gewijzigd.

#%%

#5.2.1

def polynoom(a,b,c,x):
    print('binnen functie geldt a = ', a)
    return a*x**2 + b*x + c

a=3.14
f = polynoom(x=3.14, a=1, b=1, c=1)
print('buiten functie geldt a = ', a)


#%%
def f(a,b):
    return a+2*b

print(f(1 ,2)) # 5
print(f(2 ,1)) # 4

#%%
def polynoom(a,b,c,x):
    y = a*x**2 + b*x + c
    return y

i = 1
j = 2
k = 3
z = 1

waarde = polynoom(i,j,k,z) # hier gebruiken we positional arguments
print(waarde)


#%%
#5.4.1.1
def som(a,b,c):
    y = a + b + c
    return y


waarde = som(1,2,3)
print (waarde)

a = 2
b = 3
c = 4
waarde2 = som(a,b,c)
print(waarde2)

print(som(3,4,5))


#%%
#5.4.1.2
import numpy as np
import matplotlib.pyplot as plt

# Rechte lijn
def f(x,a,b):
    return a+b*x

# Sinus
def g(x,amp,freq,offset):
    return offset + amp*np.sin(freq*x)

def k(x,a,b,c):
    return a*x**2 + b*x + c

## Simpele plotfunctie
# plot functie "func" over range "x"
# extra argumenten worden doorgegeven met *args
def my_plot(x,func,*args):
    plt.plot(x,func(x,*args))
    plt.show()
    
## Gebruik:
x_arr = np.linspace(-5.,5.)


#print(my_plot(x_arr,f,1,2))
#print(my_plot(x_arr,g,1,2,3))

print(my_plot(x_arr,k,1,1,1))

#%%

def f(farg, *args, **kwargs):
    print("Het formele argument is", farg)
    print("De extra argumenten zijn:")
    for arg in args:
        print(arg)
    print("De keyword argumenten zijn:")
    for key in kwargs:
        print("  de key",key,"met argument",kwargs[key])
        if key == 'my_name':
            print("Mijn naam is", kwargs[key])
            
## Aanroepen van bovenstaande functie:
f("Aap", "Noot", "Mies", arg4="Wim" ,my_name="Zus")
# in bovenstaande aanroep zijn:
# Formeel argument   "Aap"
# Extra   argumenten "Noot" en "Mies"
# Keyword argumenten "Wim" bij keyword arg4, en "Zus" bij my_name

#%%
#5.6.1

import numpy as np


def sin_func(x, A=1, P=2*np.pi, phase=0, v=0):
    return A*np.sin((2*np.pi/P)*(x + phase)) + v
def sin_func2(x, A=1, P=np.pi, phase=0, v=0):
    return A*np.sin((2*np.pi/P)*(x + phase)) + v
def sin_func3(x, A=0.5, P=2*np.pi, phase=np.pi/2, v=1):
    return A*np.sin((2*np.pi/P)*(x + phase)) + v

x = np.linspace(-5.,5.)

plt.plot(x,sin_func(x))
plt.plot(x,sin_func2(x))
plt.plot(x,sin_func3(x))


#%%
import mypolyimport as mp
import numpy as np

import os
file = os.path.dirname(__file__)
os.chdir(file)
#def poly(x,a,b,c):
  #  return a*x**2 + b*x + c
x = np.arange (0 ,11 ,1)
y = mp.poly(x,4 ,3 ,2)

plt.plot(x,y)
plt.show()

#%%

#5.7.1

def my_plot(x, y, xlabel, ylabel, xerror=None,yerror=None, xrange=None,yrange=None):
      plt.figure()
      plt.plot(x,y)
      plt.xlabel(xlabel)
      plt.ylabel(ylabel)
      plt.errorbar(x, y, xerr=xerror, yerr= yerror, fmt='.k')
      plt.xlim(xrange)
      plt.ylim(yrange)
      plt.show()

#%%

#5.7.2

import numpy as np

def my_plot(x, An, x0 = 0, y0 = 0):
 #   som = 0
     y = []
     for i in range(len(An)):
         y.append(y0 + An[i]*(x0-x[i])**(i + 1))
     return np.sum(np.array(y))

print(my_plot(np.array([1,2,3]), np.array([1,2,3])))


#%%


import numpy as np

def my_plot(t, An, f_0 = 0, t_0 = 0, phi_0 = 0):
 #   som = 0
     y = []
     for i in range(len(An)):
         y.append(An*np.sin((i + 1)*2*np.pi*f_0*(t - t_0) + phi_0))
     return np.sum(np.array(y))

print(my_plot(np.array([1,2,3]), np.array([1,2,3])))

