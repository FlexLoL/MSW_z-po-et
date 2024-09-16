import random
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo(zakladni_hodnota, pocet_iteraci):
    hodnota_pri_simulaci = [zakladni_hodnota]
    hodnota = zakladni_hodnota

    # Simulace každého kroku (hod mincí)
    for hod in range(pocet_iteraci):
        hod_minci = random.choice(['hlava', 'orel'])
        
        if hod_minci == 'hlava':
            hodnota *= 1.80  # Zvětší o 80 %
        else:
            hodnota *= 0.50  # Zmenší o 50 %
        
        hodnota_pri_simulaci.append(hodnota)
    
    return hodnota_pri_simulaci

zaklad = 100  
pocet_iteraci = 10  
pocet_simulaci = 5  

vysledeky_simulaci = []
for sim in range(pocet_simulaci):
    simulace = monte_carlo(zaklad, pocet_iteraci)
    vysledeky_simulaci.append(simulace)

# Vytvoření grafu pro vývoj hodnoty během kroků
plt.figure(figsize=(10, 7))

for i, simulace in enumerate(vysledeky_simulaci):
    plt.plot(range(pocet_iteraci+1), simulace, marker='o', label=f'Simulace {i+1}')

# Osy a legenda
plt.axhline(y=zaklad, color="r", linestyle="-")
plt.title('Vývoj hodnoty během hodů mincí')
plt.xlabel('Počet hodů')
plt.ylabel('Hodnota')
plt.legend()
plt.grid(True)

plt.show()
