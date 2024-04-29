
import matplotlib.pyplot as plt
import numpy as np

# Set data
Month = ['January', 'February', 'March', 'April']
Production_A = [1000, 1200, 800, 1500]
Production_B = [800, 900, 1100, 1200]
Production_C = [1200, 1100, 1300, 1400]
Production_D = [1500, 1600, 1200, 800]

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot data
ax.plot(Month, Production_A, label='Production A(thousand tons)', marker='o', linestyle='--', color='red')
ax.plot(Month, Production_B, label='Production B(thousand tons)', marker='^', linestyle='-.', color='green')
ax.plot(Month, Production_C, label='Production C(thousand tons)', marker='d', linestyle=':', color='blue')
ax.plot(Month, Production_D, label='Production D(thousand tons)', marker='s', linestyle='-', color='black')

# Setting x ticks
xticks = np.arange(len(Month))
ax.set_xticks(xticks)
ax.set_xticklabels(Month, rotation=30, wrap=True)

# Set legend, title and grid
ax.legend(bbox_to_anchor=(1.01, 1.0))
ax.set_title('Crop Production in Four Provinces of China in 2021')
ax.grid()

# Save image
plt.tight_layout()
plt.savefig('line chart/png/295.png')

# Clear image
plt.cla()