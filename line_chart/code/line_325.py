
import numpy as np
import matplotlib.pyplot as plt

month = ['January', 'February', 'March', 'April', 'May']
Painting_A = [100, 105, 90, 95, 110]
Painting_B = [150, 155, 160, 145, 170]
Painting_C = [120, 125, 110, 115, 130]
Painting_D = [130, 135, 140, 145, 150]

# Create figure
fig = plt.figure(figsize=(7,5))

# Plot line chart
ax = fig.add_subplot(111)
ax.set_title('Number of Paintings Sold in Four Categories in 2021', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Number of Paintings (in thousands)', fontsize=14)
ax.plot(month, Painting_A, linewidth=2, label='Painting A')
ax.plot(month, Painting_B, linewidth=2, label='Painting B')
ax.plot(month, Painting_C, linewidth=2, label='Painting C')
ax.plot(month, Painting_D, linewidth=2, label='Painting D')

# Set x ticks with rotation
ax.set_xticks(np.arange(len(month)), minor=False)
ax.set_xticklabels(month, fontdict={'fontsize': 12}, rotation=45, ha='right')

# Set legend
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Set background grid
ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Resize figure
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/210.png', dpi=210)

# Clear current image state
plt.clf()