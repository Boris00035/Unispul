import numpy as np
import matplotlib.pyplot as plt

# functiedefinities:

# De functie fourierreeks neemt 3 verplichte argumenten.
# t is een array van waardes waarvan we de functiewaarden willen weten.
# A_n is een array van waardes die de coeficienten van de fourier serie representeren.
# f_0 is de frequentie van de golf.
# de optionele argumenten zijn phi_n en t_0; deze staan voor het fase verschil en het tijdsverschil van de functie.  

def fourierreeks(t, A_n, f_0, phi_n = None, t_0 = 0):
    if phi_n == None:                                   # De default waarde phi_n is een array van nullen, met dezelfde lengte als A_n.
        phi_n = np.zeros(len(A_n))                      # Omdat de default waarde niet in de functie definitie kan afhangen van A_n,
    elif len(A_n) != len(phi_n):                        # maken we de default None en vervangen we deze met een array van nullen.
        print("De lijsten zijn niet even groot")        # Als de waarde van phi_n niet None is, testen we hier ook of de gegeven array
        return                                          # wel van de goede grootte is, en geven anders een error.

    y_t_list = np.array([])                             # Hier wordt de lijst waar alle functie waardes in terechtkomen geinitialiseerd.
    for i in t:                                         # Bereken voor elke waarde in de lijst t de functie waarden.
        y_t_list = np.append(y_t_list, np.sum( A_n * np.sin(2*np.pi* np.arange(len(A_n)) *f_0*(i - t_0) + phi_n)) )

    return y_t_list                                     # Return de berekende array van functiewaarden.

# functie voor D(t), berekent de functiewaarde van een driehoeksgolf met een bepaalde frequentie op een punt t.
def driehoek_golf(t, f_0=0):
    D_t = 4*abs(f_0*t+(1/4)-np.floor(f_0*t+(3/4)))-1
    return D_t

# functie voor Z(t), berekent de functiewaarde van een zaagtandgolf met een bepaalde frequentie op een punt t.
def zaagtand_golf(t, f_0=0):
    Z_t=f_0*t-np.floor(f_0*t)-(1/2)
    return Z_t  

# functie voor S(t), berekent de functiewaarde van een "gewone" sinusgolf met een bepaalde frequentie op een punt t.
def sinus_golf(t, f_0=0):
    S_t=np.sin(2*np.pi*t*f_0)
    return S_t

# Deze functie neemt een n als argument en returned een array van de eerste n coefficienten van de fourier serie van een driehoekgolf.
# Er zijn efficientere manieren om om te gaan met de even / oneven definitie van deze functie, helemaal omdat het even geval constant is,
# maar we hebben hier toch gekozen voor de meest voor de hand liggende manier door te testen of i even of oneven is.
def gen_coefs_driehoeksgolf(n):
    coefs_list = np.array([])
    for i in range(n):
        if i % 2 == 0:
            coefs_list = np.append(coefs_list, 0)
        else:
            coefs_list = np.append(coefs_list, (-1)**( (i - 1) / 2 ) / i**2)
    return coefs_list * 8 / (np.pi**2)

# Deze functie neemt een n als argument en returned een array van de eerste n coefficienten van de fourier serie van een zaagtandgolf.
def gen_coefs_zaagtandgolf(n):
    coefs_list = np.array([0])
    for i in range(1, n):
        coefs_list = np.append(coefs_list, -1/(np.pi * i))
    return coefs_list

# Deze functie neemt twee arrays, en berekent de som van de kwadraten van de verschillen van elk element van de arrays.
def tot_kwadratisch_verschil(arr1, arr2):
    if arr1.size != arr2.size:                                                              # Hier wordt getest of de arrays dezelfde grootte hebben.
        print("Voor het kwadratisch verschil moeten de arrays dezelfde grootte hebben.")
        return

    return np.sum( (arr1 - arr2)**2 )

# opdracht 6.3 final
# a, driehoek:
t = np.linspace(0,1,num=1000)                                                               # Maakt een linspace aan.

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)                                      # Dit maakt de figuur aan.

ax[0,0].plot(t,  driehoek_golf(t, f_0=1), label = 'D(t)')                                   # Plot de orginele functie linksboven.
ax[0,0].plot(t, fourierreeks(t, gen_coefs_driehoeksgolf(2), 1), label = 'Fourier D(t)')     # Plot de fourier series op dezelfde plek.
ax[0,0].legend()                                                                            # Teken een legenda.
ax[0,0].set_title('n = 2')                                                                  # Zet een titel van de subfiguur.

ax[0,1].plot(t,  driehoek_golf(t, f_0=1), label = 'D(t)')
ax[0,1].plot(t, fourierreeks(t, gen_coefs_driehoeksgolf(5), 1), label = 'Fourier D(t)')
ax[0,1].legend()
ax[0,1].set_title('n = 5')

ax[1,0].plot(t,  driehoek_golf(t, f_0=1), label = 'D(t)')
ax[1,0].plot(t, fourierreeks(t, gen_coefs_driehoeksgolf(10), 1), label = 'Fourier D(t)')
ax[1,0].legend()
ax[1,0].set_title('n = 10')

ax[1,1].plot(t,  driehoek_golf(t, f_0=1), label = 'D(t)')
ax[1,1].plot(t, fourierreeks(t, gen_coefs_driehoeksgolf(15), 1), label = 'Fourier D(t)')
ax[1,1].legend()
ax[1,1].set_title('n = 15')

fig.suptitle('Illustratie Fourierseries driehoeksgolf')

plt.gcf().set_size_inches(8, 6)                                                            # De default grootte waarmee matplotlib een foto opslaat is aan de kleine kant, hiermee pas ik de grootte aan van het plaatje. 
fig.savefig('../images/Fourier_driehoekgolf.png', bbox_inches='tight', dpi=200)  
# En als laatste sla het plaatje op.
plt.show()

# zaagtand
t = np.linspace(0,1,num=1000)                                                               # Maakt een linspace aan.

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)                                      # Dit maakt de figuur aan.

ax[0,0].plot(t,  zaagtand_golf(t, f_0=1), label = 'Z(t)')                                   # Plot de orginele functie linksboven.
ax[0,0].plot(t, fourierreeks(t, gen_coefs_zaagtandgolf(2), 1), label = 'Fourier Z(t)')     # Plot de fourier series op dezelfde plek.
ax[0,0].legend()                                                                            # Teken een legenda.
ax[0,0].set_title('n = 2')                                                                  # Zet een titel van de subfiguur.

ax[0,1].plot(t,  zaagtand_golf(t, f_0=1), label = 'Z(t)')
ax[0,1].plot(t, fourierreeks(t, gen_coefs_zaagtandgolf(5), 1), label = 'Fourier Z(t)')
ax[0,1].legend()
ax[0,1].set_title('n = 5')

ax[1,0].plot(t,  zaagtand_golf(t, f_0=1), label = 'Z(t)')
ax[1,0].plot(t, fourierreeks(t, gen_coefs_zaagtandgolf(10), 1), label = 'Fourier Z(t)')
ax[1,0].legend()
ax[1,0].set_title('n = 10')

ax[1,1].plot(t,  zaagtand_golf(t, f_0=1), label = 'Z(t)')
ax[1,1].plot(t, fourierreeks(t, gen_coefs_zaagtandgolf(15), 1), label = 'Fourier Z(t)')
ax[1,1].legend()
ax[1,1].set_title('n = 15')

fig.suptitle('Illustratie Fourierserie zaagtandgolf')

plt.gcf().set_size_inches(8, 6)                                                             # De default grootte waarmee matplotlib een foto opslaat is aan de kleine kant, hiermee pas ik de grootte aan van het plaatje. 
fig.savefig('../images/Fourier_zaagtandgolf.png', bbox_inches='tight', dpi=200)  
# En als laatste sla het plaatje op.
plt.show()

# 6.3b
t = np.linspace(0,1,num=1000)                                                                                # Maakt een linspace aan
# kwadratische verschillen zaagtandgolf driehoeksgolf:
print('Driehoeksgolf:')
print( 'Het totale kwadratisch verschil bij 2 Fourier coefficienten is:', 
        tot_kwadratisch_verschil(driehoek_golf(t, f_0=1), fourierreeks(t, gen_coefs_driehoeksgolf(2), 1)) )   # Bereken  en print het kwadratisch verschil bij 2 Fourier coeffiecienten

print( 'Het totale kwadratisch verschil bij 5 Fourier coefficienten is:',
        tot_kwadratisch_verschil(driehoek_golf(t, f_0=1), fourierreeks(t, gen_coefs_driehoeksgolf(5), 1)) )   # ... bij 5 Fourier coefficienten

print( 'Het totale kwadratisch verschil bij 10 Fourier coefficienten is:',
        tot_kwadratisch_verschil(driehoek_golf(t, f_0=1), fourierreeks(t, gen_coefs_driehoeksgolf(10), 1)) )  # etc

print( 'Het totale kwadratisch verschil bij 15 Fourier coefficienten is:',
        tot_kwadratisch_verschil(driehoek_golf(t, f_0=1), fourierreeks(t, gen_coefs_driehoeksgolf(15), 1)) )

# kwadratische verschillen zaagtandgolf:
print('Zaagtandgolf:')
print( 'Het totale kwadratisch verschil bij 2 Fourier coefficienten is:', 
        tot_kwadratisch_verschil(zaagtand_golf(t, f_0=1), fourierreeks(t, gen_coefs_zaagtandgolf(2), 1)) )  

print( 'Het totale kwadratisch verschil bij 5 Fourier coefficienten is:',
        tot_kwadratisch_verschil(zaagtand_golf(t, f_0=1), fourierreeks(t, gen_coefs_zaagtandgolf(5), 1)) )  

print( 'Het totale kwadratisch verschil bij 10 Fourier coefficienten is:',
        tot_kwadratisch_verschil(zaagtand_golf(t, f_0=1), fourierreeks(t, gen_coefs_zaagtandgolf(10), 1)) )  

print( 'Het totale kwadratisch verschil bij 15 Fourier coefficienten is:',
        tot_kwadratisch_verschil(zaagtand_golf(t, f_0=1), fourierreeks(t, gen_coefs_zaagtandgolf(15), 1)) )

# 6.3c
t = np.linspace(0,1,num=1000)                                                               # Maakt een linspace aan voor het vergelijken van het kwadratisch verschil.
n = np.linspace(1,50,num=50)                                                                # Maakt een linspace aan voor het aantal Fourier coefficienten.
                                                            
out_list_driehoek = np.array([])                                                            # Initializeer de lijsten.
out_list_zaagtand = np.array([])
for i in n:                                                                                 # Bereken de kwadratische verschillen
    out_list_driehoek = np.append(out_list_driehoek, tot_kwadratisch_verschil( driehoek_golf(t, f_0 = 1), fourierreeks( t, gen_coefs_driehoeksgolf(int(i)), 1 ) ))
    out_list_zaagtand = np.append(out_list_zaagtand, tot_kwadratisch_verschil( zaagtand_golf(t, f_0 = 1), fourierreeks( t, gen_coefs_zaagtandgolf(int(i)), 1 ) ))

fig, ax = plt.subplots(1, 2)                                                                # Initializeert het matplotlib figuur.
ax[0].plot(n, out_list_driehoek)                                                            # Plot het verschil tegen het aantal coefficienten
ax[0].set_yscale('log')                                                                     # Zet de yas op log schaal
ax[0].title.set_text('Kwadratisch verschil driehoeksgolf')                                  # Zet de titel van de subplot

ax[1].plot(n, out_list_zaagtand)
ax[1].set_yscale('log')
ax[1].title.set_text('Kwadratisch verschil Zaagtandgolf')

plt.gcf().set_size_inches(8, 3.5)                           
fig.savefig('../images/tot_kwadratisch_verschil.png', bbox_inches='tight', dpi=200)         # Sla het bestand op
plt.show()














# t = np.linspace(0,1,num=100)
# plt.figure() 
# plt.plot(t, fourierreeks(t, np.array([1,2]), 1))
# plt.xlabel("t")


# opdracht 6.2b, plot van D(t), Z(t) en S(t)
# t = np.linspace(0,1,num=1000)
# plt.figure() 
# plt.plot(t,  driehoek_golf(t, f_0=1), label = 'D(t)')
# plt.plot(t, zaagtand_golf(t, f_0=1), label = 'Z(t)')
# plt.plot(t, sinus_golf(t, f_0=1), label = 'S(t)')
# plt.show()















