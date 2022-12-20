import numpy as np
import matplotlib.pyplot as plt
import time

def fourierreeks(t, A_n, f_0, phi_n = None, t_0 = 0):
    if phi_n is None:
        phi_n = np.zeros(len(A_n))
    elif len(A_n) != len(phi_n):
        print("De lijsten zijn niet even groot")
        return 

    y_t_list = np.array([])
    for i in t:
        y_t_list = np.append(y_t_list, np.sum( A_n * np.sin(2*np.pi* np.arange(len(A_n)) *f_0*(i - t_0) + phi_n)) )

    return y_t_list

#functie voor D(t)
def my_plot(t, f_0=0):
    D_t=4*abs(f_0*t+(1/4)-np.floor(f_0*t+(3/4)))-1
    return D_t

#functie voor Z(t)
def my_plot2(t, f_0=0):
    Z_t=f_0*t-np.floor(f_0*t)-(1/2)
    return Z_t  

#functie voor S(t)
def my_plot3(t, f_0=0):
    S_t=np.sin(2*np.pi*t*f_0)
    return S_t

def gen_coefs_driehoeksgolf(n):
    coefs_list = np.array([])
    for i in range(n):
        if i % 2 == 0:
            coefs_list = np.append(coefs_list, 0)
        else:
            coefs_list = np.append(coefs_list, (-1)**( (i - 1) / 2 ) / i**2)
    return coefs_list * 8 / (np.pi**2)

def gen_coefs_zaagtandgolf(n):
    coefs_list = np.array([0])
    for i in range(1, n):
        coefs_list = np.append(coefs_list, -1/(np.pi * i))
    return coefs_list


# t = np.linspace(0,1,num=100)
# plt.figure() 
# plt.plot(t, fourierreeks(t, np.array([1,2]), 1))
# plt.xlabel("t")


#opdracht 2b, plot van D(t), Z(t) en S(t)
# t = np.linspace(0,1/2,num=200)
# plt.figure() 
# plt.plot(t,  my_plot(t, f_0=2), label = 'D(t)')
# plt.plot(t, my_plot2(t, f_0=2), label = 'Z(t)')
# plt.plot(t, my_plot3(t, f_0=2), label = 'S(t)')
# plt.xlabel("t")
# plt.legend()
# plt.show()

t = np.linspace(0,3,num=1000)
plt.figure()

plt.plot(t, fourierreeks(t, gen_coefs_driehoeksgolf(100), 1))
plt.plot(t, fourierreeks(t, gen_coefs_zaagtandgolf(100), 1))

plt.xlabel("t")
plt.show()

















