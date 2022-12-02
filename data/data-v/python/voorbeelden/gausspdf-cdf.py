# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:03:58 2017

@author: capel102
"""
import numpy as np
import matplotlib.pyplot as plt
# Deze regel laadt commando's omtrent de normale verdeling
from scipy.stats import norm

# Maak een lijst met x-waarden voor plotdoeleinden
x=np.arange(-5,5,.1) 
# Normale verdeling met verwachtingswaarde 0, standaarddeviatie 1:
# norm.pdf(x,loc=0,scale=1)
# Cumulatieve verdeling voor dezelfde gegevens:
# norm.cdf(x,loc=0,scale=1)

# Een plot van de verdeling en de cumulatieve verdeling
plt.plot(x,norm.pdf(x),label='PDF')
plt.plot(x,norm.cdf(x),label='CDF')
plt.legend()
plt.show()

# 1000 random getallen trekken
randnum=norm.rvs(loc=0,scale=1,size=1000)
# Een bin-histogrammetje van de data
plt.hist(randnum,normed=1)

# Berekening op de kans op een waarde tussen 2 en 3, 
# ongeveer 2.1%
print(norm.cdf(3,loc=0,scale=1)-norm.cdf(2,loc=0,scale=1))