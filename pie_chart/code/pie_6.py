
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Data to plot
labels = 'Solar','Wind','Hydropower','Geothermal','Nuclear','Biomass'
sizes = [20,25,20,15,15,5]
colors = ['yellowgreen','gold','lightskyblue','lightcoral','blue','red']

# Draw Pie Chart
ax.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', startangle=90)
ax.axis('equal')

# Set Title
ax.set_title("Distribution of Renewable Energy Sources in the US, 2023")

# Set display for labels
ax.legend(loc="upper left", bbox_to_anchor=(1,1), fontsize='large')

# Add background grid
ax.grid(color='w', linestyle='-', linewidth=0.5)

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/172.png')

# Clear image
plt.clf()