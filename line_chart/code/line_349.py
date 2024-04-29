

import matplotlib.pyplot as plt
import numpy as np

# Set data
Month = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
Museum_Visits = np.array([200, 150, 180, 220, 190, 140, 100, 160, 170, 200, 150, 180])
Theater_Visits = np.array([100, 120, 150, 180, 140, 120, 90, 140, 120, 150, 90, 130])
Gallery_Visits = np.array([150, 90, 140, 110, 170, 160, 120, 150, 140, 180, 100, 160])

# Create figure and plot space
fig, ax = plt.subplots(figsize=(15, 7))

# Add x-axis and y-axis
ax.plot(Month, Museum_Visits, color='blue')
ax.plot(Month, Theater_Visits, color='red')
ax.plot(Month, Gallery_Visits, color='green')

# Set title and labels for axes
ax.set(xlabel="Month",
       ylabel="Visits",
       title="Cultural visits in the UK from January 2021 to December 2021")

# Rotate tick labels
plt.xticks(rotation=45)

# Set legend
ax.legend()

# Use tight_layout so that long labels do not go out of the figure
plt.tight_layout()

# Save the figure
plt.savefig("line chart/png/265.png")

# Clear the current image state
plt.clf()