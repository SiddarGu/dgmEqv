
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure(figsize=(10, 8))

# Set the pie chart
labels = ['Business','Leisure','Education','Medical']
sizes = [20,60,10,10]

# Set the color of the pie chart
colors = ['#4d79ff', '#00b4d8', '#ff4d4d', '#ffb366']

# Set the position of the legend
plt.legend(labels, loc='upper left')

# Set the title of the figure
plt.title('Distribution of Tourists in the World, 2023')

# Set the fontsize
plt.rcParams['font.size'] = 16 

# Set the font
plt.rcParams['font.family'] = 'serif'

# Set the rotation
plt.axis('equal')

# Make sure xticks don't interpolate
plt.xticks(np.arange(0, 360, 45))

# Plot the Pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/284.png', format='png')

# Clear the image state
plt.clf()