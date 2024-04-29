

import matplotlib.pyplot as plt
import numpy as np
 
Month = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])
Electricity_Production = np.array([2500, 3000, 4000, 5000, 4500, 6000, 7000, 6500])
Coal_Consumption = np.array([30000, 35000, 45000, 50000, 55000, 40000, 30000, 25000])
 
# Create a figure with subplots
fig, ax = plt.subplots(figsize=(8, 6))
 
# Plot the line chart
ax.plot(Month, Electricity_Production, label='Electricity Production(MW)', marker='o')
ax.plot(Month, Coal_Consumption, label='Coal Consumption(tons)', marker='o')
 
# Get the current figure axes
axes = plt.gca()
# Set the x,y axis max and min
axes.set_ylim([0, 8500])
axes.set_xlim([0, 8])
# Setting X-ticks
x_tick_position = np.arange(1, len(Month)+1)
ax.set_xticks(x_tick_position)
ax.set_xticklabels(Month)
 
# Add a title and a legend
plt.title('Monthly electricity production and coal consumption in 2021')
plt.legend()
# Add value of each data point
for a, b in zip(Month, Electricity_Production):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
for a, b in zip(Month, Coal_Consumption):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
 
# Automatically adjust the image size
plt.tight_layout()
# Save and show the figure
plt.savefig('line chart/png/129.png', format='png')
plt.show()

# Clear the current image state
plt.clf()