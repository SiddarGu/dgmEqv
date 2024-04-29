
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[20000, 1200, 1000], [15000, 1400, 1100], [17000, 1600, 1200], [18000, 1800, 1400]])
region = ["North America", "South America", "Europe", "Asia"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(region, data[:, 0], label="Trucks", bottom=data[:, 1]+data[:, 2])
ax.bar(region, data[:, 1], label="Trains", bottom=data[:, 2])
ax.bar(region, data[:, 2], label="Ships")

ax.set_title("Number of trucks, trains, and ships in four regions in 2021")
ax.set_xticks(region)
ax.legend(loc='upper right')

x_offset = -0.3
y_offset = 0
for i, (trucks, trains, ships) in enumerate(data):
    ax.annotate('{}'.format(trucks), (region[i], trucks/2 + y_offset), xytext=(x_offset, y_offset), textcoords='offset points', fontsize=12)
    ax.annotate('{}'.format(trains), (region[i], trucks + trains/2 + y_offset), xytext=(x_offset, y_offset), textcoords='offset points', fontsize=12)
    ax.annotate('{}'.format(ships), (region[i], trucks + trains + ships/2 + y_offset), xytext=(x_offset, y_offset), textcoords='offset points', fontsize=12)

plt.tight_layout()
plt.savefig('Bar Chart/png/621.png')
plt.clf()