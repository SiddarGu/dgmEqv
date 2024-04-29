
import matplotlib.pyplot as plt
import numpy as np

year = [2021, 2022, 2023, 2024]
CO2_emission = [1000, 800, 700, 900]
Renewable_energy = [800, 900, 1100, 1200]

plt.figure(figsize=(10, 6))
plt.plot(year, CO2_emission, label='CO2 emission')
plt.plot(year, Renewable_energy, label='Renewable energy')
plt.title('Carbon dioxide emission and Renewable energy production in the US from 2021-2024', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Amount', fontsize=12)
plt.xticks(year, fontsize=12)
plt.legend(fontsize=12, loc='upper right')

for a, b, c in zip(year, CO2_emission, Renewable_energy):
    plt.annotate('{},{}'.format(b, c), xy=(a, b), xytext=(a, b+50), fontsize=12, rotation=45, va='bottom', ha='right')

plt.tight_layout()
plt.savefig('line chart/png/403.png')
plt.clf()