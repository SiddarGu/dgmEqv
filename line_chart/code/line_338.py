
import matplotlib.pyplot as plt
import numpy as np

# Set data
year = [2019, 2020, 2021, 2022, 2023]
solar_energy = [5000, 7000, 9000, 11000, 13000]
wind_energy = [3000, 4000, 5000, 6000, 7000]
hydro_energy = [1000, 2000, 4000, 6000, 8000]

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# Plot
ax.plot(year, solar_energy, label='Solar Energy Production(kWh)')
ax.plot(year, wind_energy, label='Wind Energy Production(kWh)')
ax.plot(year, hydro_energy, label='Hydro Energy Production(kWh)')

# Add title and labels
ax.set_title('Renewable Energy Production in the UK from 2019-2023')
ax.set_xlabel('Year')
ax.set_ylabel('Production(kWh)')

# Add grid
ax.grid(linestyle='--', linewidth=0.5, alpha=0.5)

# Set ticks and limits
ax.set_xticks(np.arange(min(year), max(year) + 1, 1.0))
ax.set_ylim(0, 14000)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/205.png')

# Clear figure
plt.clf()