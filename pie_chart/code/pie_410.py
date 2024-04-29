
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 10))

# Set data
labels = ['Facebook', 'YouTube', 'Instagram', 'Twitter', 'Other']
sizes = [30, 25, 20, 10, 15]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14, 'wrap': True}) 

# Title
plt.title("Popular Social Media Platforms Usage in the US, 2023", fontsize=18)

# Save as image
plt.savefig('pie chart/png/445.png', bbox_inches='tight')

# Clear current image
plt.clf()