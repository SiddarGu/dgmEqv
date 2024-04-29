
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',20000, 28000],
        ['UK',25000, 30000],
        ['Germany',27000, 32000],
        ['France',24000, 35000]]

# Get the data
countries = [row[0] for row in data]
crops = [row[1] for row in data]
livestock = [row[2] for row in data]

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# Plot the data
ax.bar(countries, crops, label='Crops', color='#FFBB00', bottom=livestock)
ax.bar(countries, livestock, label='Livestock', color='#0099FF')

# Add labels
for i, j in enumerate(livestock):
    ax.annotate(str(j), xy=(i-0.2, j/2))
for i, j in enumerate(crops):
    ax.annotate(str(j), xy=(i-0.2, j+livestock[i]/2))

# Add legend and title
ax.legend(loc='upper left')
ax.set_title('Crop and livestock production in four countries in 2021')

# Adjust parameters
ax.set_xticks(np.arange(len(countries)))
ax.set_xticklabels(countries, rotation=45, ha="right", wrap=True)
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/243.png')

# Clear current image
plt.clf()