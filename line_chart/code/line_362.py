

import numpy as np
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']
solar_energy = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 2000, 2200]
wind_energy = [1400, 1100, 1000, 1300, 1400, 1200, 1000, 1300, 1200]

# Create figure before plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Plot the data
ax.plot(months, solar_energy, color='red', linewidth=2, label='Solar Energy', marker="o")
ax.plot(months, wind_energy, color='blue', linewidth=2, label='Wind Energy', marker="o")

# Add grid
ax.grid(linestyle='--', linewidth=0.5)

# Add legend
ax.legend(loc='upper right', fontsize=14)

# Add title
ax.set_title('Renewable Energy Production in the US in 2023', fontsize=16)

# Set xticks
plt.xticks(rotation = 90)

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save image
plt.savefig('line chart/png/300.png', bbox_inches='tight')

# Clear the image state
plt.cla()