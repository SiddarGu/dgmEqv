
import matplotlib.pyplot as plt
import numpy as np

# Create a figure object
fig = plt.figure(figsize=(8, 8))
# Add a subplot
ax = fig.add_subplot(111)

# Data to plot
labels = 'Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass'
sizes = [25, 25, 20, 15, 15]

# Pie chart
patches, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, labeldistance=1.05)

# Equal aspect ratio
ax.axis('equal')
# Title
plt.title('Percentage of Renewable Resources in the World, 2023', fontsize=14) 
# Legend
plt.legend(loc='upper right', bbox_to_anchor=(1, 0.8))
# Resize the image
plt.tight_layout()
# Rotate the labels
for i, label in enumerate(labels):
    angle = (sizes[i]/sum(sizes))*360
    if angle > 90:
        texts[i].set_rotation(angle-180)
    else:
        texts[i].set_rotation(angle)

# Save the figure
plt.savefig('pie chart/png/25.png')

# Clear the current image state
plt.clf()