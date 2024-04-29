

import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(12, 6))

# Generate data
Year = np.array([2018, 2019, 2020, 2021, 2022])
Online_Sales = np.array([500, 600, 800, 1000, 1200])
Store_Sales = np.array([400, 500, 600, 800, 1000])

# Plot the data
plt.plot(Year, Online_Sales, marker='o', color='blue', label='Online Sales')
plt.plot(Year, Store_Sales, marker='o', color='red', label='Store Sales')

# Set the title
plt.title('Comparison of Online and Store Sales from 2018 to 2022')

# Set x, y limits
plt.xlim(2018, 2022)
plt.ylim(0, 1300)

# Set xticks
plt.xticks(Year)

# Set the grid
plt.grid(True, linestyle='-.', color='#333333', linewidth=1)

# Set legend
plt.legend(loc='upper left')

# Set tight_layout
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/46.png')

# Clear the current image state
plt.clf()