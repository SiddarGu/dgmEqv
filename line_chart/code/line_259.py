
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(8,6))

# Set data
data = np.array([[2020,2,3,4],
                 [2021,3,4,5],
                 [2022,4,5,6],
                 [2023,5,6,7],
                 [2024,6,7,8]])

# Set labels
labels = ['Air Travel (million passengers)',
          'Rail Travel (million passengers)',
          'Road Travel (million passengers)']

colors = ['blue','green','orange']

# Plot data
ax = plt.subplot()
for i in range(1,data.shape[1]):
    ax.plot(data[:,0], data[:,i], color=colors[i-1], label=labels[i-1])

# Set title
ax.set_title('Transportation Mode Usage in the US in 2020-2024')

# Set xlim and ylim
ax.set_xlim(2020, 2024)
ax.set_ylim(2, 8)

# Set x-axis label
ax.set_xlabel('Year')

# Set xticks
xticks = np.arange(2020, 2025, 1)
ax.set_xticks(xticks)

# Set legend
ax.legend(loc='upper left')

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/411.png')

# Clear figure
plt.clf()