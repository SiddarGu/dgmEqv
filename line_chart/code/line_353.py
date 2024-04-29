

import matplotlib.pyplot as plt
import numpy as np

# Read data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
production_A = [500, 600, 550, 650, 750, 650, 800, 900]
production_B = [400, 450, 400, 500, 550, 450, 550, 600]
production_C = [600, 550, 650, 700, 850, 700, 900, 1000]
production_D = [800, 900, 900, 800, 900, 1000, 1100, 1200]

# Create figure
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# Plot line chart
ax.plot(months, production_A, '-o', color='red', label='Production A')
ax.plot(months, production_B, '-o', color='green', label='Production B')
ax.plot(months, production_C, '-o', color='blue', label='Production C')
ax.plot(months, production_D, '-o', color='violet', label='Production D')

# Set x ticks
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45, wrap=True)

# Add title
plt.title('Manufacturing production changes in the first eight months of 2021', fontsize=18)

# Add legend
plt.legend(loc='upper right')

# Adjust figure size
plt.tight_layout()

# Save image
plt.savefig('line chart/png/37.png')

# Clear current image state
plt.clf()