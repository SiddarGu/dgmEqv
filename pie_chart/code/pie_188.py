
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(7,7))

# Data to plot
labels = 'Studio', '1 Bedroom', '2 Bedrooms', '3 Bedrooms', '4+ Bedrooms'
sizes = [7, 21, 37, 28, 7]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 15})

# Title
plt.title('Distribution of Home Sizes in the US Housing Market in 2023', fontsize=18)

# Tight layout
plt.tight_layout()

# Save
plt.savefig('pie chart/png/14.png')

# Clear
plt.clf()