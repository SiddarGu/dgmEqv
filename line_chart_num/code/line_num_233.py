
import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Set data
month = ['January', 'February', 'March', 'April', 'May']
wind_speed = [14, 17, 15, 20, 18]
air_pressure = [1000, 1010, 1025, 1050, 1020]
humidity = [60, 58, 62, 55, 67]
precipitation = [3.5, 5.3, 4.2, 4.8, 3.9]

# Plot line chart
ax.plot(month, wind_speed, color='royalblue', label='Wind Speed(mph)')
ax.plot(month, air_pressure, color='green', label='Air Pressure(mbar)')
ax.plot(month, humidity, color='red', label='Humidity(%)')
ax.plot(month, precipitation, color='gold', label='Precipitation(mm)')

# Set xticks
x_ticks = np.arange(len(month))
ax.set_xticks(x_ticks)
ax.set_xticklabels(month, rotation=45, ha='right')

# Set title
ax.set_title('Weather conditions in the city of San Francisco in 2021', fontsize=15)

# Set legend
ax.legend(loc='best', fontsize=14, framealpha=0.5)

# Set labels
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Value', fontsize=14)

# Set grids
ax.grid(ls='--', color='gray', alpha=0.5)

# Add text
for x, y, txt in zip(x_ticks, wind_speed, wind_speed):
    ax.annotate(txt, (x, y), fontsize=14, va='center')
for x, y, txt in zip(x_ticks, air_pressure, air_pressure):
    ax.annotate(txt, (x, y), fontsize=14, va='center')
for x, y, txt in zip(x_ticks, humidity, humidity):
    ax.annotate(txt, (x, y), fontsize=14, va='center')
for x, y, txt in zip(x_ticks, precipitation, precipitation):
    ax.annotate(txt, (x, y), fontsize=14, va='center')

# Resize image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/324.png')

# Clear current image state
plt.clf()