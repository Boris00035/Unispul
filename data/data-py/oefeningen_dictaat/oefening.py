import math
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

import csv

# # opdracht 2.1.1
# def ex_or(input1, input2):
    # if (input1 or input2) and not (input1 and input2):
#         return True
#     else:
#         return False

# print(ex_or(True,True))
# print(ex_or(True,False))
# print(ex_or(False,True))
# print(ex_or(False,False))

# opdracht 2.3.1
# input = int(input("Geef een positief getal: "))

# if input >= 0:
#     print(math.sqrt(input))

# # opdracht 2.4.1
# lijst1 = list(range(0, 99))
# lijst3 = []

# for n in lijst1:
#     lijst3.append(lijst1[n] * 100 - lijst1[n]**2) 

# print(lijst3)

# # opdracht 2.4.2
# lijst_celcius = [7, 24, 19, 88, 79, 3.35, -10]

# for n in range(0, len(lijst_celcius)):
#     if lijst_celcius[n] <= 0:
#         print("Fahrenheit: ", lijst_celcius[n] * (9/5) + 32, "het vriest")
#     else:
#         print("Fahrenheit: ", lijst_celcius[n] * (9/5) + 32, "het vriest niet")

# # opdracht 2.5.1
# a = 1
# b = 1
# print(a)
# print(b)
# for n in range(0, 100):
#     c=a+b 
#     print(c)
#     a=b
#     b=c
    
# # opdracht 2.5.2

# n = 5

# for i in range(2, n):
#     if n % i == 0:
#         break
    
#     if i == n - 1:
#         print(n, 'prime')

# # opdracht 3.1.1

# k = 10

# arr = np.arange(0, k, 1)
# arr1 = []

# for n in arr:
#     arr1.append(arr[n]**arr[n])

# avg = max(arr1) / len(arr1)
# print(avg)

# # opdracht 3.3.1 oplossing 1

# y = np.arange(30)
# np.random.shuffle(y)

# y1 = np.array([])

# for i in y:
#     if i % 2 == 1:
#         y1 = np.insert(y1, 0, i)
#     else:
#         y1 = np.append(y1, i)
#     # print(y1)

# y = y1
# y = np.sort(y.reshape(2,15))
# print(y)
            
# opdracht 3.3.1 oplossing 2

# y = np.arange(30)
# np.random.shuffle(y)

# y.sort()

# print(y.reshape(15,2).T)

# f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

# x = np.linspace(0,2*np.pi)

# ax1.plot(x,np.cos(x)**2)
# ax2.plot(x,np.sin(x)**2)
# ax3.plot(x,np.cos(x)*np.sin(x))

# # f.subplots_adjust(hspace=0.1)
# plt.xticks()

# f.suptitle("Drie plotjes tegelijk")
# plt.show()

# f, axarr = plt.subplots(2, 2, sharex='col', sharey='row')

# x = np.linspace(0,2*np.pi)

# axarr[0,0].plot(x,np.cos(x)**2)              
# axarr[0,1].plot(x,np.sin(x)**2)            
# axarr[1,0].plot(x,np.cos(x)*np.sin(x))        
# axarr[1,1].plot(x,np.cos(x)**2*np.sin(x)**2)   

# f.suptitle("Vier plotjes tegelijk")
# plt.imshow()

# # opdracht 3.7.1 random getallen en pi

# np.random.seed(43892)
# max_aantal_samples = 1000

# def calculate_pi(aantal_samples):
#     unif = np.random.rand(int(aantal_samples),2)
#     masker = [1 if math.sqrt(j[0]**2 + j[1]**2) < 1 else 0 for j in unif]

#     ratio = np.average(masker)
#     return 4 * ratio

# x_as = np.linspace(0,max_aantal_samples, max_aantal_samples)
# y_as = []

# for i in x_as:
#     print(i)
#     y_as.append(np.pi - calculate_pi(i))

# # plt.xscale('log')
# # plt.yscale('log')

# plt.plot(x_as,y_as)

# plt.show()

# writing to csv files

# f = open('test.csv', 'w', newline='')

# writer = csv.writer(f)

# row = ['x_as', 'y_as']
# writer.writerow(row)

# test_inputs = np.linspace(0,10,11)
# test_metingen = np.random.rand(11)

# test_metingen_sci_format = []

# for i in range(0, len(test_metingen)):
#     test_metingen_sci_format.append(np.format_float_scientific(test_metingen[i], 3))

# twod_data_matrix = np.array([test_inputs, test_metingen_sci_format])

# writer.writerows(np.transpose(twod_data_matrix))


# f.close()







    