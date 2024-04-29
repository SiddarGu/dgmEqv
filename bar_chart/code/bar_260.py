
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = ['North America', 'South America', 'Europe', 'Asia']
num_orgs = [2000, 3000, 4000, 5000]
donations = [50, 60, 70, 80]

# Create figure before plotting
fig, ax = plt.subplots(figsize=(10,6))

# Plot the data
ax.bar(labels, num_orgs, label="Organizations")
ax.bar(labels, donations, bottom=num_orgs, label="Donations (millions)")

# Set title
ax.set_title('Number of Charitable Organizations and Donations in Four Regions in 2021')

# Set x-axis labels
ax.set_xticklabels(labels, rotation=45, wrap=True)

# Set legend
ax.legend(loc='upper left')

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save the image
plt.savefig('bar chart/png/364.png')

# Clear the current image state
plt.clf()