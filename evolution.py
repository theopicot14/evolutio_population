import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

max_generation = 100

temps = np.arange(0,max_generation, 1)

r = st.slider("entrer nb enfant/organisme au départ :", #nombre d'enfant au départ
                min_value = 0.,
                max_value = 4.,
                value = 2.0,
                step = .1)

x0 = st.slider("entrer la densité d'organisme au départ :", #taille de la pop au départ
                min_value = .01, 
                max_value = 1., 
                value = .1, 
                step = .01) 

pop = np.zeros_like(temps, dtype=float) #remplie un tableau de la taille de temps avec des zéros
pop[0] = x0 #condition innitiale (premiere valeur = x0)

for i in range(max_generation-1): # boucle pour calucler la densité de population au cours des générations      
    pop[i+1] = r*(1-pop[i])*pop[i] # la taille de la population de la génération i+1 = r*(1-la pop à la génération i/0) *pop a la generation i (pour la compétition)

#calculs cobweb plot
cobx = np.repeat(pop, 2) # doublonne chaque coordonée de pop dans cobx
coby = np.concatenate(([0.], cobx[2:])) # rajoute une valeur(0) et enlève la première génération
cobx = cobx[:-1] # enlève la dernière valeur pour que cobx et coby aient la même taille

abscisse = np.arange(0, 1.02, 0.02)

ordo1 = abscisse
ordo2 = r*abscisse*(1-abscisse)

#representation graphique
fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(14,8))

#densité de population au cours du temps
ax2.plot(temps, pop, 
        color = "C1", 
        linewidth = 3, 
        label = "avec nb d'enfant/organisme au départ={}".format(r))

ax2.set_xlabel('temps', fontsize=12, color="brown") #légendes de ax2
ax2.set_ylabel('pop', fontsize=12, color="brown")

ax2.legend(fontsize = 12)
ax2.grid()
ax2.axis([-1, 100, 0, 1]) #limite des axes

#cobweb plot
ax3.plot(cobx, coby, 
        color = "C2", 
        linewidth = 3,
        label = "avec nb d'enfant/organisme={}".format(r))
ax3.plot(abscisse, ordo1, color = "C3", linewidth = 3)
ax3.plot(abscisse, ordo2, color = "C1", linewidth = 3)


ax3.set_xlabel('$x_n$', fontsize=14, color="brown") #légendes de ax3
ax3.set_ylabel('$x_{n+1}$', fontsize=14, color="brown")

ax3.legend(fontsize = 12)
ax3.grid()
ax3.axis([0, 1, 0, 1]) #limite des axes

fig2.suptitle("Evolution du nombre d'organismes dans une population \n en fonction du temps et du nombre d'enfant/organisme",
             fontsize = 16)

st.pyplot(fig2)
