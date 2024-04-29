
import matplotlib.pyplot as plt 
import numpy as np

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Data
data = [['USA',100,2],['UK',90,1.5],['Germany',80,1.7],['France',70,1.3]]
country = [x[0] for x in data] 
rnd = [x[1] for x in data] 
engineers = [x[2] for x in data]

# Plot bar chart
ax.bar(country, rnd, label='Research &Development(billion)')
ax.bar(country, engineers, bottom=rnd, label='Engineers(million)')

# Set labels
ax.set_xlabel('Country')
ax.set_ylabel('Amount')

# Set title
ax.set_title('Research &Development and Engineers in four countries in 2021')

# Set legend
ax.legend(loc='upper left')

# Set xticks
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country, rotation=45, wrap=True)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/254.png')

# Clear the image state
plt.clf()