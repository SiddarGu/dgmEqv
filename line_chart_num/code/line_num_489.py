
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12

# Set figure size
plt.figure(figsize=(9, 5))

# Set the title
plt.title("Traffic Volume on the M25 Motorway in London on April 1, 2021")

# Create subplot
ax = plt.subplot()

# Set x-axis and y-axis
x = np.arange(8)
daytime_traffic = [300, 250, 200, 150, 100, 75, 50, 25]
nighttime_traffic = [400, 350, 300, 250, 200, 150, 100, 50]

# Plot the data
ax.plot(x, daytime_traffic, color='blue', marker='o', linestyle='-', label='Daytime Traffic')
ax.plot(x, nighttime_traffic, color='red', marker='o', linestyle='-', label='Nighttime Traffic')

# Set xticks
ax.set_xticks(x)
ax.set_xticklabels(['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00'], rotation=45, ha='right', wrap=True)

# Add legend
ax.legend(loc='best')

# Add grids
ax.grid(axis='x', color='gray', linestyle='--', linewidth=0.3)
ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

# Add labels
for x_coord, y_coord in zip(x, daytime_traffic):
    plt.annotate(y_coord, (x_coord, y_coord), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=12)

for x_coord, y_coord in zip(x, nighttime_traffic):
    plt.annotate(y_coord, (x_coord, y_coord), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=12)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/611.png')

# Clear the current image state
plt.clf()