import numpy as np 
#import matplotlib.pyplot as plt

#a 
#onderstaande numpy array bevat de gemten valtijden t1 tot t40

valtijden = np.array([63, 58, 74, 78, 70, 74, 75, 82, 68, 69, 76, 62, 72, 88, 65, 81, 79, 77, 66, 76, 86, 72, 79, 77, 60, 70, 65, 69, 73, 77, 72, 79, 65, 66, 70, 74, 84, 76, 80, 69])

#Nu berekenen we de gemiddelde valtijd, tgem
tgem = np.mean(valtijden)
print(
    'De gemiddelde valtijd zoals berekend door python is', 
    tgem, 
    ' in honderste secondes.'
    )

#Nu berekenen we de standaarddeviatie:
tsd = np.std(valtijden,ddof=1)
print(
    'De standaarddeviatie is zoals berekend door python is', 
    tsd, 
    'in honderste secondes.'
    )

#b
#We herschikken onze numpy array zodat deze wordt opgedeeld in tien kolommen.
valtijdenk = valtijden.reshape(4,10)
#We maken hier een numpy array van zodat we straks de standaardeviatie uit
#kunnen rekenen.
valtijdenknp = np.array(valtijdenk)
    
#Nu berekenen we de gemiddeldes en standaarddeviatie van deze arrays.

deeltgem = np.mean(valtijdenknp, axis=0)
    
#c

#We bereken de gemiddelde valtijd en de standdaarddeviatie van de 10 deel 
#experimenten:
tdeelgem = np.mean(deeltgem)

tdeelstd = np.std(deeltgem,ddof=1)