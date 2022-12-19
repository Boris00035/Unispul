import numpy as np
import matplotlib .pyplot as plt


#functie voor D(t)
def my_plot(t, f_0=0.0):
    D_t=4*abs(f_0*t+(1/4)-np.floor(f_0*t+(3/4)))-1
    return D_t


#functie voor Z(t)
def my_plot2(t, f_0=0.0):
    Z_t=f_0*t-np.floor(f_0*t)-(1/2)
    return Z_t  

#functie voor S(t)
def my_plot3(t, f_0=0.0):
    S_t=np.sin(2*np.pi*t*f_0)
    return S_t


#plot van D(t), Z(t) en S(t)
t = np.linspace(0,10,num=100)
plt.figure() 
plt.plot(t,  my_plot(t, f_0=0.1), label = 'D(t)')
plt.plot(t, my_plot2(t, f_0=0.1), label = 'Z(t)')
plt.plot(t, my_plot3(t, f_0=0.1), label = 'S(t)')
plt.xlabel("t")
plt.legend()
plt.show()






