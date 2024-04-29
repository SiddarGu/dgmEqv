
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

month = ['January', 'February', 'March', 'April']
wind_energy = [500, 550, 600, 650]
solar_energy = [800, 850, 900, 950]
hydro_energy = [300, 400, 450, 500]

ax.bar(month, wind_energy, width=0.2,  label='Wind', color='b', bottom=solar_energy)
ax.bar(month, solar_energy, width=0.2, label='Solar', color='g', bottom=hydro_energy)
ax.bar(month, hydro_energy, width=0.2, label='Hydro', color='r')

plt.xticks(rotation=45)
plt.title('Energy production from Wind, Solar and Hydro sources from January to April 2021')
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('bar chart/png/302.png')
plt.clf()