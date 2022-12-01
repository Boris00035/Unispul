# import numpy as np
# import matplotlib.pyplot as plt

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