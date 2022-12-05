# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:41:22 2017

@author: capel102
"""

import numpy as np
import matplotlib.pyplot as plt

# Uitkomsten verkregen met np.random.randint(6, size=30)
example=np.array([5,1,0,1,3,5,3,2,2,2,2,2,5,0,5,4,5,4,5,4,3,2,5,5,0,2,4,0,1,2])
# Mogelijke uitkomsten [0,1,2,3,4,5]
uitk=np.arange(6)
# Voor een bar-histogram moet je eerst de frequenties bepalen
# Dat kan bijvoorbeeld met np.bincount
# freq=np.bincount(example)
# Aantal keer voorgekomen zoals bepaald door bincount
freq=np.array([4,3,8,3,4,8])

## Bar-histogram
plt.figure()
# Plot van de data (zwarte punten)
plt.plot(uitk,freq,'ok')
# met plt.bar vullen we de y-as tussen 0 en de absolute frequenties 
# Het derde argument is de breedte van de bar. 
# Met color kun je de kleur gelijk stellen aan de punten
# (als je dat wilt)
plt.bar(uitk,freq,.05, color='k')

##Bin-histogram
# Bin-histogram (ongenormeerd, met 3 kolommen)
plt.figure()
plt.hist(example,3)
# Bin-histogram, genormeerd, 6 kolommen, gecentreerd op mogelijke uitkomsten
plt.figure()
plt.hist(example,6,density=True,range=(-0.5,5.5))
plt.show()