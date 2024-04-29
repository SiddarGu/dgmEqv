
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 10))

# Data to plot
labels = ['Single-Family Homes','Townhomes','Condominiums','Multi-Family Homes']
sizes = [50,30,10,10]

# Plot
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Title
ax.set_title('Distribution of Home Types in the USA in 2023', fontsize=20)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Adjust space between chart and legend
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/401.png')

# Clear the current image state
plt.clf()