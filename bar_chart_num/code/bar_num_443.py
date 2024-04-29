
import matplotlib.pyplot as plt
import numpy as np

CO2_Emissions = [5500, 4000, 5000, 4500]
Renewable_Energy = [10, 20, 15, 25]
Country = ["USA", "UK", "Germany", "France"]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(Country, CO2_Emissions, label="CO2 Emissions(kt)", bottom=0)
ax.bar(Country, Renewable_Energy, label="Renewable Energy(%)", bottom=CO2_Emissions)
plt.xticks(Country, rotation=45)
ax.legend(loc='upper left')
plt.title('CO2 emissions and percentage of renewable energy in four countries in 2021')
for i, v in enumerate(CO2_Emissions):
    ax.text(i - 0.1, v + 0.2, str(v), color='blue', fontweight='bold')
for i, v in enumerate(Renewable_Energy):
    ax.text(i - 0.1, CO2_Emissions[i] + v + 0.2, str(v), color='green', fontweight='bold')
plt.tight_layout()
plt.savefig('Bar Chart/png/532.png')
plt.clf()