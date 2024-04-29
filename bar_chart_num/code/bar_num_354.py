
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',3000,4000], ['UK',2800,4200], ['Germany',2500,4500], ['France',2300,4600]]

country = [country[0] for country in data]
carbon_emissions = [country[1] for country in data]
energy_usage = [country[2] for country in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.bar(country, carbon_emissions, label='Carbon Emissions(Tons)', color='b')
ax.bar(country, energy_usage, bottom=carbon_emissions, label='Energy Usage(Kwh)', color='r')
plt.xticks(np.arange(len(country)), country)
ax.set_ylabel('Units')
ax.set_title('Carbon Emissions and Energy Usage in four countries in 2021')
ax.legend(loc='upper left')

for i, v in enumerate(carbon_emissions):
    ax.text(i - 0.2, v+200, str(v), color='b', fontweight='bold')

for i, v in enumerate(energy_usage):
    ax.text(i - 0.2, v+200, str(v), color='r', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/369.png')
plt.clf()