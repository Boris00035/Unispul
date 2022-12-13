import numpy as np
import matplotlib.pyplot as plt
import os

file = os.path.dirname(__file__)
os.chdir(file)

plt.figure(1) # begin met opbouwen van Figuur 1, default afmeting
 
x = np.linspace(-2*np.pi, 2*np.pi)
y = np.sin(x)
plt.plot(x, y, color = 'red')  # 1 curve is getekend

# nu een gladdere curve tekenen door meer (dan 50) punten te kiezen 
x = np.linspace(-2*np.pi, 2*np.pi, num=200)
y = np.sin(x)

# de breedte van de te tekenen curve moet ook worden aangepast
# anders zie je nog geen verschillen met de rode lijn
plt.plot(x, y, linewidth=0.1, color='black')

plt.savefig('sinus.png')      # sla verschillende bestandstypen 
plt.savefig('sinus.pdf')      # op om te kunnen vergelijken

plt.figure(2, figsize=[8,4])  # begin met opbouwen van Figuur 2
                              # met opgegeven afmeting in inches
plt.plot(x, np.cos(x))
plt.savefig('cosinus.pdf')    # ... en weer een figuur opgeslagen.