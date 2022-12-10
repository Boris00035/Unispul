import numpy as np
import math
from scipy.stats import norm
import matplotlib.pyplot as plt

def average(list):
    avg = sum(list) / len(list)
    return avg

def std_dev_avg(list):
    std_dev = math.sqrt(1/len(list)) * average(list)
    return std_dev


# fig = plt.figure()
# ax = fig.add_subplot(111)

# # Volgorde: Mercurius, Venus, Aarde, Mars, Jupiter, Saturnus, Uranus, Neptunus
# # Omlooptijden T in jaren
# T = [0.24,0.62,1.00,1.88,11.86,29.46,84.01,164.8]
# # Gemiddelde afstand tot de zon a in AU
# a = [0.39,0.72,1.00,1.52,5.20,9.54,19.22,30.06]

# for n in range(1, len(T)):
#     T[n] = T[n]**2
#     a[n] = a[n]**3

# ax.plot(T,a)

# plt.show()

# Massadichtheid \rho in g/cm^3
# np.array([18.5,21.0,16.8,15.3,19.6,19.8])

## opdracht 2.5.1

# fib_num1 = 0
# fib_num2 = 1

# for n in range(0, 10):
#     print(fib_num1)
#     fib_num3 = fib_num1 + fib_num2
#     fib_num1 = fib_num2
#     fib_num2 = fib_num3


# # opdracht 2.5.2

# for num in range(2, 6):
#     for pot_divisor in range(2, num + 1):
#         if pot_divisor == num:
#             print(num, "prime")
#             break
#         if num % pot_divisor == 0:
#             print(num, "Not a prime")
#             break

# # opdracht 3.9

# array = [98.7, 95.3, 95.9, 98.3, 96.3, 93, 100.2, 96.4, 98.9, 93.2]
# error = [0.4, 1.6, 3.0, 0.4, 2.8, 7, 1.0, 1.2, 0.8, 6.2]
# x = np.linspace(0, len(array), len(array))

# plt.errorbar(x, array, yerr=error, fmt='.k')
# # plt.show()
# print(average(array))
# print(std_dev_avg(array))

# # opdracht 4.2

# mu1 = 2
# sigma1 = 1
# mu2 = 1
# sigma2 = 2
# x = np.linspace(mu2 - 3*sigma2, mu1 + 3*sigma2, 100)
# plt.plot(x, norm.pdf(x, mu1, sigma1))
# plt.plot(x, norm.pdf(x, mu2, sigma2))

# # plt.show()

# print(norm.cdf(mu1 + sigma1/1.5, mu1, sigma1) - norm.cdf(mu1 - sigma1/1.5, mu1, sigma1))
