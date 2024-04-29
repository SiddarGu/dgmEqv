

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

month = ['January','February','March','April','May','June','July','August','September','October','November','December']
electricity_usage = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]
solar_energy = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
wind_energy = [400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

plt.figure(figsize=(8,5))

plt.plot(month, electricity_usage, color='darkblue', linestyle='--', marker='o', label='Electricity Usage (kWh)')
plt.plot(month, solar_energy, color='orange', linestyle='-.', marker='o', label='Solar Energy Produced (kWh)')
plt.plot(month, wind_energy, color='green', linestyle=':', marker='o', label='Wind Energy Produced (kWh)')

plt.xticks(month)

plt.grid(axis='y', linestyle='-')

plt.title("Energy Usage and Production in a Household in 2021")

for i in range(len(month)):
    plt.annotate(electricity_usage[i], (month[i], electricity_usage[i]))
    plt.annotate(solar_energy[i], (month[i], solar_energy[i]))
    plt.annotate(wind_energy[i], (month[i], wind_energy[i]))

plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/590.png')
plt.clf()