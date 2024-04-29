
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 8))

# Data to plot
labels = ['Automotive','Aerospace','Industrial Machinery','Electronics','Food and Beverages','Chemicals','Textiles','Semiconductors','Other']
sizes = [20, 18, 15, 14, 10, 9, 7, 5, 12]

# Add subplot
ax = fig.add_subplot()

# Plot
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14}, wedgeprops={'linewidth': 1.5, 'edgecolor': 'black'})

# Add title
ax.set_title('Distribution of Manufacturing Sectors in the US, 2023', fontsize=20)

# Set legend
ax.legend(labels, loc="best", fontsize='large')

# Automatically resize the image
plt.tight_layout()

# Set xticks
plt.xticks(np.arange(0.0, 360.0, 90.0))

# Save the figure
plt.savefig('pie chart/png/95.png')

# Clear the current image state
plt.clf()