
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,5))

# Define data
Country = ('USA', 'UK', 'Germany', 'France')
Painting = (100, 80, 90, 120)
Sculpture = (50, 60, 70, 40)
Photography = (200, 220, 190, 210)

x = np.arange(len(Country))
width = 0.2

# Plotting
ax = fig.add_subplot()
ax.bar(x-width, Painting, width, label='Painting', color='#FFD700')
ax.bar(x, Sculpture, width, label='Sculpture', color='#FF8C00')
ax.bar(x+width, Photography, width, label='Photography', color='#FF1493')

# Set xticks
ax.set_xticks(x)
ax.set_xticklabels(Country, fontsize=10, rotation=0, wrap=True)

# Set title
ax.set_title("Number of artworks in four countries in 2021")

# Show legend
ax.legend(loc="upper right")

# Resize the image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/337.png')

# Clear figure
plt.clf()