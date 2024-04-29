
import matplotlib.pyplot as plt
import numpy as np

# Define data
country = ['USA', 'UK', 'Germany', 'France']
manufacturing_output_level = [3000, 2500, 1800, 2100]

# Create figure and plot data
fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)
ax.bar(country, manufacturing_output_level, color='#539caf')

# Set title and labels
ax.set_title('Manufacturing output levels and quantities in four countries in 2021', fontsize=14)
ax.set_xlabel('Country')
ax.set_ylabel('Manufacturing Output Quantity')

# Adjust the x-axis
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country, rotation=30, ha="right")

# Fix the legend
ax.legend(['Manufacturing Output Level'], loc='upper right')

# Resize the image
plt.tight_layout()

# Save the image
fig.savefig('bar chart/png/499.png')

# Clear the image state
plt.clf()