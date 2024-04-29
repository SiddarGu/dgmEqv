
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot() 

# Set labels
labels = ['Youtube', 'Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat', 'WhatsApp', 'Reddit', 'Other']

# Set data
sizes = np.array([25, 20, 15, 10, 10, 10, 5, 3, 2])

# Set colors
colors = ['#EA7500', '#0B3C49', '#7F8FA6', '#F2CF00', '#00A6AC', '#FF0097', '#F6F6F6', '#EF3E36', '#4D2A68']

# Plot pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10}, wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'dashed'})

# Set legend outside of chart and make sure it doesn't interfere with the chart
plt.legend(labels, bbox_to_anchor=(1.2, 0.5), loc="center right", fontsize=10, borderaxespad=0.1)

# Set title
plt.title('Social Media Platforms Usage in the US, 2023', fontsize=15)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/242.png')

# Clear the current image state
plt.clf()