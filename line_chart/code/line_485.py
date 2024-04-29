
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Data
Age = [0, 6, 16, 26, 41, 61, 81]
AvgTemp = [37.2, 36.7, 36.6, 36.5, 36.4, 36.3, 36.2]
AvgHeartRate = [110, 97, 75, 75, 77, 85, 95]

# Plot line
ax.plot(Age, AvgTemp, color='red', label='Average body temperature(degrees Celcius)')
ax.plot(Age, AvgHeartRate, color='blue', label='Average heart rate(beats/min)')

# Grid
plt.grid(True, color='black', linestyle='dashed')

# Ticks
plt.xticks(Age)

# Legend
ax.legend(loc='best', frameon=False)

# Title
plt.title('Average body temperature and heart rate of different age groups', fontsize=14)

# Tight Layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/233.png')

# Clear figure
plt.clf()