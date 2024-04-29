
import matplotlib.pyplot as plt
import numpy as np

# Set data
Region = ['North America', 'Europe', 'Asia', 'Africa']
Solar_Energy = [100, 120, 150, 90]
Wind_Energy = [200, 180, 220, 150]
Hydro_Energy = [150, 100, 200, 120]

# Set figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot data
ax.bar(Region, Solar_Energy, bottom=np.add(Wind_Energy, Hydro_Energy), label='Solar Energy (GWh)', width=.3, color='#FFA500')
ax.bar(Region, Wind_Energy, bottom=Hydro_Energy, label='Wind Energy (GWh)', width=.3, color='#00FFFF')
ax.bar(Region, Hydro_Energy, label='Hydro Energy (GWh)', width=.3, color='#00FF00')

# Set labels
ax.set_xlabel('Region', fontsize=14)
ax.set_xticks(Region)
ax.set_title('Energy production from Solar, Wind and Hydro sources in four regions in 2021', fontsize=16)
ax.legend(loc='upper right', fontsize=14)

# Set grid
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')

# Resize Figure
plt.tight_layout()

# Save Figure
plt.savefig('bar chart/png/125.png')

# Clear Figure
plt.clf()