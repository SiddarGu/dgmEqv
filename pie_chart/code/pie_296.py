
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure(figsize=(10,10))

# Data to be plotted
platforms = ['Facebook', 'Instagram', 'Twitter', 'YouTube', 'Snapchat', 'Pinterest', 'LinkedIn', 'Other']
percentage = [35, 25, 15, 10, 5, 5, 5, 5]

# Plot the data
ax = fig.add_subplot(111)
ax.pie(percentage, labels=platforms,autopct='%1.1f%%', shadow=True, startangle=90)

# Add title to the figure
ax.set_title('Social Media Platform Usage in the USA, 2023', fontsize=15, wrap=True)
ax.legend(loc='lower right')

# Fit the figure to the axis
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/227.png')

# Clear the figure
plt.clf()