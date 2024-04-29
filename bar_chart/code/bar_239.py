
import matplotlib.pyplot as plt
import numpy as np

# Create data
Country = ['USA','UK','Germany','France']
Crops = [200,250,220,230]
Milk = [10000,12000,11000,12500]
Meat = [6000,7000,8000,9000]

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Plot data
ax.bar(Country, Crops, label='Crops')
ax.bar(Country, Milk, bottom=Crops, label='Milk Production (tons)')
ax.bar(Country, Meat, bottom=np.array(Crops)+np.array(Milk), label='Meat Production (tons)')

# Add title and labels
ax.set_title('Agricultural production of crops, milk, and meat in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Production (tons)')

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Resize image
plt.tight_layout()

# Set xticks
plt.xticks(Country)

# Save figure
plt.savefig('bar chart/png/428.png')

# Clear figure
plt.clf()