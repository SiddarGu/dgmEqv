
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

# Data 
Country = ['USA','UK','Germany','France']
Museums = [50,55,45,60]
Theaters = [60,65,70,75]
Galleries = [70,75,80,85]

# Plot
width = 0.2
x = np.arange(len(Country))
ax.bar(x - width, Museums, width, label='Museums')
ax.bar(x, Theaters, width, label='Theaters')
ax.bar(x + width, Galleries, width, label='Galleries')

# Set labels, title, legend
ax.set_ylabel('Number of Venues')
ax.set_xticks(x)
ax.set_xticklabels(Country, rotation=45, ha='right')
ax.set_title('Number of Arts and Culture venues in four countries in 2021')
ax.legend()

fig.tight_layout()

# Save figure
plt.savefig("bar chart/png/365.png")

# Clear current image state
plt.clf()