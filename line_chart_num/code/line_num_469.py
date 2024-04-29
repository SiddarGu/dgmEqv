
import matplotlib.pyplot as plt
import numpy as np

month = ['January', 'February', 'March', 'April', 'May', 'June']
wind_energy = [1000,1200,1500,1300,1100,1400]
solar_energy = [600,700,800,650,750,850]
hydro_energy = [400,500,450,600,400,550]

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(month, wind_energy, label='Wind Energy (MW)', color='blue', marker='o')
ax.plot(month, solar_energy, label='Solar Energy (MW)', color='red', marker='o')
ax.plot(month, hydro_energy, label='Hydro Energy (MW)', color='green', marker='o')

for x, y in zip(month, wind_energy):
    label = "{:.0f}".format(y)
    ax.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x, y in zip(month, solar_energy):
    label = "{:.0f}".format(y)
    ax.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x, y in zip(month, hydro_energy):
    label = "{:.0f}".format(y)
    ax.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

ax.set_title('Comparative Energy Output of Wind, Solar, and Hydro Sources in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Energy (MW)')

plt.xticks(month)
ax.grid(linestyle=':')
ax.legend(loc='lower left')
plt.tight_layout()
plt.savefig('line chart/png/95.png')
plt.clf()