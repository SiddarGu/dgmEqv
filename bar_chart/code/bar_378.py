
import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting
plt.figure(figsize=(10, 6))

# Create data
year = ['2020', '2021', '2022', '2023']
renewable_energy = [11, 12, 14, 15]
pollutants = [400, 410, 420, 430]
CO2_emission = [3700, 3500, 3200, 3000]

# Draw the bar chart
bar_width = 0.2
x1 = np.arange(len(renewable_energy))
x2 = x1 + bar_width
x3 = x2 + bar_width

ax = plt.subplot()
ax.bar(x1, renewable_energy, bar_width, label='Renewable Energy(%)')
ax.bar(x2, pollutants, bar_width, label='Pollutants(ppm)')
ax.bar(x3, CO2_emission, bar_width, label='CO2 Emission(million tons)')
ax.set_xticks(x2)
ax.set_xticklabels(year, rotation=45, ha='right', wrap=True)
ax.set_title('Environmental sustainability indicators from 2020 to 2023')
ax.legend(loc='upper left')

# Customize grid
ax.grid(axis='y', linestyle='--', linewidth=2)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/67.png', dpi=100)

# Clear the current image state
plt.clf()