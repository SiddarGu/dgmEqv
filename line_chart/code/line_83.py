
import matplotlib.pyplot as plt
import numpy as np

# Generate data.
data = np.array([[2010, 1000, 5, 60], 
                 [2011, 1100, 7, 55],
                 [2012, 1200, 10, 50],
                 [2013, 1300, 12, 45],
                 [2014, 1400, 15, 40],
                 [2015, 1500, 18, 35],
                 [2016, 1600, 20, 30]])

# Create figure.
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Get x, y data.
x_data = data[:, 0]
y1_data = data[:, 1]
y2_data = data[:, 2]
y3_data = data[:, 3]

# Plot data.
ax.plot(x_data, y1_data, label='Greenhouse Gas Emissions (million tons)', color='#8B008B', linestyle='-', marker='o', linewidth=2)
ax.plot(x_data, y2_data, label='Renewable Energy Usage (GW)', color='#FFA500', linestyle='-', marker='^', linewidth=2)
ax.plot(x_data, y3_data, label='Air Quality Index', color='#20B2AA', linestyle='-', marker='s', linewidth=2)

# Set title and legend.
ax.set_title('Environmental changes in the US between 2010 and 2016')
ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.legend(loc='best', fontsize=12, ncol=2)

# Set xticks.
plt.xticks(x_data, rotation=0)

# Resize.
plt.tight_layout()

# Save figure.
plt.savefig('line chart/png/185.png', dpi=300)

# Clear figure.
plt.clf()