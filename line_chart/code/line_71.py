
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 4))
month = ['January', 'February', 'March', 'April', 'May']
wind = [1000, 1400, 1500, 1800, 1300]
solar = [1200, 1100, 1300, 1400, 1600]
hydro = [800, 900, 1200, 1600, 1000]

plt.plot(month, wind, label='Wind Energy(kWh)', marker='o')
plt.plot(month, solar, label='Solar Energy(kWh)', marker='o')
plt.plot(month, hydro, label='Hydro Energy(kWh)', marker='o')

plt.xticks(month, rotation=45, wrap=True)
plt.title('Renewable energy use in the US during the first half of 2021')
plt.xlabel('Month')
plt.ylabel('Energy(kWh)')
plt.legend(loc=2)
plt.tight_layout()
plt.savefig('line chart/png/246.png', dpi=200)
plt.clf()