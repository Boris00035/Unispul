import numpy as np

def fourierreeks(t, A_n, f_0, phi_n = None, t_0 = 0):
    if phi_n is None:
        phi_n = np.zeros(len(A_n))
    elif len(A_n) != len(phi_n):
        print("De lijsten zijn niet even groot")
        return 

    y_t_list = []
    for i in t:
        y_t_list.append( np.sum(A_n * np.sin(2*np.pi* np.arange(len(A_n)) *f_0*(i - t_0) + phi_n)) )

    return y_t_list

print( fourierreeks(np.array([0.25, 0.25]), np.array([1,2]), 1) )


