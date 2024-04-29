
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(8)
solar_energy = [200,250,300,350,400,450,500,550]
wind_energy = [400,450,500,550,600,650,700,750]

plt.figure(figsize=(8, 6))
plt.plot(x, solar_energy, 's-', label='Solar Energy')
plt.plot(x, wind_energy, 'o-', label='Wind Energy')
plt.xticks(x, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'))
plt.title('Renewable Energy Production in 2020')
plt.xlabel('Month')
plt.ylabel('Energy Production')
plt.legend(loc='lower right')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/14.png')
plt.clf()