import matplotlib.pyplot as plt
import math

ingangshoekfrequentie = [30 * 2*math.pi
,40*2*math.pi
,50*2*math.pi
,60*2*math.pi
,70*2*math.pi
,80*2*math.pi
,90*2*math.pi
,100*2*math.pi
,110*2*math.pi
,120*2*math.pi
,130*2*math.pi
]

uitgangsspanning = [28.0
,27.2
,26.4
,25.2
,24.4
,23.2
,22.4
,21.6
,20.8
,20.0
,19.2
]

faserespons = [1.400
,1.720
,1.520
,1.320
,1.300
,1.240
,1.140
,1.220
,1.180
,1.020
,1.040
]

amplituderespons = [0.875
,0.85
,0.825
,0.7875
,0.7625
,0.725
,0.7
,0.675
,0.65
,0.625
,0.6
]

R = 100.1 * 10**3
C = 15.53 * 10**-9

theoretischeamplituderespons = []
theoretischefaserespons = []

for n in ingangshoekfrequentie:
    theoretischeamplituderespons.append(math.sqrt(1 / (1 + (n * R * C)**2))) 
    theoretischefaserespons.append(math.atan(-n * R * C))

plt.xscale('log')
plt.plot(ingangshoekfrequentie, faserespons)
plt.plot(ingangshoekfrequentie, theoretischefaserespons)


plt.ylabel('phi(w)')
plt.xlabel('w')

plt.show()
print(R*C)